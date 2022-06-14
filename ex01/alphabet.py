import datetime
import random
ans_num = 10
lost_w=2
repeat_m=5
repeat=0
ans_list=[]
mode=False

def alphabets():
    global ans_num, lost_w, ans_list
    alp=[]
    for i in range(ans_num):
        number=random.randint(65,90)
        alphabet=chr(number)
        alp+=alphabet
    print(f"対象文字:\n{alp}")
    n=ans_num
    for j in range(lost_w):
        n-=1
        luck=random.randint(0,n)
        ans_list+=alp.pop(luck)
    print(f"表示文字:\n{alp}")
    #print(ans)

def main():
    st = datetime.datetime.now()
    while mode==False:
        alphabets()
        que()
        if repeat == repeat_m:
            break
        else:
            continue
    ed = datetime.datetime.now()
    print(f"繰り返し回数:{repeat_m}")
    print(f"かかった時間(s):{(ed-st).seconds}")

def que():
    global lost_w, ans_list, mode, repeat_m, repeat
    x=int(input("欠損文字はいくつあるでしょうか？"))
    if x==2:
        print("正解です。それでは、具体的に欠損文字を一つずつ入力してください")
        z=input("1つ目の文字を入力してください")
        result = z in ans_list
        if result==True:
            z2=input("2つ目の文字を入力してください")
            result2 = z2 in ans_list
            if result2==True:
                print("正解")
                mode=True
        else:
            print("不正解です.またチャレンジしてください")
            repeat+=1
    else:
        print("不正解です.またチャレンジしてください")
        repeat+=1
if __name__ == "__main__":
    main()