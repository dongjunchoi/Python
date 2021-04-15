import cv2
 
# 이미지 읽기
img = cv2.imread('4.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.resize(img, (28, 28))
img3 = (img2.reshape((1,28*28))/255)

# print(img3)
# 
# for i in img2:
#     for j in i:
#         if j > 40:
#             print(" ",end=" ")
#         else:
#             print("0",end=" ")
#     print()
#  
# 이미지 화면에 표시
# cv2.imshow('Test Image', img2)
cv2.waitKey(0)
# 이미지 윈도우 삭제
cv2.destroyAllWindows()
 
