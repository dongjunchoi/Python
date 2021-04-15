# 구구단 3단출력
num = 3;
sum = 0;
for i in range(10):
    if i != 0:
        sum = num * i
#         print(str(num) + "*" + str(i) + "=" + str(sum))
        print(num,"*",i,"=",sum)
        
print()

for i in range(9):
    print("4 * " + str((i+1)) + " = " + str((i+1)*4) + "")