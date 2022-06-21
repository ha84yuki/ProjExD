from random import randint, random
import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn=event.widget
    i = btn["text"]
    #tkm.showinfo("",f"{i}のボタンがクリックされました")
    entry.insert(tk.END,i)

def click_eqall(event):#=の関数
    eqn=entry.get()
    res=eval(eqn)
    entry.delete(0,tk.END)
    entry.insert(tk.END,str(res))

def click_alclear(event):#文字列全削除
    entry.delete(0,tk.END)
    entry.insert(tk.END)
    
def click_clear(event):#一文字削除
    cl=entry.get()
    cl2=cl[:-1]
    entry.delete(0,tk.END)
    entry.insert(tk.END,str(cl2))

def click_lucky(event):
    entry.delete(0,tk.END)
    color_n=randint(1,7)
    if color_n==1:
        color="赤"
        entry["bg"] = "#ff0000"
    elif color_n==2:
        color="橙"
        entry["bg"] = "#ffa000"
    elif color_n==3:
        color="黄"
        entry["bg"] = "#ffff00"
    elif color_n==4:
        color="緑"
        entry["bg"] = "#008000"
    elif color_n==5:
        color="青"
        entry["bg"] = "#0000ff"
    elif color_n==6:
        color="藍"
        entry["bg"] = "#2e4b71"
    else:
        color="紫"
        entry["bg"] = "#800080"
    entry.insert(tk.END,str(color))

if __name__ == '__main__':
    root = tk.Tk()
    #root.geometry("300x600")
    root.title("電卓")

    entry = tk.Entry(root, justify="right",width=10,font=("Times New Roman",40))
    entry.grid(row=0,column=0,columnspan=3)

    r,c=1,0
    for i,num in enumerate(["AC","C","/","*",9,8,7,"-",6,5,4,"+",3,2,1,"=",0,"LC"]):
        btn =tk.Button(root,
                       text=num,
                       width=4,
                       height=2,
                       font=("Times New Roman",30)
                    )
        btn.bind("<1>", button_click)
        btn.grid(row=r,column=c)
        c+=1
        if num=="=":
            btn.bind("<1>",click_eqall)
        if num=="AC":
            btn.bind("<1>",click_alclear)
        if num=="C":
            btn.bind("<1>",click_clear)
        if num=="LC":
            btn.bind("<1>",click_lucky)
        if (i+1)%4==0:
            r+=1
            c=0

    root.mainloop()