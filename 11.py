from PIL import Image
 
# 二值化处理
def two_value():
    for i in range(1,1):
        # 打开文件夹中的图片
        image=Image.open('./Img/'+str(i)+'.jpg')
        # 灰度图
        lim=image.convert('L')
        # 灰度阈值设为165，低于这个值的点全部填白色
        threshold=165
        table=[]
        
        for j in range(256):
            if j<threshold:
                table.append(0)
            else:
                table.append(1)
 
        bim=lim.point(table,'1')
        bim.save('./Img2/'+str(i)+'.jpg')
 
two_value()