# Last updated: 9/17/2025, 3:53:04 PM
class Solution:
    def findOrder(self, numCourses: int, pre: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in pre:
            graph[b].append(a)
            indegree[a] += 1
        

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return order if len(order) == numCourses else []