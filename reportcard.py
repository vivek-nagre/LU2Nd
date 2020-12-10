
# first assignment to make the the report card
mark=int(input("enter your mark:"))
if mark>70 :
    print("A grade")
elif mark>50 and mark<60  :
    print("B grade")
elif mark>40 and mark<50  :
    print("C grade")
else:
    print("fail")


print("find the prime number in between 1-1000")
lower = 1
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
print("")
print("")
print("")
print("tables")
for r in range(1,11):
    for j in range(1,11):
        print(r*j,end=" ")
    print()
