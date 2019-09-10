animal=input("Name your animal.")
list=["lion","cat","dog"]
if animal in list:
	print(animal.title(),'is in the list')
else:
	print(animal.title(),'is not in the list')
print(list.append("ox"))
list.sort()
print(list[0:4])
for list in list:
	print(list.title())
print(len(list))
for a in range(4,6):
	print (a)


