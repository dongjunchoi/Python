# 필요한 라이브러리 불러오기
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import cv2

# MNIST 데이터셋 불러오기
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

for i in range(len(train_images)):
    lable = str(train_labels[0])
    cv2.imwrite("image/"+lable+"_"+str(i)+".jpg", train_images[i])

cv2.waitKey(0)
cv2.destroyAllWindows()
 
print(train_images[0])

for i in train_images[0]:
    for j in i:
        if j > 0:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()
