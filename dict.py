item1=input("Enter key-value 1st dictionary").split()
item2=input("Enter key-value 2nd dictionary").split()
dict1={item1[i]:item1[i+1]for i in range(0,len(item1),2)}
dict2={item2[i]:item2[i+1]for i in range(0,len(item2),2)}
merged=dict1.copy()
merged.update(dict2)
print("merged dictionary:", merged)