setc1={"green","blue"}
setc2={"blue","yellow"}

print("Original sets:")
print(setc1)
print(setc2)

setc=setc1.union(setc2)
print("\nUnion of the above sets:")
print(setc)

set=setc1.intersection(setc2)
print("\nIntersection of the above sets:")
print(set)