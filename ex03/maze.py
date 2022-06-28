from itertools import count
import random
import tkinter as tk
import tkinter.messagebox as tkm
from turtle import back
from unittest import skip
import maze_maker as mk
global goal
goal=True
global c_t,key,mx,my,cx,cy
c_t = 0

def over_10s(): #30回で煽り機能
    global c_t
    if c_t ==30:
        tkm.showinfo(root,f"{c_t}回動いたおw急ごうね")


def key_down(event):
    global key 
    key=event.keysym

def key_up(event):
    global key,goal
    key=""
    if cx==1350 and cy==750 and goal==True :#ゴールメッセージ
        tkm.showinfo(root,f"ゴール!!!{c_t}回移動したよ")
        goal=None
    elif cx==1350 and cy==150 : #ヒント処理機能
        tkm.showinfo(root,"ゴールは下だよ")
    elif cx==150 and cy==750 : #ヒント処理機能
        tkm.showinfo(root,"ゴールは右だよ")

def main_proc():#こうかとんの移動とカウントの増加
    global cx,cy,key,mx,my,c_t
    if key == "Up" and maze_bg[my-1][mx]==0:
        my-=1
        c_t += 1
    elif key=="Down" and maze_bg[my+1][mx]==0:
        my+=1
        c_t += 1
    elif key=="Right" and maze_bg[my][mx+1]==0:
        mx+=1
        c_t += 1
    elif key=="Left" and maze_bg[my][mx-1]==0:
        mx-=1
        c_t += 1
    cx,cy=100*mx+50,100*my+50
    over_10s()

    canvas.coords("tori",cx,cy)
    
    if cx!=1350 or cy!=750:#ゴール以外でしか動けない
        root.after(100,main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title('迷えるこうかとん')
    
    canvas=tk.Canvas(root,width=1500,height=900,background='black')#サイズと背景色
    canvas.pack()

    maze_bg=mk.make_maze(15,9)#背景の描画
    mk.show_maze(canvas,maze_bg)

    tori= tk.PhotoImage(file='fig/2.png')#こうかとん配置
    mx,my=1,1
    cx,cy=100*mx+50,100*my+50
    canvas.create_image(cx,cy,image=tori,tag='tori')

    key= ""
    if cx!=1350 and cy!=750:
        root.bind("<KeyPress>",key_down)
        root.bind("<KeyRelease>",key_up)
    #スタートとゴール地点の追加
    label = tk.Label(root,text="S",font=("Times New Roman",50),bg="red")
    label.pack()
    label.place(x=70,y=100)
    label = tk.Label(root,text="G",font=("Times New Roman",50),bg="blue")
    label.pack()
    label.place(x=1400,y=700)
    
    root.after(100,main_proc)
    
    root.mainloop()