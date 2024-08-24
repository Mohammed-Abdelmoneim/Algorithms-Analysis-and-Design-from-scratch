import heapq

class HeapNode:

  def __init__(self, data, freq):
    self.data = data
    self.freq = freq
    self.left = None
    self.right = None

  def __lt__(self, other):
    return self.freq < other.freq


class Huffman:

  def __init__(self, message):
    self.internal_char = chr(0)
    self.codes = {}
    freqHash = {}

    # Calculate frequency of each character in the message
    for char in message:
      if char in freqHash:
        freqHash[char] += 1
      else:
        freqHash[char] = 1

    # Create a heap node for each character and add it to min heap
    self.minHeap = []
    for char, freq in freqHash.items():
      newNode = HeapNode(char, freq)
      heapq.heappush(self.minHeap, (newNode.freq, newNode))

    # Construct Huffman tree by repeatedly extracting nodes from min heap
    while len(self.minHeap) > 1:
      left_freq, left_node = heapq.heappop(self.minHeap)
      right_freq, right_node = heapq.heappop(self.minHeap)
      newFreq = left_freq + right_freq
      top = HeapNode(self.internal_char, newFreq)
      top.left = left_node
      top.right = right_node
      heapq.heappush(self.minHeap, (newFreq, top))

    # Generate Huffman code for each character
    self.generateCodes(self.minHeap[0][1], "")

  def generateCodes(self, node, code):
    if node is None:
      return
    if node.data != self.internal_char:
      self.codes[node.data] = code
    self.generateCodes(node.left, code + "0")
    self.generateCodes(node.right, code + "1")

# Test the code
msg = "The output from Huffman's algorithm can be viewed as a variable length code table for encoding a source symbol. The algorithm derives this table from the estimated probability or frequency of occurrence for each possible value of the source symbol. as in other entropy encoding methods, more common symbols are generally represented using fewer bits than less common symbols. Huffman's method can be efficiently implemented, finding a code in time linear to the number of input weights if these weights are sorted. However, although optimal among methods encoding symbols separately, Huffman coding is not always optimal among all compression methods it is replaced with arithmetic coding or asymmetric numeral systems if better compression ratio is required."
huff = Huffman(msg)

for k in huff.codes.keys():
  print(k, huff.codes[k])
