X1=int(input())
Y1=X1
Z1=0
while(Y1>0):
   Z1=Z1+(Y1%10)**3
   Y1=Y1//10
if(Z1==X1):
  print('yes')
else:
  print('no')
