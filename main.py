import collections
import datetime
import time
from array import array
import re

##regular expressions
pattern = re.compile(r"([a-zA-Z0-9][a-zA-Z0-9-_.]+@[a-zA-Z]{1}[a-zA-Z.-_]+\.[a-z])")
string = 'ol.ga123@some.site123.com aa12.44@gmail.coma1.com'
match = pattern.findall(string)
print(match)
g = pattern.search(string);
print(g.groups(1))

