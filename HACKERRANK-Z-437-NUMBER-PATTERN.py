/* 

    1
   12
  123
 1234
12345

*/
n=int(input())
j=""
for i in range(1,n+1):
   j=j+str(i)
   print(" "*(n-i)+j,end="")
   print()
