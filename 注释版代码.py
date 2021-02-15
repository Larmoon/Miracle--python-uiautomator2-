import uiautomator2 as u2#引用ui自动化库
money = 0#本次抢红包抢到的数额
d = u2.connect()#连接好安卓设备
d.app_start("com.tencent.mm")#打开微信
class record:#抢红包记录的类型
    def __init__(self,text,time):
        self.text = text#红包消息
        self.time = time#红包时间
record_list = []#记录的列表
def is_new(text,time):#判断这个红包是不是已经抢过
    for i in record_list:
        if i.text == text and i.time == time:
            return False
    return True
def find(position):#通过一连串resourceid找出ui元素
    try:
        i = d(resourceId="com.tencent.mm:id/" + position[0])
        for index in range(1, len(position)):
            i = i.child(resourceId="com.tencent.mm:id/" + position[index])
        return i
    except BaseException:
        print("resource id not found")
def get_red_packet():
    global record_list,money
    dialogues = find(["e8x", "bl6", "d5e", "g8f", "ffv", "f6r", "f67", "bg1"])
    for i in dialogues:
        text = i.child(resourceId="com.tencent.mm:id/e7t").get_text()
        time = i.child(resourceId="com.tencent.mm:id/j0l").get_text()
        if "[微信红包]" in text and is_new(text, time):
            record_list.append(record(text, time))
            i.click()
            red_packet = find(['ffv', 'auc', 'ay1', 'ay0', 'auh', 'avl', 'awv', 'aui'])
            red_packet[len(red_packet) - 1].click()
            try:
                find(['cc', 'ffv', 'f44', 'f42', 'f47', 'f4f']).click()
            except BaseException:
                print("红包抢完了呢")
            while True:#防止退出过快导致红包抢不到
                try:
                    sum = float(find(['bl6', 'ffv', 'ezj', 'eyw', 'ezi', 'eyr', 'eys', 'eyq']).get_text())
                    money += sum
                    print("今日已赚："+str(money)+"元")
                    break
                except BaseException:
                    continue
            d.press("back")
            d.press("back")
            break
while True:
    get_red_packet()