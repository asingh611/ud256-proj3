# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        parent_node = self.root
        for character in word:
            parent_node.insert(character)
            parent_node = parent_node.children[character]

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        nodeToSearch = self.root
        for char in prefix:
            if char not in nodeToSearch.children:
                return None
            nodeToSearch = nodeToSearch.children[char]
        return nodeToSearch


# Represents a single node in the Trie
class TrieNode:
    def __init__(self, value=''):
        # Initialize this node in the Trie
        self.value = value
        self.children = {}
    
    def insert(self, char):
        # Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode(char)
        
    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for 
        # all complete words below this point
        all_suffixes = []
        if len(self.children) > 0:
            for child in self.children:
                all_suffixes += self.children[child].suffixes(suffix + child)
            return all_suffixes
        
        return [suffix]


# Populating sample data
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


# Function to return results from test data
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print(', '.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')


# Print outputs
f('')   # Expected result: ''
f('q')  # Expected result: "q not found"
f('a')  # Expected result: "ntagonist, ntonym, nthology"
f('ant')  # Expected result: "agonist, onym, hology"
f('anto')  # Expected result: "nym"
f('tri')  # Expected result: "gger, gonometry, e, pod"
f('trig')  # Expected result: "ger, onometry"
