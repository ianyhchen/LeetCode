class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # start_index: potential starting station
        # total_surplus: total balance of (gas - cost) for the entire trip
        # current_tank: balance from the current start_index to station i
        start_index, total_surplus, current_tank = 0, 0, 0
        
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_surplus += diff
            current_tank += diff

            # If current_tank drops below 0, it means all stations from 
            # current start_index to i cannot be the starting point.
            if current_tank < 0:
                # Greedy choice: try the next station as the new start
                start_index = i + 1
                # Reset the current tank for the new starting point
                current_tank = 0
                
        # If the total gas is less than the total cost, no solution exists.
        # Otherwise, the last updated start_index is guaranteed to be the solution.
        return start_index if  total_surplus >= 0 else -1

