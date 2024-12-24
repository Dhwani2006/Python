Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d={'a':[10,20,30,(40,50,60)],'b':['c','d','e']}
>>> d
{'a': [10, 20, 30, (40, 50, 60)], 'b': ['c', 'd', 'e']}
>>> d[a][3][2]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    d[a][3][2]
NameError: name 'a' is not defined
>>> d={'k1':10,'k2':20}
>>> type(d[k1])
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    type(d[k1])
NameError: name 'k1' is not defined
>>> type('k1')
<class 'str'>
>>> type(d1['k1'])
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    type(d1['k1'])
NameError: name 'd1' is not defined. Did you mean: 'd'?
>>> type(d['k1'])
<class 'int'>
>>> my_dict = {"apple": 10, "banana": 20, "cherry": 30}
... keys_list = list(my_dict.keys())
... print(keys_list)
SyntaxError: multiple statements found while compiling a single statement
>>> my_dict = {"apple": 10, "banana": 20, "cherry": 30}
>>> keys_list = list(my_dict.keys())
>>> print(keys_list)
['apple', 'banana', 'cherry']
>>> a='parul'
>>> s=a[0].upper()+a[1:]
>>> print(s)
Parul
>>> 'a'+'b'
'ab'
>>> 'a'+str(2)
'a2'
>>> 'abc'*3
'abcabcabc'
>>> 'abc'*'abc'
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    'abc'*'abc'
TypeError: can't multiply sequence by non-int of type 'str'
