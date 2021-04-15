import random

mine = input("홀/짝을 선택하시오....")
print(mine)

rnd = random.random()
# rnd = random.randrange(1,3)
print(rnd)
if rnd > 0.5 :
    com = "홀"
else :
    com = "짝"

result = ""
if mine == com :
    result = "이겼습니다"
else :
    result = "졌습니다"

print("mine:",mine)
print("com:",com)
print("result=",result)