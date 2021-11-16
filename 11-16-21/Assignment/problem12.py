def getP (n1,n2):
   temp = 1
   while (temp != 0):
      temp = n1 % n2
      if (temp == 0):
         p = n2
      else:
         n1 = n2
         n2 = temp
   return p
   
def getQ(n1,n2):
   p = getP(n1,n2)
   q = n1 // p* n2
   return q
   
print (getQ(200,300))