a=int(input())

b=input()
list1=b.split()
while len(list1) != a:
    b=input()
    list1=b.split()
c=input()
list2=c.split()
while len(list2) != a:
    c=input()
    list2=c.split()
x=list2
count=0

def func():
    global count
    for i in range(a):
        # if '0' not in list2 :
        x[i]=int(x[i])-int(list1[i])
    
    count=count +1

    print(x)
    for i in range(a):
        if int(x[i]) <= 0:
            return count
    
    return func()

        # else:
        # #     for i in range(a):
        # # # if '0' not in list2 :
        # #         x[i]=int(x[i])-int(list1[i])
        #     count=count +1
        #     func()
    
ak=func()
print(ak)
# print(count)

# for i in range(a):
#         # if '0' not in list2 :
#     x[i]=int(x[i])-int(list1[i])
    
# print(x)
    

# print(count)