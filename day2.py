#5. Bitwise Operators (&,|,^,~,<<,>>)
print(13&8)
print(13<<1)#13 left shift by one(usually doubles the no. at shift by 1 then if by 2 then double no. of 13<<1 and so on)
print(13>>1)#right shift by 1 gives half only int value
print(~13)# ~n=-(n+1) as it thinks 0 mirror image as -1 (-0) so shift no. line by 1
#6 Membership Operators(in,not in)
#7 Identity Operators(is,is not) gives true only if address same while = checks value
l1=[1,2,3]
l2=[1,2,3]
print(id(l1),id(l2))
#For loop
for i in range(0,11,1):#runs upto stop-1
    print(f"3 * {i} = {3*i}")
#while loop
#break statement 
#continue statement 
#pass statement
#for else (else runs when for loop naturally ends without break)