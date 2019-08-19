# -*- coding:utf-8 -*-
import cv2
import os
import numpy as np
import copy
from PIL import Image



print(cv2.imread)

''' 根据该像素周围点为黑色的像素数（包括本身）来判断是否把它归属于噪声，如果是噪声就将其变为白色'''
'''
	input:  img:二值化图
			number：周围像素数为黑色的小于number个，就算为噪声，并将其去掉，如number=6，
			就是一个像素周围9个点（包括本身）中小于6个的就将这个像素归为噪声
	output：返回去噪声的图像
'''

def del_noise(img,number):
    height = img.shape[0]
    width = img.shape[1]

    img_new = copy.deepcopy(img)
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            point = [[], [], []]
            count = 0
            point[0].append(img[i - 1][j - 1])
            point[0].append(img[i - 1][j])
            point[0].append(img[i - 1][j + 1])
            point[1].append(img[i][j - 1])
            point[1].append(img[i][j])
            point[1].append(img[i][j + 1])
            point[2].append(img[i + 1][j - 1])
            point[2].append(img[i + 1][j])
            point[2].append(img[i + 1][j + 1])
            for k in range(3):
                for z in range(3):
                    if point[k][z] == 0:
                        count += 1
            if count <= number:
                img_new[i, j] = 255
    return img_new


if __name__=='__main__':
    img_dir = './Img'
    img_name = os.listdir(img_dir)  # 列出文件夹下所有的目录与文件
    kernel = np.ones((5, 5), np.uint8)
    for i in range(len(img_name)):
        path = os.path.join(img_dir, img_name[i])
        image = cv2.imread(path)
        name_list = list(img_name[i])[:5]
        if '.' in name_list:
            print("%s标签错误，请重新标签!" % img_name[i])
        else:
            name = ''.join(name_list)
            print("没有走我啊")
            # 灰度化
            # print(image.shape)
            grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # 二值化
            result = cv2.adaptiveThreshold(grayImage, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 1)
            # 去噪声
            img = del_noise(result, 6)
            img = del_noise(img, 4)
            img = del_noise(img, 3)
            # 加滤波去噪
            im_temp = cv2.bilateralFilter(src=img, d=15, sigmaColor=130, sigmaSpace=150)
            im_temp = im_temp[1:-1,1:-1]
            im_temp = cv2.copyMakeBorder(im_temp, 83, 83, 13, 13, cv2.BORDER_CONSTANT, value=[255])
            cv2.imwrite('./Img3/%s.jpg' %(name), im_temp)
            print("%s %s.jpg"%(i,name))
    print("图片预处理完成！")