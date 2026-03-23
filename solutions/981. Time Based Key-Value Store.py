from collections import defaultdict
class TimeMap:

    def __init__(self):
        # Use a dictionary where the value is a list of [timestamp, value] pairs
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Since timestamps are strictly increasing, we can just append
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        value_list = self.store[key]
        
        # Early return if target timestamp is smaller than the earliest recorded
        if timestamp < value_list[0][0]:
            return "" 
        
        # Binary Search to find the largest timestamp <= given timestamp
        left, right = 0, len(value_list) - 1
        res = ""

        while left <= right:
            mid = left + (right - left)//2

            # If the current timestamp is exactly what we need or smaller
            if value_list[mid][0] <= timestamp:
                # This could be a potential answer, store it and look for a larger one
                res = value_list[mid][1]
                left = mid + 1
            else:
                # If current timestamp is too large, look to the left
                right = mid - 1
        
        return res


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)