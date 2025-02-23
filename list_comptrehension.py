even=[]
odd=[]
for x in range(10):
    if x%2==0:
        even.append(x)
    elif x%2!=0:
        odd.append(x)
print(even)
print(odd)

even=[x for x in range(10) if x%2==0]
print(even)

odd=[x for x in range(10) if x%2!=0]
print(odd)

cubes=[]
for x in range(10):
    if x%2==0:
        cubes.append(x**3)
print("using For loop : ",cubes)

cubes=[x**3 for x in range(10) if x%2==0]
print(cubes)

