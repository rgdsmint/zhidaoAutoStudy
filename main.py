from zhidao import AutoClickZhidaoCourse
import time

if __name__=='__main__':
    unableScanGreenTimes = 0
    aczc = AutoClickZhidaoCourse()
    while(True):
        if(not aczc.isEnoughGreen()):
            unableScanGreenTimes+=1
            aczc.autoClick()
            time.sleep(1)
            print("Click!")
            while (unableScanGreenTimes >= 3):
                aczc.downTouchScreen()
                time.sleep(1)
                if (aczc.isEnoughGreen()):
                    unableScanGreenTimes = 0
                    print("Next page!")
                    break
        else:
            time.sleep(2)
            unableScanGreenTimes = 0