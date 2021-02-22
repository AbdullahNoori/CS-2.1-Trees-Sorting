#!python3

from prefixtreenode import PrefixTreeNode


class PrefixTree:
    """PrefixTree: A multi-way prefix tree that stores strings with efficient
    methods to insert a string into the tree, check if it contains a matching
    string, and retrieve all strings that start with a given prefix string.
    Time complexity of these methods depends only on the number of strings
    retrieved and their maximum length (size and height of subtree searched),
    but is independent of the number of strings stored in the prefix tree, as
    its height depends only on the length of the longest string stored in it.
    This makes a prefix tree effective for spell-checking and autocompletion.
    Each string is stored as a sequence of characters along a path from the
    tree's root node to a terminal node that marks the end of the string."""

    # Constant for the start character stored in the prefix tree's root node
    START_CHARACTER = ''

    def __init__(self, strings=None):
        """Initialize this prefix tree and insert the given strings, if any."""
        # Create a new root node with the start character
        self.root = PrefixTreeNode(PrefixTree.START_CHARACTER)
        # Count the number of strings inserted into the tree
        self.size = 0
        # Insert each string, if any were given
        if strings is not None:
            for string in strings:
                self.insert(string)

    def __repr__(self):
        """Return a string representation of this prefix tree."""
        return f'PrefixTree({self.strings()!r})'

    def is_empty(self):
        """Return True if this prefix tree is empty (contains no strings)."""
        # TODO

    def contains(self, string):
        """Return True if this prefix tree contains the given string."""
        # TODO

    def insert(self, string):
        """Insert the given string into this prefix tree."""
        # TODO

    def _find_node(self, string):
        """Return a pair containing the deepest node in this prefix tree that
        matches the longest prefix of the given string and the node's depth.
        The depth returned is equal to the number of prefix characters matched.
        Search is done iteratively with a loop starting from the root node."""
        # Match the empty string
        if len(string) == 0:
            return self.root, 0
        # Start with the root node
        node = self.root
        # TODO
# start at the root 
# search for the first letter of the prefix in root's       children
#  if the letter is not there
# return False 
# if it is there, look for the next letter 
# so basically, the first letter node and checks its children
# repeat until whole prefix is found or False

# below does a reference check
current = self.root
# testing below to see if reference check is working
for letter in prefix:
  print(letter)



  def insert(self, word):
    '''This method will add a new word to the prefix tree input = "dog"'''
  
# start with the root
# check children of root and if the first letter of the word is not there 
# add a new node with letter
# else do nothing
# repeat, get the node corresponding to the letter 
# check its children for the next letter 

    current = self.root
    for letter in word:
    flag = 0 
    # check if letter in children
    # TODO: comparing string to node won't work line below!! 
    # if letter in current.children:
        # print() 
    for child in current.children:
        if child.letter == letter:
        # already there
        current = child
          flag  = 1
    # I exit this loop without having to found a child with the letter 
    # then add it
    if   flag  != 1:
    childnode = PrefixTreeNode
    (letter)
    current.children.append
    (childnode)
    current = childnode
    (PrefixTreeNode(letter))



    def complete(self, prefix):
        """Return a list of all strings stored in this prefix tree that start
        with the given prefix string."""
        # Create a list of completions in prefix tree
        completions = []
        # TODO

    def strings(self):
        """Return a list of all strings stored in this prefix tree."""
        # Create a list of all strings in prefix tree
        all_strings = []
        # TODO

    def _traverse(self, node, prefix, visit):
        """Traverse this prefix tree with recursive depth-first traversal.
        Start at the given node with the given prefix representing its path in
        this prefix tree and visit each node with the given visit function."""
        # TODO


def create_prefix_tree(strings):
    print(f'strings: {strings}')

    tree = PrefixTree()
    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')
    print(f'strings: {tree.strings()}')

    print('\nInserting strings:')
    for string in strings:
        tree.insert(string)
        print(f'insert({string!r}), size: {tree.size}')

    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')

    print('\nSearching for strings in tree:')
    for string in sorted(set(strings)):
        result = tree.contains(string)
        print(f'contains({string!r}): {result}')

    print('\nSearching for strings not in tree:')
    prefixes = sorted(set(string[:len(string)//2] for string in strings))
    for prefix in prefixes:
        if len(prefix) == 0 or prefix in strings:
            continue
        result = tree.contains(prefix)
        print(f'contains({prefix!r}): {result}')

    print('\nCompleting prefixes in tree:')
    for prefix in prefixes:
        completions = tree.complete(prefix)
        print(f'complete({prefix!r}): {completions}')

    print('\nRetrieving all strings:')
    retrieved_strings = tree.strings()
    print(f'strings: {retrieved_strings}')
    matches = set(retrieved_strings) == set(strings)
    print(f'matches? {matches}')


def main():
    # Simpe test case of string with partial substring overlaps
    strings = ['ABC', 'ABD', 'A', 'XYZ']
    create_prefix_tree(strings)

    # Create a dictionary of tongue-twisters with similar words to test with
    tongue_twisters = {
        'Seashells': 'Shelly sells seashells by the sea shore'.split(),
        # 'Peppers': 'Peter Piper picked a peck of pickled peppers'.split(),
        # 'Woodchuck': ('How much wood would a wood chuck chuck'
        #                ' if a wood chuck could chuck wood').split()
    }
    # Create a prefix tree with the similar words in each tongue-twister
    for name, strings in tongue_twisters.items():
        print(f'{name} tongue-twister:')
        create_prefix_tree(strings)
        if len(tongue_twisters) > 1:
            print('\n' + '='*80 + '\n')


if __name__ == '__main__':
    main()
class PrefixTreeNode:
    
  def __init__(self, letter):

    # Character string
    self.letter = letter

    #References to other child nodes
    self.children = []

    #Is the node the end of a word or not?
    self.terminal = False

class PrefixTree:

  def __init__(self):

    self.root = PrefixTreeNode("")

  def search(self, prefix):
    '''This method will return true if a given prefix is present false if not
    input = "Ca"
    output = True'''
    #Start at the root
    #Search for first letter of the prefix in root's children
    #If the letter is not there then return False
    #if it is there, then look for next letter
    #(Go to that first letter node and check its children and
    # repeat until whole prefix is found/true or false.
    current = self.root

    for letter in prefix:
      found_it = 0

      for child in current.children:
        if child.letter == letter:
          #Find letter and check child's children
          current = child
          found_it = 1
          break

      if found_it == 0:
        return False

    return True

  def insert(self, word):
    '''This method will add a new word to the prefix tree
    input = "dog" 
    '''
    #Start with the root
    #Check children of root
    # Check if first letter of word is not there
    #Add a new node with letter
    #Else, do nothing
    #Repeat,
    # Get the node corresponding to the letter
    #Check it's children 
    current = self.root
    for letter in word:
      already_there_flag = 0

      #check if letter in children
      for child in current.children:
        if child.letter == letter:
          #already there
          current = child
          already_there_flag = 1
      #Exit this loop without having found a child with the letter, then add it
      if already_there_flag != 1:
        childnode = PrefixTreeNode(letter)
        current.children.append(childnode)
        current = childnode

    #When at the end, set terminal to True
    current.terminal = True

  def find_all_words(self, prefix):
    '''returns a list of valid words in the tree starting with the given Prefix
    input "cat"
    output ["category", "cat"] '''
    #TODO: Think about how to implement this
    print('Hello you over there')
    PrefixTree.search(self,prefix)
    print('made it ')
    pass

  def delete(self, word):
    '''This method will remove a word from the prefix tree
    input = "dog" '''
    input = 'dog'

    for word in PrefixTree:
      input = PrefixTree.get(word, None)
      if input is None:
        break
      
    else:
        del input[_end]