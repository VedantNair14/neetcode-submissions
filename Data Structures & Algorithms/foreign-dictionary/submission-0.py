from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Step 1: Initialize adjacency list for all unique characters
        adj = {c: set() for w in words for c in w}

        # Step 2: Compare adjacent words to build directed edges
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            # Invalid prefix case: e.g., "apple" appears before "app"
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            # Find the first character that differs
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])  # w1[j] must come before w2[j]
                    break  # Only the first difference defines relative order

        # Step 3: Topological sort with 3-state cycle detection
        # visited dictionary states:
        #   visited[c] == True  -> Fully processed and added to res
        #   visited[c] == False -> Currently in the active recursion stack (cycle!)
        visited = {}
        res = []

        def dfs(char: str) -> bool:
            if char in visited:
                # If True: already processed safely. If False: cycle detected!
                return visited[char]

            # Mark as currently visiting (active in recursion stack)
            visited[char] = False

            # Visit all characters that must come after this character
            for neighbor in adj[char]:
                if not dfs(neighbor):
                    return False

            # Mark as completely processed
            visited[char] = True
            # Post-order: append character after all its dependencies are visited
            res.append(char)
            return True

        # Run DFS for every unique character
        for char in list(adj.keys()):
            if not dfs(char):
                return ""

        # Step 4: Reverse post-order result to get correct increasing order
        res.reverse()
        return "".join(res)