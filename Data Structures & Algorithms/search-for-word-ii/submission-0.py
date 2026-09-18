class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Stores the full word when a word ends here


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # Step 1: Build the Trie from the word list
        root = TrieNode()
        for w in words:
            curr = root
            for char in w:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = w  # Mark the end of this word

        ROWS, COLS = len(board), len(board[0])
        res = []

        # Step 2: DFS Backtracking on the grid guided by the Trie
        def dfs(r: int, c: int, parent_node: TrieNode):
            char = board[r][c]
            curr_node = parent_node.children[char]

            # If we reached a word, record it
            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None  # Prevent duplicate additions

            # Mark cell as visited
            board[r][c] = "#"

            # Explore 4 neighbors: Up, Down, Left, Right
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 
                    0 <= nc < COLS and 
                    board[nr][nc] in curr_node.children):
                    dfs(nr, nc, curr_node)

            # Backtrack: Restore the cell
            board[r][c] = char

            # Optimization (Trie Pruning): Remove leaf nodes to speed up subsequent searches
            if not curr_node.children:
                del parent_node.children[char]

        # Step 3: Trigger DFS from any cell matching a root Trie branch
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return res