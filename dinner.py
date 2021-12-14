import os, random, time
f = open(os.getcwd() + "/log.txt", "r", encoding = "utf-8")
a = f.readlines()
li = []

for aa in a:
    li.append(aa.strip())

while True:
    word = input('要隨機選擇今天的晚餐嗎？')
    if word == 'q':
        break
    else:
        print("正在從資料庫" + str(li) + "中進行隨機選擇，請稍候...")
        time.sleep(1)
        print("今天的晚餐吃：" + random.choice(li))

os.system("pause")
    