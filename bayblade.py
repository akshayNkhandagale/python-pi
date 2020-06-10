a=int(input())

for i in range(a):
    try:
        b=int(input())
        c=input()
        # list1=c.split()
        list1=sorted(c.split(),reverse=True)   #sorted the 1st list in desending order to compair largest number 
        d=input()
        list2=d.split()
    except Exception as e:
        print("")


    count=0

    for i in range(len(list1)):
        list3=[]                                    # every time list3 going to be empty
        for j in range(len(list2)):                 
            if(list1[i] > list2[j]):
                list3.append(list2[j])
                        
    
    # print(max(list3))
    
        try:
            list2.remove(max(list3))
        except:
            break
        count=count+1
    
        print(list3)     
        print("\n")

    print(count)
