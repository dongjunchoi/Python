import random

mine = input("가위/바위/보 중 하나를 내시오...")

rnd = random.randrange(1,3)

if rnd == 1:
    com = "가위"
elif rnd == 2:
    com = "바위"
else :
    com = "보"

result = ""
if mine == "가위" and com == "가위" :
    result = "비겼습니다."
elif mine == "바위" and com == "바위" :
    result = "비겼습니다."
elif mine == "보" and com == "보" :
    result = "비겼습니다."

elif mine == "바위" and com == "가위" :
    result = "이겼습니다."
elif mine == "바위" and com == "바위" :
    result = "비겼습니다."
elif mine == "바위" and com == "보" :
    result = "졌습니다."
    
elif mine == "보" and com == "가위" :
    result = "졌습니다."
elif mine == "보" and com == "바위" :
    result = "이겼습니다."
elif mine == "보" and com == "보" :
    result = "비겼습니다."
else:
    pass

print("mine : ",mine)
print("com : ", com)
print("result = ", result)
