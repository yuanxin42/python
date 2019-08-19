from PIL import Image
import cv2
 

def custom_threshold(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    mean = gray.mean()
    print("mean:", mean)
    ret, binary = cv2.threshold(gray, mean, 255, cv2.THRESH_BINARY)
    print("阈值：%s" %ret)
    return ret
# 二值化处理

def two_value(imgStr):
    # 打开文件夹中的图片
    image=Image.open(imgStr)
    img = cv2.imread(imgStr)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print(gray)
    # 灰度图
    lim=image.convert('L')
    # 灰度阈值设为165，低于这个值的点全部填白色
    src1 = cv2.imread(imgStr)
    threshold = custom_threshold(src1)
    # threshold=165
    table=[]
    
    for j in range(256):
        if j<threshold:
            table.append(0)
        else:
            table.append(1)

    bim=lim.point(table,'1')
    bim.save('./Img2/zzzz.jpg')
 
two_value('./Img/WechatIMG15.jpeg')