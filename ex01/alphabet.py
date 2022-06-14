import random 
import string
global t,n,lost_w,uncommon
t=1
lost_w=0
uncommon=0
n=random.randint(1,9)

def syutudai():
    list_a = list(string.ascii_uppercase) #list_a全てのアルファベット
    alphabet=[] #選ばれるやつ１０こ
    alphabet=random.sample(list_a, 10)
    point_alpha=[] #欠損文字
    rand_alpha=random.shuffle(alphabet)
    print(f"対象文字：\n{rand_alpha}")
    point_alpha=random.sample(rand_alpha, n)
    uncommon = set(alphabet) ^ set(point_alpha)
    print(f"表示文字：\n{uncommon}\n")
    lost_w=len(uncommon)

def kaitou():
    A1=input(f"欠損文字はいくつあるでしょうか？：{A1}")
    if A1 == lost_w:
        print("正解です.それでは、具体的な欠損文字を１つずつ入力してください")
        while (t <= lost_w):
            A2=input(f"{t}つ目の文字を入力してください：{A2}")
            if A2 in uncommon:
                t+=1
            else:
                default()
                break
    else:
        default()

def default():
    print("不正解です.またチャレンジしてください")

def main():
    syutudai()

main()