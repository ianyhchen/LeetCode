from collections import defaultdict
class Solution:
    def sortVowels(self, s: str) -> str:
        freq_map, first_pos_map = defaultdict(int), {}
        vowels = set('aeiou')
        vowels_to_sort, vowel_indices = [], []
        for i in range(len(s)):
            char = s[i]
            if char in vowels:                
                freq_map[char] += 1
                if char not in first_pos_map:
                    first_pos_map[char] = i     

                vowels_to_sort.append(char)
                vowel_indices.append(i)

        sorted_vowels = sorted(vowels_to_sort, key = lambda x: (-freq_map[x], first_pos_map[x]))
        res_list = list(s)
        for i in range(len(vowel_indices)):
            res_list[vowel_indices[i]] = sorted_vowels[i]
        
        return ''.join(res_list)
