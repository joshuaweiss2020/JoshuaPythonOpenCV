import cv2
import numpy as np

image = cv2.imread("Alex1small.jpg")
print("shape:", image.shape)
print("size:", image.size)
print("dtype:", image.dtype)
print("px rgb", image[642, 499])
print("px", image[642, 499, 1])

# 改变图片左上角区域的颜色 y:0-100 x:0-100
# for i in range(300,401):
#     for j in range(250,351):
#         image[i,j] = [100,100,100]

# 将BGR转化为GRAY BLUE GREEN RED
gray_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
print("gray_img.shape", gray_img.shape)
# gray_img2 = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# 将BGR转化为HSV  H 色彩 0红 180蓝 S 饱和度 V 明暗度
hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
print("HSV_IMG.shape:", hsv_img.shape)
print("px hsv", hsv_img[642, 499])
# 拆分 合并BGR中的通道
# b,g,r = cv2.split(image)
# cv2.imshow("b",b)
# cv2.imshow("g",g)
# cv2.imshow("r",r)
# print("B.shape",b.shape)
# b[:,:]=180
# g[:,:]=90
# image_new = cv2.merge([b,g,r])
#
# cv2.imshow("m",image_new)

# 拆分HSV中的通道
# h,s,v = cv2.split(hsv_img)
# h[:,:]=180
# v[:,:]=255
# hsv_img_new = cv2.merge([h,s,v])
# cv2.imshow("h",h)
# cv2.imshow("s",s)
# cv2.imshow("v",v)

# img_new = cv2.cvtColor(hsv_img_new,cv2.COLOR_HSV2BGR)

# BRGA
# img_BRGA = cv2.cvtColor(image,cv2.COLOR_BGR2BGRA)
# b,g,r,a = cv2.split(img_BRGA)
# a[:,:] = 172
# img_BRGA_new = cv2.merge([b,g,r,a])
# cv2.imwrite("img_bgra_172.png",img_BRGA_new)
# image = cv2.imread("img_bgra_0.png")
# cv2.imshow("img_new", image)
# cv2.waitKey()
# cv2.destroyAllWindows()

# 通过NUMPY 创建图像
w = 200
h = 100
img = np.zeros((h, w), np.uint8)
# cv2.imshow("black", img)
# img = np.ones((h, w), np.uint8) * 255
# cv2.imshow("white", img)

# 在白色中，抠出一个20象素的黑色正方形
# sqr = 20
# img[int(height / 2 - sqr / 2): int(height / 2 + sqr / 2), int(width / 2 - sqr / 2): int(width / 2 + sqr / 2)] = 0
#创建琴键
# sqr = 50
# for i in range(0,w,sqr):
#     img[:,i:i+25] = 255
#
# cv2.imshow("new", img)

#创建彩色图像
# img_color = np.zeros((h,w,3),np.uint8)
# blue = img_color.copy()
# blue[:,:,0] = 255
# cv2.imshow("blue",blue)
# green = img_color.copy()e
# green[:,:,1] = 255
# cv2.imshow("green",green)
# red = img_color.copy()
# red[:,:,2] = 255
# cv2.imshow("red",red)
#生成雪花点
# img = np.random.randint(256,size=(h,w,3),dtype=np.uint8)
#拼接
img_2 = np.hstack((image,image))

cv2.imshow("snow",img_2)
cv2.waitKey()
cv2.destroyAllWindows()
