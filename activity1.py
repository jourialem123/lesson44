tup1=()
tup2=(1,5,9,16)
tup3=(6,)
tup2=tup2+tup3
print(tup1)
print(tup2)
tup4=("Hello",15,[1,5,8,90])
tup5=("Hello everyone")
print(tup4[0])
print("Sliced tuple is ",tup5[2:3])
tup6=((2,4,8),(14,80,4),(5,578,456))
print("Nested tuple is ",tup6)

tup7=("W",'o','r','l','d')

for tup in tup7:
    print("Hello",tup)