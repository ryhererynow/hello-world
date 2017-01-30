#x= "hello"
#print (x)
#print (7/3)
#print (7//3)
#print (7%3)
#print (5==5)

n= input("choose a number")

n = int(n)

def recurse(n):
    if n > 0:
        print (n)
        n = n-1
        recurse(n)
    else:
        return

recurse(n)

x=str(n)

print(x*n)



    
    







