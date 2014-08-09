lexical_uuid
============

A Lexical UUID type for Python

### Usage

It's a very basic library and has many of the same functions as Python's built-in UUID library.

#### Constructing

```python
from lexical_uuid import LexicalUUID

l = LexicalUUID() # create one from current UTC timestamp

from datetime import datetime
l = LexicalUUID(datetime.now()) # create one from current local timestamp

l = LexicalUUID(25965632506355266687123197517829786L) # create from an int

l = LexicalUUID('\x00\x05\x004[\x99\xef\n\xae\xd7S\x028\xc3\x16\x9a') # create from bytes

l = LexicalUUID('00050034-5b99-ef0a-aed7-530238c3169a') # create from GUID representation
```

#### Working With It

```python
from lexical_uuid import LexicalUUID

l = LexicalUUID()

# get integer
l.int
# => 25965632506355266687123197517829786L

# get GUID represnetation
l.guid
# => '00050034-5b99-ef0a-aed7-530238c3169a'

# get bytes
l.bytes
# => '\x00\x05\x004[\x99\xef\n\xae\xd7S\x028\xc3\x16\x9a'

# get byte tuple
l.byte_tuple
# => (0, 5, 0, 52, 91, 153, 239, 10, 174, 215, 83, 2, 56, 195, 22, 154)

# get the node id assigned to whatever machine generated it
l.node
# => 12598629751599601306L

# get timestamp
l.timestamp
# => 1407599758667530

# get a URL-safe minified version
l.encode()
# => 'BQA0W5nvCq7XUwI4wxaa'

# construct from URL-safe minified version
l2 = LexicalUUID.decode('BQA0W5nvCq7XUwI4wxaa')

# you can sort them
l3 = LexicalUUID()
sorted([l3, l2])

# you can compare them
assert l == l2
assert l < l3
assert l3 > l

# they can be used as keys in dictionaries (they are hashable)
d = {l: (l2, l3)}
```

### Credits

An adaptation of https://github.com/jamesgolick/lexical_uuid for pythons. Borrowing code from https://github.com/jakedouglas/fnv-ruby And http://hg.python.org/cpython/file/90eda29a8e03/Lib/uuid.py
