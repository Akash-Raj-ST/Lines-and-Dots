n=int(input("No of Lines:"))
fact=1
fact1=[1]
fact2=[0,1,1]
j=1000000
for i in range(1,j):
    t=0
    fact=fact*i
    fact1.append(fact)
    fact2.append(fact*2)
    if fact1[-1]/fact2[-3]==n:
        if n>=3:
            l=len(fact1)-1
            break
        elif n==1:
            l=len(fact1)
            break     
        else:
            t=1
            break
    else:
        t=1
if t==1:  
    print("Maximum no of lines can be drawn using these points")
if fact1[-1]/fact2[-3]==n and t!=1:
    print("Dots Required: ",l)
        
