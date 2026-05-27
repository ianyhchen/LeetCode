import random
class RandomizedSet:

    def __init__(self):
        # Map to store val -> index in the list
        self.value_index_map = {}
        # List to store the actual values for O(1) random access
        self.value_list = []


    def insert(self, val: int) -> bool:
        if val not in self.value_index_map:
            # Add the new value to the end of the list
            self.value_list.append(val)
            # Record the index of the newly added value
            self.value_index_map[val] = len(self.value_list) - 1            
            return True
        else:
            # If val already exists, return False
            return False

    def remove(self, val: int) -> bool:
        if val in self.value_index_map:
            # Get the index of the element to be removed
            idx = self.value_index_map[val]
            # Get the last element in the list
            last_val =  self.value_list[-1]

            # Move the last element to the position of the element to be deleted
            self.value_list[idx] = last_val
            # Update the index of the moved element in the map
            self.value_index_map[last_val] = idx

            # Remove the last element from the list (O(1))
            del self.value_list[-1]
            # Remove the target value from the map (O(1))
            del self.value_index_map[val]
            
            return True
        else:
            # If val does not exist, return False
            return False
        

    def getRandom(self) -> int:
        rand_int = random.randint(0, len(self.value_list) - 1)        
        return self.value_list[rand_int]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()