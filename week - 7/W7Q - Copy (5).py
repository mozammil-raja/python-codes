term = int(input("Enter number of terms : "))
n1, n2 = 0, 1
count = 0
if term <= 0:
   print("Enter a positive integer")
elif term == 1:
   print(f"Fibonacci sequence upto{term}:")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < term:
       print(n1, end=" ")
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
