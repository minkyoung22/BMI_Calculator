from tkinter import *
win = Tk()

def bmi():
    weight = float(ent1.get())
    height = float(ent2.get()) * 0.01
    bmi = round(weight / (height ** 2), 2)
    if bmi < 18.5:
        status = "저체중"
    elif 18.5 <= bmi <= 24.9:
        status = "정상체중"
    elif 25 <= bmi <= 29.9:
        status = "과체중"
    else:
        status = "비만"
        
    lab3.configure(text="당신의 bmi는 " + str(bmi) + "입니다.\n" + status +"입니다.")

win.title("BMI 계산기")
win.geometry("400x300")
win.option_add("*Font","맑은고딕 16")

lab0 = Label(win)
lab0.configure(text = "BMI 계산기")
lab0.grid(column=0, row=0, columnspan=3)

#체중 라벨
lab1 = Label(win)
lab1.configure(text = "체중(kg)")
lab1.grid(column=0, row=1)

#체중 입력창
ent1 = Entry(win)
ent1.grid(column=2, row=1)

#키
lab2 = Label(win)
lab2.configure(text = "키(cm)")
lab2.grid(column=0, row=2)

#키 입력창
ent2 = Entry(win)
ent2.grid(column=2, row=2)

#결과
lab3 = Label(win)
lab3.grid(row=4, column=0, padx=5, pady=10, columnspan=3)

#계산버튼
btn = Button(win)
btn.configure(text="계산" ,command=bmi)
btn.grid(row=3, column=0, padx=5, pady=10, columnspan=3)


win.mainloop() #창 실행