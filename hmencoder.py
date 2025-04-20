import heapq
import sys

# Huffman Encoder Node structure
class Wrapper:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

# This function builds the Huffman tree from the input data
def huffman_tree(data):
    # Count frequency of each character
    frequency = []
    for char in data:
        if frequency == []: # if the list is empty, add the first character
            frequency.append([1,char])
        else: # if the list is not empty, check if the character is already in the list
            Flag = False
            for j in range(len(frequency)):
                if frequency[j][1] == char:
                    frequency[j][0] += 1
                    Flag = True
            if Flag == False:
                frequency.append([1,char])

    # Create a priority queue (min-heap)
    heap = [ Wrapper(frequency[i][0],frequency[i][1]) for i in range(len(frequency))]
    heapq.heapify(heap) # turns the list into a min-heap

    # Build the Huffman tree by dynamically merging the two least frequent nodes
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merge_node = Wrapper(left.freq + right.freq, None)
        merge_node.left = left
        merge_node.right = right
        heapq.heappush(heap, merge_node)
        heapq.heapify(heap)
    return heap[0] # The root of the Huffman tree
    
# Generate the Huffman codes for each character
def generating_codes(node, prefix="", codelist={},freqlist={}):
    if node.data != None: # check if the node is a leaf
        codelist[node.data]=prefix
        freqlist[node.data]=node.freq
    else:
        generating_codes(node.left, prefix + '0', codelist)
        generating_codes(node.right, prefix + '1', codelist)
    return codelist,freqlist

# Encode the data using the generated Huffman codes
def encode(data):
    # Create the Huffman tree
    final_tree = huffman_tree(data)
    
    # Generate Huffman codes
    codelist, freqlist = generating_codes(final_tree)
    
    # Encode the data
    encoded_data = ""
    for char in data:
        encoded_data += codelist[char]
    
    return encoded_data, codelist, freqlist

# Main function: utilize the above functions to output the expected files

# Read the input file
if len(sys.argv) != 2:
    print("Usage: hmencoder [input_file]")
    exit()
filename = sys.argv[1] #input file name

# Check if the file exists and open the file
try:
    fin = open(filename, 'r')
except:
    print("File not found")
    exit()
data = fin.read()
fin.close()
# Check if the file is empty
if not data:
    print("File is empty")
    exit()
else:
    encoded_data, codelist, freqlist = encode(data) # call the function: encode the data and generate the codes

# Output the encoded data to "encodemsg.txt" file
fout = open("encodemsg.txt", 'w')
for i in range(0,len(encoded_data),80):
    fout.write(encoded_data[i:i+80] + "\n")
fout.close()

# Output the Huffman code instructiosn to "code.txt" file
fout = open("code.txt", 'w')
total_bit = 0
total_count = 0
for key in sorted(codelist):
    if key == '\n':
        fout.write("\\n: " + codelist[key] + "\n")
    elif key == ' ':
        fout.write("Space: " + codelist[key] + "\n")
    else:
        fout.write(key + ": " + codelist[key] + "\n")
    total_bit += len(codelist[key])*freqlist[key]
    total_count += freqlist[key]
aver_bit = round(total_bit / total_count,2)
fout.write("Ave = " + str(aver_bit) + " bits per symbol" + "\n")
fout.close()