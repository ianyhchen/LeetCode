from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 1. Build the adjacency list and in-degree array
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1

        # 2. Add all courses with no prerequisites (in-degree 0) to the queue
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        order = []

        # 3. Process courses in the queue
        while queue:
            current_course = queue.popleft()           
            order.append(current_course)

            # Reduce the in-degree of each neighboring course
            for neighbor in graph[current_course]:
                in_degree[neighbor] -= 1

                # If in-degree becomes 0, it means all prerequisites are met
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # 4. If order length matches numCourses, no cycle exists     
        return order if len(order) == numCourses else []