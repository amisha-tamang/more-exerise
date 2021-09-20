# Question 8


list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16] 
i=0
a=[]
while i<len(list1):
    c=list1[i]
    if c not in a:
        a.append(c)
        j=0
        while j<len(list2):
            d=list2[j]
            if d not in a:
                a.append(d)
            j=j+1
    i=i+1
print(a)
  


# [1, 2, 5, 10, 12, 13, 16, 20] 