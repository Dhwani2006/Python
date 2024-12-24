Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=[1,2,3]
b=[3,2,1]
a+b
[1, 2, 3, 3, 2, 1]
remove(3)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    remove(3)
NameError: name 'remove' is not defined
a.remove(3)
a
[1, 2]
b
[3, 2, 1]
b.remove(3)
b
[2, 1]
a+b
[1, 2, 2, 1]
a.b.remove(2)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.b.remove(2)
AttributeError: 'list' object has no attribute 'b'
a.remove(b)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.remove(b)
ValueError: list.remove(x): x not in list
a=(1,2,3)
a
(1, 2, 3)
b=(1,2,3)
b
(1, 2, 3)
a+b
(1, 2, 3, 1, 2, 3)
a={1,2,3,3}
a
{1, 2, 3}
b={1,2,3,4,4,4,5,5,2,3,1}
b
{1, 2, 3, 4, 5}
>>> b={5,1,3,3,10}
>>> b
{1, 10, 3, 5}
>>> a+b
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a+b
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> a={1,7,7,10,0}
>>> b={1,1,7,10,10,0,0}
>>> a+b
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a+b
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> a.remove(10)
>>> a
{0, 1, 7}
>>> a.add(10)
>>> a
{0, 1, 10, 7}
>>> thisdict ={
...   "brand": "Ford",
...   "model": "Mustang",
...   "year": 1964
... }
>>> thisdict
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>> thisdict.remove(year)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    thisdict.remove(year)
AttributeError: 'dict' object has no attribute 'remove'
>>> thisdict.remove(1964)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    thisdict.remove(1964)
AttributeError: 'dict' object has no attribute 'remove'
>>> thisdict.remove('year')
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    thisdict.remove('year')
AttributeError: 'dict' object has no attribute 'remove'
>>> thisdict.remove('1964')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    thisdict.remove('1964')
AttributeError: 'dict' object has no attribute 'remove'
Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
t=(10)
print(t)
10
t
10
t=(11,12,11,12,14,16_
   
SyntaxError: invalid decimal literal
t
   
10
t=(12,11,13,11,18)
   
t
   
(12, 11, 13, 11, 18)
)
SyntaxError: unmatched ')'
t
(12, 11, 13, 11, 18)
t.remove(11)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    t.remove(11)
AttributeError: 'tuple' object has no attribute 'remove'
t.remove
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    t.remove
AttributeError: 'tuple' object has no attribute 'remove'
t.remove(11)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    t.remove(11)
AttributeError: 'tuple' object has no attribute 'remove'
t.add(15)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    t.add(15)
AttributeError: 'tuple' object has no attribute 'add'
t=(10)
t
10
t=(10,)
t
(10,)
remove(19_
       
SyntaxError: invalid decimal literal
)
SyntaxError: unmatched ')'
remove(11)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    remove(11)
NameError: name 'remove' is not defined
t.remove(11)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    t.remove(11)
AttributeError: 'tuple' object has no attribute 'remove'
d={'a':[10,20,30,(40,50,60)],'b':['c','d','e']}
d
{'a': [10, 20, 30, (40, 50, 60)], 'b': ['c', 'd', 'e']}
print(60)
