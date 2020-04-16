list=[100,300,250]
sum=0
for i in list:
    if sum<=1000:
        print("Shopping successfull")
        break
    sum=sum+list[i]
else:
    print("insufficient balance in account")
