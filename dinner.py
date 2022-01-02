import os, random, time

# foods = []

# 讀取檔案
def read_file(filename, foods):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '店家,公休日,電話' in line:
                continue
            name, leave, tel = line.strip().split(',')
            foods.append([name, leave, tel])
    return foods

# 讓使用者輸入
def user_input(foods):
    while True:
        print('增加晚餐店家，請輸入1\n' + '隨機選擇晚餐，請輸入2\n' + '查看目前所有店家資料，請輸入3')
        opt = input('請輸入： ')
        if opt == '1':
            add_store(foods)
        elif opt == '2':
            ran_choose(foods)
        elif opt == '3':
            print_info(foods)
        else:
            print('輸入資料無效，關閉程式')
            break
    return foods
    
# 增加店家
def add_store(foods):
    while True:
        answer = input('輸入任意文字以繼續，若要退出店家管理系統，請輸入q： ')
        if answer == 'q':
            break
        else:
            name = input('請輸入欲增加之店家名稱： ')
            leave = input('請輸入公休日： ')
            tel = input('請輸入電話： ')
            foods.append([name, leave, tel])
    return foods

# 隨機選擇晚餐
def ran_choose(foods):
    for d in foods:
        print('正在從晚餐資料庫中進行隨機選擇，請稍候...')
        time.sleep(1)
        print('今天的晚餐吃：' + random.choice(d) + '公休日為' + d[1] + '，' + d[2])

# 印出目前所有店家資訊
def print_info(foods):
    for s in foods:
        print(s[0] + '的公休日為' + s[1] + '，' + '電話為' + s[2])

# 寫入檔案
def write_file(filename, foods):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('店家,公休日,電話\n')
        for d in foods:
            f.write(d[0] + ',' + d[1] + ',' + d[2] + '\n')

def main():
    foods = []
    filename = 'dinner.csv'
    if os.path.isfile(filename):
        print('Yeah!找到檔案了！')
        foods = read_file(filename, foods)
    else:
        print('Sorry...找不到檔案')

    foods = user_input(foods)
    write_file('dinner.csv', foods)

if __name__ == '__main__':
    main()


# opt = input('增加晚餐店家，請輸入1；隨機選擇晚餐，請輸入2： ')
# data = []
# if opt == '1':
#     with open('log.txt', 'r') as f:
#         for line in f:
#             data.append(line.strip())
# else:
#     while True:
#         if opt == 'q':
#             break
#         else:
#             print('正在從晚餐資料庫中進行隨機選擇，請稍候...')
#             time.sleep(1)
#             print('今天的晚餐吃：' + random.choice(data))

# f = open(os.getcwd() + "/log.txt", "r", encoding = "utf-8")
# a = f.readlines()

# for aa in a:
#     li.append(aa.strip())

# while True:
#     word = input('要隨機選擇今天的晚餐嗎？')
#     if word == 'q':
#         break
#     else:
#         print("正在從資料庫" + str(li) + "中進行隨機選擇，請稍候...")
#         time.sleep(1)
#         print("今天的晚餐吃：" + random.choice(li))

# os.system("pause")
    