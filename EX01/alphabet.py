import random
import datetime
x = 10
y = 2

def shutudai():
    a = list() 
    b = list()
    while True:
        mozi = chr(random.randint(65,90))
        if mozi in a:
            continue
        else:
            a.append(mozi)
        if len(a) == x:
            break     

    print("対象文字")
    for i in range(x):
        print(a[i] , end =" ")
    print("")
    random.shuffle(a)
    for i in range(2):
        sakujo = a.pop()
        b.append(sakujo)
    
    print("表示文字")
    for i in range(x - y):
        print(a[i] , end =" ")
    print("")

    kaito1(b)

def kaito1(list):
    ans = int(input("欠損文字はいくつあるでしょうか？"))
    if ans == y :
        print("正解です。それでは具体的に欠損文字をひとつづつ入力してください")
        kaito2(list)
        
def kaito2(b):
    corect = 0
    for i in range(2):
        ans2 = input(f"{i + 1}つ目の文字を入力してください：")
        if ans2 in b:
            corect += 1
    if corect == 2:
        print("正解です。")
        
    else:
        print("不正解です。またチャレンジしてください。")


if __name__ == "__main__":
    st = datetime.datetime.now()
    shutudai()
    while True:
        if z == 1:
            shutudai()
        else:
            break
    ed = datetime.datetime.now()
    print(str((ed-st).seconds) + "秒")

