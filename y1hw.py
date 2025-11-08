
import random
rp=45
sp=40
op=130
rw=3
sw=2.5
ow=1.8
print("The Total Price is: ")
print("rice: ",rp*rw)
print("sugar: ",sp*sw)
print("oil: ",op*ow)
total=rp*rw+sp*sw+op*ow
print("The Total Bill is: ",total)
print("The total bill as an integer is: ",int(total))
print("The Total value in String is: ",str(total))
total=float(total)
ra=random.randrange(5,10)
print("The Delivery Charge is: ",ra)
print("The Total After Adding Delivery Charge is Price is: ",total+ra)
