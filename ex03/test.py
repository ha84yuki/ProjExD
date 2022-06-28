import tkinter as tk 
import tkinter.messagebox as tkm

def count_up():
    global tmr,jid
    tmr = tmr +1
    label["text"]=tmr
    jid=root.after(1000,count_up)#リアルタイム処理中断
    
def key_down(event):#キー入力
    global jid 
    if jid !=None:#リアルタイム処理中断
        root.after_cancel(jid)
        jid = None
        return
    #key =event.keysym#キー入力
    #tkm.showinfo("キー押下",f"{key}キーが押されました")#キー入力
    jid=root.after(1000,count_up)

if __name__ == "__main__":
    root = tk.Tk()
    label = tk.Label(root,text="hello",font=("Times New Roman",80))
    label.pack()
    tmr=0
    root.bind("<KeyPress>",key_down)
    count_up()
    root.mainloop()
