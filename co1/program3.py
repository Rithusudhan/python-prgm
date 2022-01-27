

num=[10,0,-2,4,6,-7,8]
positive=[x for x in num if x > 0]
print(positive)


n=int(input("enter the limit:"))
square=[x*x for x in range(1,n+1)]
print(square)



word="english"
vowels="aeiou"
newlist=[x for x in word if x in vowels]
print(newlist)


word="english"
list=[ord(x) for x in word]
print(list)