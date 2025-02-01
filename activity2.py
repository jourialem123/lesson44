set1={1,4,8,3,3,3,3,2,2,6,9,9,3,2,2}
set1.add(5)
print(set1)
set2={1,2,2,2,7,7,7,8,8,8,3,9}
print(set2)
print("The difference of set1 and set2 is ",set1.difference(set2))
print("The difference of set2 and set1 is ",set2.difference(set1))
print("The symetric difference of set1 and set2 is ",set1.symmetric_difference(set2))
print("The symetric difference of set2 and set1 is ",set2.symmetric_difference(set1))