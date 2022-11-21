from PIL import Image
import os
import time

class AutoClickZhidaoCourse:
    def screenshot(self):
        os.system("adb shell /system/bin/screencap -p /sdcard/screenshot.jpg")
        os.system("adb pull /sdcard/screenshot.jpg D:/Documents/zhidao/screenshot.jpg")

    def cropPic(self, fileName):
        img = Image.open(fileName)
        img = img.convert("RGB")
        cropped = img.crop((0, 720, 1080, 2340))
        cropped.save("screenshotCropped.jpg")

    def handlePic(self, fileName):
        im = Image.open(fileName)
        width = im.size[0]
        height = im.size[1]
        im = im.convert("RGB")
        usefulPixels = 0
        for x in range(width):
            for y in range(height):
                r, g, b = im.getpixel((x, y))
                # print(r, g, b)
                if (r >= 0 and r <= 100 and g >= 150 and g <= 250 and b >= 110 and b <= 210):
                    usefulPixels += 1
        return 100*usefulPixels/(width*height)

    def autoClick(self):
        os.system("adb shell input tap 130 730")
        time.sleep(0.5)
        os.system("adb shell input tap 955 390")

    def isEnoughGreen(self):
        self.screenshot()
        self.cropPic("screenshot.jpg")
        NormalPercent = 0.1
        curPercent = self.handlePic("screenshotCropped.jpg")
        if(curPercent/NormalPercent > 0.1):
            return True
        else:
            return False

    def downTouchScreen(self):
        os.system("adb shell input swipe 580 2100 580 1400")

    # def upTouchScreen(self):
    #     os.system("adb shell input swipe 580 2100 580 2800")









