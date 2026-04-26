from collections import Counter
import heapq

class WordItem:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
    
    def __lt__(self, other):
        # Min-Heap logic: The one at the top should be the "least" important.
        if self.freq != other.freq:
            # Lower frequency is "smaller" (less important)
            return self.freq < other.freq

        # If frequencies are equal, the "larger" lexicographical word 
        # is "smaller" (less important) in our heap's logic.
        return self.word > other.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # 1. Count frequency
        counter = Counter(words)   

        # 2. Maintain a min-heap of size k
        heap = []
        for word, freq in counter.items():
            heapq.heappush(heap, WordItem(word, freq))

            if len(heap) > k:
                heapq.heappop(heap)

        # 3. Extract and reverse (since it's a min-heap)
        res = []
        while heap:
            res.append(heapq.heappop(heap).word)
        # Reverse to get high frequency -> low frequency
        return res[::-1]
