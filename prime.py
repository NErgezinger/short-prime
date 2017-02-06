l=[]
for i in range(1,1000,2):
    p=True
    for j in range(2,i):
        if i%j==0:p=False
    if p:l.append(i)
print(l)
