n=int(input("how many numbers u want?"))
n1=0
n2=1
count=0
if n<=0:
    print("pls enter a valid number")
elif n==1:
   print(n1)
else:
   print("the series of finacci are")
   while count<n:
       print(n1,end=" ")
       fn=n1+n2
       n1=n2
       n2=fn
       count+=1

