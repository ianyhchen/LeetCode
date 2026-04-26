from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use defaultdict to avoid checking if a key exists
        sorted_strs = defaultdict(list)
        
        for s in strs:
            # Sort the string to create a unique key for anagrams
            # sorted() returns a list, so we join it back to a string
            sorted_key = ''.join(sorted(s))

            # Append the original string to the corresponding list            
            sorted_strs[sorted_key].append(s)        

        # Directly return the values of the dictionary as a list of lists
        return list(sorted_strs.values())

