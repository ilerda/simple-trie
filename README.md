# simple-trie
Simple Trie implementation

## Description
This simple Trie datastructure implements 4 basic methods to maintain a dictionary of words:

- insert(word)
- has_prefix(prefix)
- has_word(word)
- delete(word)

The time complexity for all operations is O(n) where n is the length of the word.
The space complexity is O(1) for all operations apart from insert, which can be O(n) for new nodes.

A Trie can be useful for implementing a predictive text or autocomplete dictionary.

Each character is represented as a key in a dictionary in a node which points to the next possible
characters. This is a visual representation of a Trie which contains the four words "foo", "bar",
"foolish" and "foam":

```
rootNode
|
| -> b -> a -> r* ('*' means isWord=true)
|
| -> f -> o -> o*
          |    |
          |    | -> l -> i -> s -> h*
          |
          | -> a -> m*
```

## Setup and Explanation
There are no extra requirements for this library, apart from Python 3.

Inside a python prompt at the root directory of the repo, the following commands can be run to initialise
a Trie:

```
>>> from trie import Trie
>>> new_trie = Trie()
```

These commands will add nodes for all the characters in the two new words that are added.

```
>>> new_trie.insert("foo")
>>> new_trie.insert("bar")
```

This command will only add nodes for 'l', 'i', 's' and 'h' since the 'foo' prefix has already been added.
This prefix is also marked as a word.

```
>>> new_trie.insert("foolish")
>>> new_trie.has_prefix("foo") # True
>>> new_trie.has_word("foo") # True
```

If the word 'foo' gets deleted, only the marker for isWord gets removed from the second 'o' node, since
it is still a prefix for the word 'foolish'. If subsequently 'foolish' also gets deleted, all its nodes
will need to be removed.

```
>>> new_trie.delete("foo")
>>> new_trie.delete("foolish")
>>> new_trie.has_prefix("foo") # False
>>> new_trie.has_word("foo") # False
```

## Testing
The file test-trie.py can be run which goes through some tests scenarios for the Trie implementation:

```
$ python test-trie.py
```
