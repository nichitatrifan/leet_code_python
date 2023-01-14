from typing import List

class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        triangle = [[1]]

        if num_rows == 1 :
            return triangle

        for row in range(1, num_rows):
            current_row = [1]
            for col in range(1, row):
                current_row.append(triangle[row - 1][col - 1] + triangle[row - 1][col])
            current_row.append(1)
            triangle.append(current_row.copy())

        return triangle

if __name__ == "__main__":
    solution = Solution()
    print(solution.generate(5))