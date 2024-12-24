Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
float(15)
15.0
float(20+3j)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    float(20+3j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
float("23458")
23458.0
complex(123)
(123+0j)
complex(asd,ergh)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    complex(asd,ergh)
NameError: name 'asd' is not defined
complex(f,j)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    complex(f,j)
NameError: name 'f' is not defined
complex('a',2)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    complex('a',2)
TypeError: complex() can't take second arg if first is a string
complex('dfhj')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    complex('dfhj')
ValueError: complex() arg is a malformed string
complex('3')
(3+0j)
complex(3)
(3+0j)
complex('True','False')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    complex('True','False')
TypeError: complex() can't take second arg if first is a string
complex(True,False)
(1+0j)
bool(1)
True
bool(10.4)
True
bool(0.45)
True
bool('werr')
True
bool(' ')
True
bool('')
False
bool()
False
bool('234ert')
True
bool(345rty)
SyntaxError: invalid decimal literal
bool(356)
True
bool()
False
str(rgh)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    str(rgh)
NameError: name 'rgh' is not defined
str('w456467')
'w456467'
str('234')
'234'
str('3t54t5y6')
'3t54t5y6'
str('')
''
str()
''
str("")
''
str(NULL)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    str(NULL)
NameError: name 'NULL' is not defined
str("NULL")
'NULL'
str'null'
SyntaxError: invalid syntax
str('null')
'null'
str(null)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    str(null)
NameError: name 'null' is not defined
str($$)
SyntaxError: invalid syntax
str('%^&')
'%^&'
a='s5477'
len(a)
5
len(as)
SyntaxError: invalid syntax
len(sadf)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    len(sadf)
NameError: name 'sadf' is not defined
len('ew4tr')
5
len(244)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    len(244)
TypeError: object of type 'int' has no len()
len(a[2:])
3
len([])
0
len([tyu])
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    len([tyu])
NameError: name 'tyu' is not defined
len([345])
1
len([123456])
1
len(s[:])
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    len(s[:])
NameError: name 's' is not defined
len(a[&])
SyntaxError: invalid syntax
len(a[2:])
3
len(s[3:])
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    len(s[3:])
NameError: name 's' is not defined
len(a[3:])
2
len(a[4:])
1
len(a[5:])
0
b=dhwanikhapre
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    b=dhwanikhapre
NameError: name 'dhwanikhapre' is not defined
>>> b='dhwani khapre'
>>> len(a)
5
>>> len(b)
13
>>> len(b[1:})
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> len(b[1:])
12
>>> a(len(b))
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a(len(b))
TypeError: 'str' object is not callable
>>> len(b)
13
>>> b
'dhwani khapre'
>>> a(b)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    a(b)
TypeError: 'str' object is not callable
>>> lower("BOOK")
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    lower("BOOK")
NameError: name 'lower' is not defined
>>> Lower('BOOK')
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    Lower('BOOK')
NameError: name 'Lower' is not defined
>>> a='BOOK'
>>> a.lower
<built-in method lower of str object at 0x000001BD1E2F2A90>
>>> a.lower()
'book'
>>> a.upper
<built-in method upper of str object at 0x000001BD1E2F2A90>
>>> a.upper()
'BOOK'
>>> a.strip()
'BOOK'
>>> a.isdigit()
False
>>> a.isalpha()
True
