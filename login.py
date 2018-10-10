from fangfa import user
from fangfa import question
from tkinter import *
import sys

window=Tk()
window.title("飞天科技")
window.geometry("400x300")
window.geometry("+500+100")

var9=StringVar()
var10=StringVar()
userall={"刘大贵人":"123","李欢":"456","哈哈":"789"}

def denglu():
        if  entry1.get() in userall and  entry2.get()==userall.get(entry1.get()):
            window.destroy()
            root = Tk()
            root.title("飞天趣味知识考试平台")
            root.geometry("1000x750")
            root.geometry("+100+5")

            q1 = question("第一题:买椟还珠这则成语是用来比喻有些人?", "只注重事物外表，不重内涵", 5)
            q2 = question("第二题:神话《白蛇传》中白娘娘盗仙草盗的是?", "灵芝", 10)
            q3 = question("第三题:《西游记》中的火焰山位于?", "新疆", 10)
            q4 = question("第四题:'红娘'是哪部作品中的人物?", "西厢记", 15)
            q5 = question("第五题:'来龙去脉'的成语产生于?", "风水勘探", 5)
            q6 = question("第六题:维纳斯是希腊神话中的?", "爱神和美神", 10)
            q7 = question("第七题:李清照的《如梦令》里的'绿肥红瘦'是描写什么季节的景象?", "晚春", 5)
            q8 = question("第八题:'司空见惯'中的'司空'是指? ", "一种官职", 10)
            q9 = question("第九题:我们常把那些一知半解，却喜欢在人前卖弄的人叫?", "半瓶醋", 15)
            q10 = question("第十题:京剧中，饰演性格活泼、开朗的青年女性的应是?", "花旦", 15)
            qlist = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
            var1 = StringVar()
            var2 = StringVar()
            var3 = StringVar()
            var1.set("欢迎来到趣味知识考试平台!")
            var2.set("沉着冷静,细心作答")

            li = []
            index = 0
            score = 0

            def begin():
                a = qlist[0]
                var1.set(a.timu)
                var2.set("沉着冷静,细心作答")

            def down():
                nonlocal index
                if index < len(qlist) - 1:
                    index += 1
                else:
                    index = 0
                var1.set(qlist[index].timu)
                var2.set("沉着冷静,细心作答")

            def up():
                nonlocal index
                if index < len(qlist) - 1:
                    index -= 1
                else:
                    index = 0
                var1.set(qlist[index].timu)
                var2.set("沉着冷静,细心作答")

            def panduan():
                nonlocal index
                nonlocal score
                var = entry.get()
                if var == qlist[index].answer:
                    score += qlist[index].fenzhi
                    var2.set("恭喜你答案正确!得分为%d" % (qlist[index].fenzhi))
                else:
                    score += 0
                    var2.set("答案错误!得分为%d" % (0))
                    a = qlist[index].timu + "答案为:" + qlist[index].answer
                    if qlist[index].timu not in li:
                        li.append(a)
                var3.set("")

            def chakanfenshu():
                if score >= 90:
                    var1.set("你的总得分为%d,真是优秀!" % (score))
                elif 60 < score < 90:
                    var1.set("你的总得分为%d,继续加油!" % (score))
                else:
                    var1.set("你的总得分为%d,你是猪?" % (score))
                var2.set("欢迎下次继续使用!")

            def wrong():
                var1.set(li)
                var2.set("要仔细分析错题原因哦!")

            def tuichu():
                sys.exit()

            canv1 = Canvas(root, width=1000, height=800, bg="lemonchiffon")
            canv1.pack()
            # my_image=PhotoImage(file="timg.jif")
            # canv1.create_image(1000,800,image=my_image)
            la1 = Label(root, bg="coral", textvariable=var1, font=("blue", 18), wraplength=900, justify="left")
            la1.place(x=10, y=10, width=980, height=300)

            fra = Frame(root, bg="salmon")
            fra.place(x=10, y=320, width=980, height=400)

            #输入答案框
            entry = Entry(fra, bg="navajowhite", textvariable=var3, font=("blue", 18))
            entry.place(x=10, y=10, width=400, height=285)

            la2 = Label(fra, bg="navajowhite", textvariable=var2, font=("blue", 18))
            la2.place(x=570, y=10, width=400, height=350)

            #按钮
            button1 = Button(fra, width=15, height=3, text="开始考试", background="red", font=("宋体", 10), command=begin)
            button1.place(x=430, y=10)
            button2 = Button(fra, width=15, height=3, text="下一题", background="sandybrown", font=("宋体", 10), command=down)
            button2.place(x=430, y=70)
            button3 = Button(fra, width=15, height=3, text="上一题", background="sandybrown", font=("宋体", 10), command=up)
            button3.place(x=430, y=130)
            button4 = Button(fra, width=15, height=3, text="查看分数", background="sandybrown", font=("宋体", 10),
                             command=chakanfenshu)
            button4.place(x=430, y=190)
            button4 = Button(fra, width=15, height=3, text="查看错题", background="sandybrown", font=("宋体", 10), command=wrong)
            button4.place(x=430, y=250)
            button5 = Button(fra, width=15, height=3, text="退出系统", background="sandybrown", font=("宋体", 10),
                             command=tuichu)
            button5.place(x=430, y=310)
            button6= Button(fra, width=15, height=3, text="确认", background="sandybrown", font=("宋体", 10),
                             command=panduan)
            button6.place(x=150, y=310)
            root.mainloop()
        else:
            var9.set("")
            var10.set("")
            window3=Tk()
            window3.title("登陆错误提示!")
            window3.geometry("300x100")
            window3.geometry("+500+100")
            label5=Label(window3,font=("blue",18),width=50,height=3,text="登录失败,请重新输入!",bg="red")
            label5.pack()
            window3.mainloop()

def zhuce():
    if entry1.get()!="" and entry2.get()!="":
        if entry1.get() not in userall.keys() :
            userall[entry1.get()] = entry2.get()
            window4 = Tk()
            window4.title("注册成功提示!")
            window4.geometry("300x100")
            window4.geometry("+500+100")
            label9 = Label(window4, font=("blue", 16), width=50, height=3, text="恭喜你注册成功!",bg="red")
            label9.pack()
            window4.mainloop()
        else:
            var9.set("")
            var10.set("")
            window5 = Tk()
            window5.title("注册失败提示!")
            window5.geometry("500x100")
            window5.geometry("+500+100")
            label8 = Label(window5, font=("blue", 16), width=50, height=3, text="该用户名已存在,请重新完成注册!",bg="red")
            label8.pack()
            window5.mainloop()
    else:
        window6 = Tk()
        window6.title("注册失败提示!")
        window6.geometry("500x100")
        window6.geometry("+500+100")
        label9 = Label(window6, font=("blue", 16), width=50, height=3, text="用户名不能为空!",bg="red")
        label9.pack()
        window6.mainloop()
def tuichu():
    sys.exit()


canvas=Canvas(window,width=400,height=300,bg="peachpuff")
canvas.pack()

label=Label(canvas,width=35,height=1,text="飞天考试平台登录",font=("宋体",18),bg="coral")
label.place(x=1,y=10)

canvas.create_text(70,70,text="用户名:",font=("草书",16),fill="black")
canvas.create_text(70,120,text="密码:",font=("草书",16),fill="black")
#输入用户名
# Canvas.create_text(60,100,text="用户名:",font=("宋体",16))
entry1=Entry(canvas,bg="ivory",font=("宋体",16),textvariable=var9)
entry1.place(x=125,y=60,width=200,height=25)
entry2=Entry(canvas,bg="ivory",font=("宋体",16),textvariable=var10)
entry2.place(x=125,y=110,width=200,height=25)

button1=Button(canvas,width=8,height=1,text="登录",bg="coral",command=denglu)
button1.place(x=60,y=200)

button2=Button(canvas,width=8,height=1,text="注册",bg="coral",command=zhuce)
button2.place(x=160,y=200)

button3=Button(canvas,width=8,height=1,text="退出",bg="coral",command=tuichu)
button3.place(x=260,y=200)
canvas.create_text(200,280,text="版权所有 翻版必究",font=("草书",10),fill="black")
window.mainloop()

