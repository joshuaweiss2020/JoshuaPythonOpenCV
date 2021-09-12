import cv2
import numpy as np
import os


def findCenter(c,image,i):

    # ?????
    # for c in cnts:
        # ??????????? ???????????????????????????????????????????????????????????????????x?y?????????????????
        M = cv2.moments(c)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        # ???????????
        #     cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
        # cv2.circle(image, (cX, cY), 3, (0, 255, 0), -1)
        # cv2.putText(image, str(i), (cX - 20, cY - 20),
        #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

        return cX,cY

imgFiles = []
# if 1:
for root,dir,files in os.walk("./img"):
    for file in files:
        # file = "20210911_161337.jpg"
        img = cv2.imread("img/{}".format(file))
        # img = cv2.imread("img_res/20210911_161104.jpg")
        # img = cv2.imread("img_res/20210911_161123.jpg")
        # img = cv2.imread("img_res/20210911_161337.jpg")
        #img = cv2.imread("img_res/20210911_161401.jpg")
        # img = cv2.imread("img_res/20210911_161714.jpg")
        # img = cv2.imread("img_res/20210911_161403.jpg")



        # cv2.imshow("1", img)
        # cv2.waitKey()

        # ????
        filter = cv2.bilateralFilter(img, 30, 120, 100)
        # ????
        # filter = cv2.medianBlur(img, 5)
        # ????
        # filter = cv2.GaussianBlur(img,(9,9),0,0)
        # cv2.imshow("2", filter)
        # cv2.waitKey()
        # ????
        gray_img = cv2.cvtColor(filter, cv2.COLOR_RGB2GRAY)
        # cv2.imshow("3", gray_img)
        # cv2.waitKey()
        # ????
        t1, binary = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
        # cv2.imshow("4", binary)
        # cv2.waitKey()
        # ???
        contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # ???
        imgcopy = img.copy()
        cv2.drawContours(imgcopy, contours, -1, (0, 0, 255), 5)
        # cv2.imshow("5", imgcopy)
        # cv2.waitKey()
        cY_max = 0
        target_cX =0
        target_idx = 0
        for i in range(0, len(contours) - 1):
            l = cv2.arcLength(contours[i], True)
            area = cv2.contourArea(contours[i], False)
            # print(i,":",len(contours[i]))
            #if len(contours[i]) > 20 and len(contours[i]) < 30:
            # if i in (132,147,151):
            if len(contours[i]) < 250 and area>700:
                # cv2.drawContours(img, contours[i], -1, (0, 0, 255), 5)
                cX,cY = findCenter(contours[i],img,i)
                # print(i, ":", len(contours[i]),"length:",l,"area:",area,"cX?",cX,"cY:",cY)
                if cY>cY_max:
                    cY_max = cY
                    target_cX = cX
                    target_idx = i

        cv2.drawContours(img, contours[target_idx], -1, (0, 0, 255), 5)
        cv2.circle(img, (target_cX, cY_max), 3, (0, 255, 0), -1)
        cv2.putText(img, str(target_idx), (target_cX - 20, cY_max - 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

        # for i in (0,len(contours)-1):
        #      print(contours[i])
        # print(len(contours))
        # print(dst1.shape)
        # cv2.drawContours(img, contours[9], -1, (0, 0, 255), 5)
        cv2.imshow(file, img)
        cv2.waitKey()

cv2.destroyAllWindows()
#132 147 151