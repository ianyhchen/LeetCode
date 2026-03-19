'''
檢查這個依賴關係圖是否為一個 有向無環圖 (Directed Acyclic Graph, DAG)
'''

# BFS solution
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Initialize the adjacency list and in-degree array
        # graph[src] = [dest1, dest2, ...] means dest courses depend on src course
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        # 2. Build the graph and update in-degrees
        for dest, src in prerequisites:
            # prerequisite is [a, b], meaning b -> a
            graph[src].append(dest)
            in_degree[dest] += 1

        # 3. Add all courses with 0 in-degree (no prerequisites) to the queue
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        # 4. Process the queue
        count = 0 # To track how many courses we successfully completed
        while queue:
            # Take a course that can be finished
            current_course = queue.popleft()
            count += 1

            # Decrease in-degree for all courses that depend on current_course
            for neighbor in graph[current_course]:
                in_degree[neighbor] -= 1

                # If a neighbor's in-degree becomes 0, it has no remaining prerequisites
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # 5. Check if we were able to finish all courses (no cycle detected)
        return count == numCourses
    

#DFS solution
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Initialize the adjacency list
        graph = [[] for _ in range(numCourses)]
        for dest, src in prerequisites:
            # [a, b] means b -> a
            graph[src].append(dest)

        # 2. States array: 0 = unvisited, 1 = visiting, 2 = visited
        # This state helps differentiate between backtracking into a path 
        # currently being explored (a cycle) and re-visiting a safe path already explored.
        states = [0] * numCourses

        # Define the DFS recursive function
        def has_cycle(current_course):
            # Base case: We found a course currently in the visiting path -> CYCLE detected
            if states[current_course] == 1:
                return True
            
            # Base case: We found a course that was already explored and is safe
            if states[current_course] == 2:
                return False

            # Pre-order: Mark the course as currently 'visiting'
            states[current_course] = 1

            # Visit all depending courses (neighbors)
            for neighbor in graph[current_course]:
                if has_cycle(neighbor):
                    return True

            # Post-order: Mark the course as 'visited' (safe) after all its paths are explored
            states[current_course] = 2
            return False

        # 3. Apply DFS starting from each course to handle non-connected graphs
        for i in range(numCourses):
            if has_cycle(i):
                return False

        return True

            
            