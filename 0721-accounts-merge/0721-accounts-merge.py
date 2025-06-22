from collections import defaultdict
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = list(range(n))
        size   = [1] * n

        def find(i: int) -> int:
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i: int, j: int) -> bool:
            ri, rj = find(i), find(j)
            if ri == rj:
                return False
            if size[ri] < size[rj]:
                ri, rj = rj, ri
            parent[rj] = ri
            size[ri]  += size[rj]
            return True

        # link accounts by shared email
        email_to_idx = {}  # email → representative account index
        for i, acct in enumerate(accounts):
            for email in acct[1:]:
                if email in email_to_idx:
                    union(i, email_to_idx[email])
                else:
                    email_to_idx[email] = i

        # collect emails under each root account
        groups = defaultdict(list)  # root index → list of emails
        for email, i in email_to_idx.items():
            groups[find(i)].append(email)

        # build final merged accounts
        res = []
        for root, emails in groups.items():
            name = accounts[root][0]
            res.append([name] + sorted(emails))
        return res     

# Time complexity: O(N α(N) + N log N), Space complexity: O(N)