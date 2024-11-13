import heapq

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ""
    
    # Define the less-than function to make Node objects comparable for the heap
    def __lt__(self, other):
        return self.freq < other.freq

def printNodes(node, val=""):
    # Assign binary code based on current traversal path
    newval = val + node.huff
    # If it's a leaf node, print the symbol and its code
    if not node.left and not node.right:
        print(f"{node.symbol} -> {newval}")
    # Recursive traversal for left and right child nodes
    if node.left:
        printNodes(node.left, newval)
    if node.right:
        printNodes(node.right, newval)

chars = ["a", "b", "c", "d", "e", "f"]
freqs = [50, 10, 3, 30, 2, 5]
nodes = []

# Creating a priority queue with initial nodes
for i in range(len(chars)):
    heapq.heappush(nodes, Node(freqs[i], chars[i]))

# Combine nodes to build the Huffman Tree
while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
    left.huff = "0"
    right.huff = "1"
    # Create a new internal node with combined frequency
    newnode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
    heapq.heappush(nodes, newnode)

# Print the Huffman codes starting from the root node
printNodes(nodes[0])

'''
output

a -> 0
d -> 10
b -> 110
f -> 1110
c -> 11110
e -> 11111
'''