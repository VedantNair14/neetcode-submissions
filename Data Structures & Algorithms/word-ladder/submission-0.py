from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Edge Case: If endWord is not in wordList, transformation is impossible
        if endWord not in wordList:
            return 0

        # Step 1: Precompute wildcard pattern adjacency list
        nei = defaultdict(list)
        wordList.append(beginWord)
        L = len(beginWord)

        for word in wordList:
            for j in range(L):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)

        # Step 2: Standard BFS queue
        q = deque([beginWord])
        visited = set([beginWord])
        res = 1  # Counting the number of words in the sequence

        while q:
            # Process current level (step by step)
            for _ in range(len(q)):
                word = q.popleft()

                # If reached target, return current sequence length
                if word == endWord:
                    return res

                # Look up all neighboring words via each pattern
                for j in range(L):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neighborWord in nei[pattern]:
                        if neighborWord not in visited:
                            visited.add(neighborWord)
                            q.append(neighborWord)

            res += 1

        return 0