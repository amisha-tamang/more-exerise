# Question 7

# Socho aapke paas 2 lists hain. Aapne aisa code likhna hain jisse ek nayi list banne jisme
#  inn dono lists ke woh item hone chaiye ho dono list mein aa rahe hain. Socho aapki do list yeh hain:
 
list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1] 
i=0
d=[]
while i<len(list1):
    if list1[i] in list2:
        d.append(list1[i])
    i=i+1
print(d)