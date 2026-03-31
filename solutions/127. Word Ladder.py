# 單向BFS
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Use a set for O(1) lookups
        word_set = set(wordList)

        # Edge case: if endWord is not reachable
        if endWord not in word_set:
            return 0

        # Initialize BFS queue: (current_word, level)
        queue = deque([(beginWord, 1)])
        
        #Optimization: remove beginWord from set to prevent going back
        if beginWord in word_set:
            word_set.remove(beginWord)


        while queue:
            curr_word, count = queue.popleft()

            # Try changing each character of the current word
            for i in range(len(curr_word)):
                original_char = curr_word[i]
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == original_char:
                        continue

                    # Construct new candidate word
                    next_word = curr_word[:i] + c + curr_word[i + 1:]

                    if next_word in word_set:
                        # Found the destination!
                        if next_word == endWord:
                            return count + 1
                        
                        # Add to queue and mark as visited by removing from set
                        queue.append((next_word, count + 1))
                        word_set.remove(next_word)
        # If no path is found after exhausting the queue
        return  0    



# 雙向 BFS
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Use a set for O(1) lookups
        word_set = set(wordList)

        # Edge case: if endWord is not reachable
        if endWord not in word_set:
            return 0

        # Two boundary sets
        begin_set = {beginWord}
        end_set = {endWord}
        level = 1

        while begin_set and end_set:
            # 重點：總是從較小的邊界開始擴散，這能極大地減少計算量
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set

            next_level_set = set()

            # Key move: Mark current level nodes as visited BEFORE exploring neighbors
            # so they can't be reused, but can still be found by the "other" set.
            for word in begin_set:
                if word in word_set:
                    word_set.remove(word)

            
            for word in begin_set:                
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == word[i]:
                            continue
                        
                        next_word = word[:i] + c + word[i + 1:]

                        # Intersection check: the two frontiers meet
                        if next_word in end_set:
                            return level + 1

                        if next_word in word_set:                            
                            next_level_set.add(next_word)
                            
            begin_set = next_level_set
            level += 1
                
        return 0
