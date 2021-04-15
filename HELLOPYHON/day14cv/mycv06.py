import cv2

# 이미지 읽기
img = cv2.imread('bts.jpg', 1)

for i in img:
    for j in i:
        j[0] = 0
        j[2] = 0
        

print(img)
print("shape:",img.shape)

img90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# 이미지 화면에 표시
cv2.imshow('original', img)
cv2.imshow('rotate90', img90)
cv2.waitKey(0)
# 이미지 윈도우 삭제
cv2.destroyAllWindows()

# 이미지 다른 파일로 저장
cv2.imwrite('bts2.png', img)
 
