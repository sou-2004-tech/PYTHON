a="""Python is a powerful, high-level programming language known for its
simplicity and readability. It supports multiple programming paradigms,
including procedural, object-oriented, and functional programming. 
Python’s extensive standard library and vast ecosystem of third-party packages make
it ideal for a wide range of course applications—from web development and data analysis to
artificial intelligence and automation. Its clear syntax and strong community support
 make Python an excellent choice for both beginners and experienced developers."""

b=len(a)
print("The Length of String is:",b)
print("The First Character of string is: ",a[0])
print("The last character of the string is: ",a[-1])
print("Printing first 50 characters:\t",a[:51])
print(a.replace("Python","PYTHON"))
print(a.lower())
a.strip()
words=a.split()
f=len(words)
print("The the cleaned and splitted paragraph is:\n ",words)
c="course" in a 
if(c==True):
    print("The course description is {} characters long and has {} words".format(b,f))
else:
    print("The Word not found!")
