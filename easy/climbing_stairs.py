# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?

class Solution:
    memory= {0 : 0}
    def climbStairs(self, n: int) -> int:
        if n in self.memory:
            return self.memory[n]
        elif n - 1 == 0 or n - 2 == 0:
            return n
        else:
            self.memory[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memory[n]


    paths = 0
    def climbStairs_inefficient(self, n: int)-> int:
        if n < 0:
            #print("path is incorrect")
            return n
        if n == 0:
            self.paths += 1
            #print("path is correct")
            return 0
        self.climbStairs_inefficient(n - 1)
        self.climbStairs_inefficient(n - 2)
        return self.paths

    def climbStairs2(self, n: int): #-> int:
        """finds the best path to climb the stairs

        Args:
            n (int): how many stairs to climg
        """
        if n == 0:
            print("0")
        elif n - 2 >= 0:
            print("-2")
            self.climbStairs2(n - 2)
        elif n - 1 >= 0:
            print("-1")
            self.climbStairs2(n - 1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.climbStairs(38))