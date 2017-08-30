i=int(input("请输入营业额\n"))
r=0
list1=[0,10,20,40,60,100]
list2=[0.1,0.075,0.05,0.03,0.015,0.01]
list1.reverse()
list2.reverse()
for index in range(0,6):

    if i>list1[index]:
        r+=(i-list1[index])*list2[index]
        i=list1[index]
print("奖金："+str(r))
