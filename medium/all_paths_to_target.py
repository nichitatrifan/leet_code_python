# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1,
# find all possible paths from "node 0" to "node n - 1" and return them in any order.

# The graph is given as follows: graph[i] is a list of all nodes you can visit
# from node i (i.e., there is a directed edge from node i to node graph[i][j]).

from typing import List

class Solution:
    # def depth_first_search_graph(self, vert: int, visited: List[int],  graph: List[List[int]]):
    #     """
    #     DFS of a directed graph
    #     Args:
    #         vert (int): the current node
    #         visited (List[int]): a list of visited nodes
    #         graph (List[List[int]]): graph
    #     """
    #     visited.append(vert)
    #     #print(vert, end=" ")
    #     for next in graph[vert]:
    #         if next not in visited:
    #             self.depth_first_search_graph(next, visited, graph)

    def depth_first_search_graph(self, vert: int, visited: List[int],  graph: List[List[int]], solutions: List[List[int]]):
        """
        DFS of a directed graph
        Args:
            vert (int): the current node
            visited (List[int]): a list of visited nodes
            graph (List[List[int]]): graph
        """
        visited.append(vert)
        if vert == len(graph) - 1:
            solutions.append(visited)
        else:
            for next in graph[vert]:
                if next not in visited:
                    self.depth_first_search_graph(next, visited.copy(), graph, solutions) # the problem is that visited needs to get updated

    def allPathsSourceTarget_first_try(self, graph: List[List[int]]) -> List[List[int]]:
        solutions = []
        for start_vert in graph[0]:
            path = [0]
            self.depth_first_search_graph(start_vert, path, graph, solutions)
        return solutions

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # when we have to return all possible solutions its a backtracking problem
        # when we backtrack we need to pop the current nodes from the

        # our algorithm is going to be based on depth first search.
        # but the condition is going to be the target node and not the
        # list of visited nodes
        solutions = []
        target = len(graph) - 1
        def depth_search(node:int, path:List[int]):
            path.append(node)
            if node == target:
                solutions.append(path.copy())
                return
            else:
                for next in graph[node]:
                    depth_search(next, path)
                    path.pop()
        depth_search(0, [])
        return solutions

if __name__ == '__main__':
    # input: [[4,3,1],[3,2,4],[3],[4],[]]
    # output:[[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
    solution = Solution()
    print(solution.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))
    # solution.depth_first_search_graph(1, [], [[1,2], [2], [0,3], [3]])