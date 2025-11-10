a="""The 
Total
Bill of
customer is\n"""

name1='Python Basics'
price1=450
name2='Data Science Intro'
price2=600
b=450+600
e="Thank"
f="You"
g=e+f

statement=(a+"The name of book is {} \t Price is {}\n"+"The name of book is {} \t Price is {}\n"+"The Total Price: {}\n"+g)
statement=statement.format(name1,price1,name2,price2,b)
print(statement.upper())





