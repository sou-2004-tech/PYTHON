import random
apple=15.5
orange=20
grape=10.25
tot=apple+orange+grape
b=random.randrange(5,10)
tot1=b+tot

print("The Total volume of juice sold is: " +str(tot))
tot=int(tot)
print("The datatype of tot is: "+str(type(tot)))
tot=str(tot)
print("The datatype of tot is: "+str(type(tot)))
print("The total after adding the random number is: "+str(tot1))