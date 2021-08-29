import cv2

image = cv2.imread("Alex1small.jpg")
print("shape:",image.shape)
print("size:",image.size)
print("dtype:",image.dtype)
print("px rgb",image[642,499])
print("px",image[642,499,1])

#改变图片左上角区域的颜色 y:0-100 x:0-100
# for i in range(300,401):
#     for j in range(250,351):
#         image[i,j] = [100,100,100]

#将BGR转化为GRAY BLUE GREEN RED
gray_img = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
print("gray_img.shape",gray_img.shape)
# gray_img2 = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#将BGR转化为HSV  H 色彩 0红 180蓝 S 饱和度 V 明暗度
hsv_img = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
print("HSV_IMG.shape:",hsv_img.shape)
print("px hsv",hsv_img[642,499])
#拆分 合并BGR中的通道
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

#拆分HSV中的通道
# h,s,v = cv2.split(hsv_img)
# h[:,:]=180
# v[:,:]=255
# hsv_img_new = cv2.merge([h,s,v])
# cv2.imshow("h",h)
# cv2.imshow("s",s)
# cv2.imshow("v",v)

# img_new = cv2.cvtColor(hsv_img_new,cv2.COLOR_HSV2BGR)

#BRGA
img_BRGA = cv2.cvtColor(image,cv2.COLOR_BGR2BGRA)
b,g,r,a = cv2.split(img_BRGA)
a[:,:] = 172
img_BRGA_new = cv2.merge([b,g,r,a])
cv2.imwrite("img_bgra_172.png",img_BRGA_new)
# image = cv2.imread("img_bgra_0.png")
# cv2.imshow("img_new", image)
# cv2.waitKey()
# cv2.destroyAllWindows()