from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Build the adjacency list to represent the graph. 
        # Format: adjacency_map[from_node] = [(to_node, price)]
        adjacency_map = defaultdict(list)
        for flight in flights:
            f, t, p = flight
            adjacency_map[f].append((t, p))

        # Initialize a queue for BFS level-order traversal.
        # Store tuples of (current_node, current_accumulated_cost)
        queue = deque()
        queue.append((src, 0))

        # Array to track the minimum cost to reach each node.
        # Initialized to infinity. This is crucial for pruning expensive paths.
        min_cost = [float('inf')] * n
        min_cost[src] = 0

        # Variable to track the number of stops made so far
        stops = 0

        # Perform BFS: continue while there are nodes to process and stops are within limit
        while queue and stops <=k:
            size = len(queue)
            # Process all paths at the current level (i.e., same number of stops)            
            for _ in range(size):
                curr_node, curr_cost = queue.popleft()

                # Iterate through all reachable neighboring nodes
                for next_node, price in adjacency_map[curr_node]:                    
                    new_cost = curr_cost + price

                    # Pruning condition: 
                    # Add to queue if the new cost is cheaper than the previously recorded cost to reach 'next_node'
                    if new_cost < min_cost[next_node]:
                        queue.append((next_node, new_cost))
                        min_cost[next_node] = new_cost
            # Increment stops after finishing exploring the current level
            stops += 1
            
        # Return the final minimum cost to reach dst, or -1 if it remains infinity (unreachable)
        return -1 if min_cost[dst] == float('inf') else min_cost[dst]