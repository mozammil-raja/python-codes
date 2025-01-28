
def isPerfect(num):
    sumF=0
    z=number//2 #half
    for i in range(1,z+1):
        if(number % (i)== 0): sumF+=i;
    if(sumF == number): return 1;
    else: return 0;


number =(int)(input("Enter a Number : "))
if isPerfect(number): print(f"{number} is a perfect number")
else: print(f"{number} is not a perfect number")
