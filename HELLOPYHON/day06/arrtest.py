arr = []

arr.append("가")
arr.append("나")
# arr.insert(0, "다") 앞에다 넣기
arr.insert(len(arr),"다")
arr.insert(len(arr),"라")

print(arr)