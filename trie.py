from node import Node

class Trie(object):

   def __init__(self):
      self.root = Node()

   def insert(self, word):
      current = self.root
      for i in range(len(word)):
         if not current.contains(word[i]):
            current.add_node(word[i])
         current = current.get_node(word[i])
      current.set_is_word(True)

   def has_prefix(self, prefix):
      current = self.root
      for i in range(len(prefix)):
         if not current.contains(prefix[i]):
            return False
         current = current.get_node(prefix[i])
      return True

   def has_word(self, word):
      current = self.root
      for i in range(len(word)):
         if not current.contains(word[i]):
            return False
         current = current.get_node(word[i])
      return current.is_word()

   def delete(self, word):
      if word is None or len(word) == 0:
         return

      last_node = self._get_last_node(word)
      if last_node is None or not last_node.is_word():
         return

      last_node.set_is_word(False)

      if len(last_node.get_map()) > 0:
         return

      self._remove_last_node_with_multiple_children(word)

   def _get_last_node(self, word):
      current = self.root
      for i in range(len(word)):
         if not current.contains(word[i]):
            return None
         current = current.get_node(word[i])
      return current

   def _remove_last_node_with_multiple_children(self, word):
      last_node_with_multiple_children = None
      child_to_break = 0
      current = self.root

      for i in range(len(word)-1):
         if not current.contains(word[i]):
            return
         current = current.get_node(word[i])

         if len(current.get_map()) > 1 or current.is_word():
            last_node_with_multiple_children = current
            child_to_break = word[i+1]
      if last_node_with_multiple_children is not None:
         last_node_with_multiple_children.get_map().pop(child_to_break)
      else:
         self.root.get_map().pop(word[0])
