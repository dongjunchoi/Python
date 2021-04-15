# 수학 점수를 입력하시오.
# 국어 점수를 입력
# 영어 점수를 입력
# 평균 : *
# 총점 : *

math = input("수학 점수를 입력하세요.")
kor = input("국어 점수를 입력하세요.")
eng = input("영어 점수를 입력하세요.")

total = int(math) + int(kor) + int(eng)
avg = total/3
print()

# print("수학 점수 :",math)
# print("국어 점수 :",kor)
# print("영어 점수 :",eng)
print("평균 =",avg)
print("총점 =",total)