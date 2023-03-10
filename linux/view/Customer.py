from tabnanny import check
from tkinter import *
from tkinter import ttk
import pandas as pd
win = Tk()
win.geometry("500x300")
def delt():
    #lay  = sho.get()
    #sho.delete(0, END)
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)
    ent4.delete(0, END)
    ent5.delete(0, END)

def hienthi():
    datacus = {'Ma KH':['k01','k02','k03','k04'],
               'TenKH':['Nguyen Thien Thuat', 'Trau Sinh Co', 'Hoang Van Mau'],
               'Ngay sinh':['12/05/2001', '30/08/2003', '14/02/2002'],
               'Gioi tinh':['Nam', 'Nam', 'Nu'],
               'Dia chi':['Thanh Hoa', 'Binh Dinh', 'Dong Thap'],
                'Dien thoai':['0325258', '025478008', '0528475625']}
    inputs = pd.DataFrame.from_dict(datacus, orient="index")
    df = inputs.transpose()
    da = df.to_excel('customer.xlsx')
    print(df)
    sho.config(text=df)
def luu():
    load = pd.read_excel("customer.xlsx")
    datadd =pd.DataFrame.from_dict({"Ma KH":[ent1],
              "TenKH":[ent2],
              "Ngay sinh":[ent3],
              "Gioi tinh":[la5,la6],
              "Dia diem":[ent4],
              "Dien thoai":[ent5]}, orient="index")
    # datadd laf noi chua thong tin moi, ignore_index=True dam bao chi so cua hang duoc reset
    #data = load.append(datadd, ignore_index=True)
    #ad = datadd.transpose()
    add = pd.concat([datadd], ignore_index=True)
    print(add)
    sho.config(text=add)
    #da = ad.to_excel('customer.xlsx')
la1 = Label(win, text="Thong tin khach hang")
# la2 = Label(win, text="Danh sach hoa don")
sho = Label(win, height=10)
lab1 = Label(win, text="Ma KH")
ent1 = Entry(win, width=15)
lab2 = Label(win, text="Tenkh")
ent2 = ttk.Combobox(win, width=20)
ent2["value"] = ["Nguyen Chi Huan", "Tran Cao Trung", "Cao Van Giau"]
lab3 = Label(win, text="Ngay sinh")
ent5 = Spinbox(win, from_=1/1/1970, to=31/12/2040, wrap=True, width=15)
# lab3 = Label(win, text="Ten KH")
# ent3 = ttk.Combobox(win, width=10)
# ent3["value"] = ["Admin", "Manager","Account"]
la3 = Label(win, text="Dia chi")
ent3 = Entry(win, width=15)
la4 = Label(win, text="Dien thoai")
ent4 = Entry(win, width=15)
# lab4 = Label(win, text="Khach hang")
# ent4 = ttk.Combobox(win, width=10)
# ent4["value"] = ["Nguyen Chi Huan", "Tran Cao Trung", "Cao Van Giau"]
la5 = Checkbutton(win, text="Nam", onvalue=1, offvalue=0, variable=check)
la6 = Checkbutton(win, text="Nu", onvalue=1, offvalue=0, variable=check)
btn1 = Button(win, text="Luu", command=hienthi)
btn2 = Button(win, text="Cap nhat", command=luu)
btn3 = Button(win, text="Xoa", command=delt)
btn4 = Button(win, text="Huy", command=win.destroy)
# btn5 = Button(win, text="Thoat")
la1.place(x=5)
# la2.place(x=300)
sho.place(x=300, y=20)
lab1.place(x=5, y=40)
ent1.place(x=80, y=40)
lab2.place(x=5, y=80)
ent2.place(x=80, y=80)
lab3.place(x =5, y=120)
ent5.place(x=80, y=120)
la5.place(x=5, y=160)
la6.place(x=50, y=160)
# lab3.place(x=5, y=60)
# ent3.place(x=80, y=60)
# lab4.place(x=5, y=80)
# ent4.place(x=80, y=80)
la3.place(x=5, y=200)
ent3.place(x= 80, y=200)
la4.place(x= 5, y=240)
ent4.place(x=80, y=240)
btn1.place(x=250, y=240)
btn2.place(x = 300, y=240)
btn3.place(x=370, y=240)
btn4.place(x=410, y=240)
# btn5.place(x=100, y=240)
win.mainloop()