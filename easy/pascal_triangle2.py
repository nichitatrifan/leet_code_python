from typing import List

class Solution:
    def getRow(self, row_index: int) -> List[int]:
        if row_index == 0:
            return [1]
        elif row_index == 1:
            return [1,1]
        else:
            triangle = [1,1]
            for row in range(1, row_index + 1):
                current_row = [1]
                for col in range(1, row):
                    current_row.append(triangle[col - 1] + triangle[col])
                current_row.append(1)
                triangle = current_row.copy()

            return triangle


if __name__ == "__main__":
    solution = Solution()
    print(solution.getRow(3))