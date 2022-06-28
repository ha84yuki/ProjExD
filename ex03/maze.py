import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mk

def key_down(event):
    global key 
    key=event.keysym

def key_up(event):
    global key
    key=""

def main_proc():#こうかとんの移動
    global cx,cy,key,mx,my
    if key == "Up" and maze_bg[my-1][mx]==0:
            my-=1
    elif key=="Down" and maze_bg[my+1][mx]==0:
        my+=1
    elif key=="Right" and maze_bg[my][mx+1]==0:
        mx+=1
    elif key=="Left" and maze_bg[my][mx-1]==0:
        mx-=1
    cx,cy=100*mx+50,100*my+50

    canvas.coords("tori",cx,cy)
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
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    
    root.after(100,main_proc)
    root.mainloop()