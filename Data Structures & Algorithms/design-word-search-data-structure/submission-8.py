# trie

class Node:
    def __init__(self):
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.children["#"] = True

    def search(self, word: str) -> bool:
        def check(curr, word):
            n = len(word)
            
            if n == 0:
                return "#" in curr.children

            for i in range(n):
                c = word[i]

                if c not in curr.children and c != '.':
                    return False
                elif c == ".":
                    for c in curr.children:
                        if c == "#":
                            continue

                        if check(curr.children[c], word[i+1:]):
                            return True

                    return False
                else:
                    curr = curr.children[c]

            return "#" in curr.children

        curr = self.root
        return check(curr, word)
            