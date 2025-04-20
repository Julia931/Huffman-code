# Huffman-code
COMP 2119 Assignment 3

Execution method:
  1. Dowload the file "hmencoder.py"
  2. Use Terminal by entering "python3 hmencoder.py [input_filename]"
     eg. if the input file called input.txt, then in the terminal, we just need to enter "python hmencoder.py input.txt"
  3、Then the output files "code.txt" and "encodemsg.txt" are generated

Description of the code:
1. Module usage: we use "heapq" to create a priority queue and use "sys" to input command-line arguments
2. Structure: we use class Wrapper to build the structure of the tree
3. Functions：
     3.1 huffman_tree(data)：
         This function is used to convert the input data into tree in huffman structure by firstly counting the frequency of each character, put them into heap and dynamically merging the two least frequent nodes.
     3.2 generating_codes(node, prefix="", codelist={},freqlist={}):
         This function generates the huffman codes by traversing the huffman tree structure and generating the code in recursion.
     3.3 encode(data):
         Utilize the output of previous two functions to completely transfer the data into encoded data in a line.
     3.4 The following codes:
         Read the data of the input file
         Output two required files by utilizing the output of previous functions
