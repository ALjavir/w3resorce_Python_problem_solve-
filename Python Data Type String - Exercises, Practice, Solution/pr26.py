import textwrap
a = '''  Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.
  '''
b = textwrap.fill(a, width= 50)  
print(b)