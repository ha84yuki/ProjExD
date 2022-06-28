import tkinter as tk
import tkinter.messagebox as tkm

def key_down(event):
    global key 
    key = ""
    key=event.keysym


if __name__ == "__main__":
    root = tk.Tk()
    root.title('迷えるこうかとん')
    
    canvas=tk.Canvas(root,width=1500,height=900,background='black')#サイズと背景色
    canvas.pack()

    tori= tk.PhotoImage(file='fig/2.png')#こうかとん配置
    cx,cy=300,400
    canvas.create_image(cx,cy,image=tori,tag='tori')

    root.mainloop()