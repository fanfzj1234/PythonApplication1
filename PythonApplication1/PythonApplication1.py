import random
arr = ('1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

f=file('test.txt','w') 
for i in range(10000):
     n=""
     a=""
     n=random.sample(arr,6)
     for x in range(6):
         a+=n[x]
     if x==6: break
     f.write(a)
     f.write("\n")
else: print "\n"
f.close()
