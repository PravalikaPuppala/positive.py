mylist = []
n = int(input("enter number of elements :"))

for i in range(0, n):
    element = int(input())

    mylist.append(element)

print(mylist)
a=0

while a<len(mylist):

    if mylist[a]>=0:

        print(mylist[a],"")

    a=a+1
