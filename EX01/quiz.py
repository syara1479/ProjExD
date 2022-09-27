import random #ランダムモジュールをインポートする
import datetime

num = random.randint(1,4)

def shutudai(num_shutudai):
    Q = ["サザエの旦那の名前は？", "カツオの妹の名前は？", "タラオはカツオから見てどんな関係？"]
    if num_shutudai == 1:
        print(Q[0])
    elif num_shutudai ==2:
        print(Q[1])
    elif num_shutudai == 3:
        print(Q[2])


def kaito(num_kaito):
    A1 = ["マスオ", "ますお"]
    A2 = ["ワカメ", "わかめ"]
    A3 = ["甥", "おい", "甥っ子", "おいっこ"]
    ans = input("答えるんだ:")
    if num_kaito == 1:
        if ans in A1:
            print("正解")
        else:
            print("不正解")
    elif num_kaito ==2:
        if ans in A2:
            print("正解")
        else:
            print("不正解")
    elif num_kaito == 3:
        if ans in A3:
            print("正解")
        else:
            print("不正解")

st = datetime.datetime.now()
shutudai(num)
kaito(num)
ed = datetime.datetime.now()
print(str((ed-st).seconds) + "秒")