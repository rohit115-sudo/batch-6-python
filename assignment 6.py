list1=[1,2,3,4,5,7,8]
list2= ["a","b","c","d","e"]
res = {}
for key in list1:
 for value in list2:
     res[key] = (value)
 list2.remove(value)
 break


print ("dictionary output is : " + str(res))