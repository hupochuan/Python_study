list=[1,2,3,4]
cout=0;
for a in list:
    for b in list:
        for c in list:
            if a!=b and b!=c and a!=c:
                print(a*100+b*10+c)
                cout+=1
print("能组成三位数的个数为{0:d}".format(cout))