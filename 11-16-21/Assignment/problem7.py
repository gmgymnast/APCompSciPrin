def getMax (n1,n2,n3,n4):
   max = n1
   if (n2 > max):
         max = n2
   elif (n3 > max):
         max = n3
   elif (n4 > max):
         max = n4
   return max

print (getMax(30,40,10,60))
