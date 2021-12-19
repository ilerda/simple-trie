class Node(object):
   """
   Basic Node Class for Trie Implementation

   Keeps track of whether this node marks the end of a word. Also has a
   dict with characters that point to subsequent nodes.
   """

   def __init__(self):
      self.charMap = dict()
      self.isWord = False

   def is_word(self):
      return self.isWord

   def set_is_word(self, is_word):
      self.isWord = is_word

   def contains(self, c):
      return c in self.charMap

   def add_node(self, c):
      if c not in self.charMap:
         self.charMap[c] = Node()

   def get_node(self, c):
      return self.charMap.get(c)

   def get_map(self):
      return self.charMap
