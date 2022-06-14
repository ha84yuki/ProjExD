def Q1():
    A1 = input("問題：\nサザエの旦那の名前は？\n答えるんだ:")
    if A1 == "マスオ" and "ますお":
        print("正解!!!")
    else:
        print("出直してこい")

def Q2():
    A2 = input("問題：\nカツオの妹の名前は？\n答えるんだ:")
    if A2 == "わかめ" and "ワカメ":
        print("正解!!!")
    else:
        print("出直してこい")

def Q3():
    A3 = input("問題：\nタラオはカツオから見てどんな関係？\n答えるんだ:")
    if A3 == "甥" and "おい" and "甥っ子" and "おいっこ":
        print("正解!!!")
    else:
        print("出直してこい")

from random import randint
n=randint(1, 3)
if n == 1:
    Q1()
elif n == 2:
    Q2()
elif n == 3:
    Q3()