Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
for i in range(0,10):
    print(i)
;
SyntaxError: invalid syntax
for i in range(0,10):
    print(1)

    
1
1
1
1
1
1
1
1
1
1
for i in range(0,10):
    print(i)

    
0
1
2
3
4
5
6
7
8
9
>>> for i in range(all):
...     print(i)
... 
...     
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    for i in range(all):
TypeError: 'builtin_function_or_method' object cannot be interpreted as an integer
>>> for i in range(0,10):
...     print(all)
... 
...     
<built-in function all>
<built-in function all>
<built-in function all>
<built-in function all>
<built-in function all>
<built-in function all>
<built-in function all>
<built-in function all>
<built-in function all>
<built-in function all>
>>> for i in range(10):
...     print(i)
... 
...     
0
1
2
3
4
5
6
7
8
9
>>> for i in range(1,4,10):
...     print(i)
... 
...     
1
>>> 
