# 这个程序实现自动修改ID的功能（静默版本，无语音播放）
from DBDynamics import Bee
import time
m = Bee('COM9')

startID = 1
for target in range(startID, 18, 1):
    while True:
        time.sleep(0.1)
        ret = m.getDeviceType(0)
        if ret !=0:
            print("Device 0 is connected")
            print("新设备已连接")
            break
    currentID  = 0
    targetID = target
    print("Target ID: ", targetID)
    m.changeID(currentID, targetID)
    time.sleep(0.1) 
    ret = m.getDeviceType(targetID)
    if ret!=0:
        print("Device ", targetID, " is ready")
        msg = str(targetID) + "号设备修改成功"
        print(msg)

# 输出全部修改成功的信息
msg = "全部设备修改成功"
print(msg)

l = m.scanDevices()
ll = len(l)
print("Total devices: ", ll)
msg = "共扫描到" + str(ll) + "个设备"
print(msg)

m.stop()