s="good morning guys"
flag=0
c=""
for i in s:
    if s.count(i)==1:
        c=i
        flag=1
        break
print("no non-repeating chars" if flag == 0 else "char =",c)
        
