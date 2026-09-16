class TrieNode:
    def __init__(self):
        # Maps a character to another TrieNode
        self.children = {}
        # True if a complete word terminates at this node
        self.is_end_of_word = False


class PrefixTree:

    def __init__(self):
        # The tree starts with an empty root node
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            # If the character path doesn't exist yet, create it
            if char not in curr.children:
                curr.children[char] = TrieNode()
            # Move to the child node
            curr = curr.children[char]
        # Mark the end of the word
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            # If any letter along the path is missing, the word was never inserted
            if char not in curr.children:
                return False
            curr = curr.children[char]
        # Return True only if this was marked as an actual complete word
        return curr.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            # If any letter along the prefix path is missing, return False
            if char not in curr.children:
                return False
            curr = curr.children[char]
        # If we successfully walked all characters of the prefix, return True
        return True