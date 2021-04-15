import cv2
import sys
import argparse
import requests
from PIL import Image, ImageFilter

# 이미지 읽기
img = cv2.imread('bts.jpg', 1)

# for i in img:
#     for j in i:
#         j[0] = 0
#         j[2] = 0
        

print(img)
print("shape:",img.shape)


# # 이미지 화면에 표시
# cv2.imshow('original', img)
# cv2.waitKey(0)
# # 이미지 윈도우 삭제
# cv2.destroyAllWindows()


API_URL = 'https://dapi.kakao.com/v2/vision/face/detect'
MYAPP_KEY = '54cf49304e421fee8561b41998ad6244'

def detect_face(filename):
    headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}

    try:
        files = { 'image' : open(filename, 'rb')}
        resp = requests.post(API_URL, headers=headers, files=files)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(str(e))
        sys.exit(0)

def mosaic(filename, detection_result):
    image = Image.open(filename)

    for face in detection_result['result']['faces']:
        x = int(face['x']*image.width)
        w = int(face['w']*image.width)
        y = int(face['y']*image.height)
        h = int(face['h']*image.height)
        box = image.crop((x,y,x+w, y+h))
        box = box.resize((20,20), Image.NEAREST).resize((w,h), Image.NEAREST)
        image.paste(box, (x,y,x+w, y+h))

    return image



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Mosaic faces.')
    parser.add_argument('image_file', type=str, nargs='?', default="C:\\workspce_python\\HELLOPYHON\\day14cv\\bts.jpg",
                        help='image file to hide faces')

    args = parser.parse_args()

    detection_result = detect_face(args.image_file)
    image = mosaic(args.image_file, detection_result)
    image.show()
