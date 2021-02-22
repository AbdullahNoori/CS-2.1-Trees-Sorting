from PrefixTree import PrefixTreeNode
from PrefixTree import PrefixTree

node = PrefixTreeNode("A")
pretree = PrefixTree()

pretree.insert("cat")
pretree.insert("can")
pretree.insert("category")
pretree.insert("dog")

print(pretree.search("can"))
print(pretree.find_all_words("ca"))  
