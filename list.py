#create a list of 10 nums print sum of last 4 elements of the list find out diff between max and min element of the list ,insert a num in a list at 6 th position this num must be 1/3 of num stored at 4 th postion.


lis=[1,2,99,45,23,56,89,24,77,88]

sum=0
for i in lis[6:-1]:#used slicing
    sum+=i
print("sum of last 4 numbers of list are:",sum)

print("diffrence between max and min element",max(lis)-min(lis))#used inbuilt function

newnum=lis[3]//3
lis.insert(6,newnum)#inserted  num which is 1/3 of 4th postion num to 6 th postion of list
print("list after inserting element at 6 th position:",lis)



