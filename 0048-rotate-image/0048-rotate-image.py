class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix[0]) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # save topleft
                topleft = matrix[top][l + i]

                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move topleft into top right
                matrix[top + i][r] = topleft
            
            r -= 1
            l += 1

# Note: could always transpose matrix and reverse each row either

# Time : O(N^2)
# Space: O(1), The rotation is performed in-place