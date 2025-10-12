from tkinter import *

def inserir(campo,texto):
    campo.insert(END,texto)
def deletar(campo):
    campo.delete(len(campo.get())-1)
def deletarTudo(campo):
    campo.delete(0,END)
def resultado(campo):
    r = eval(campo.get())
    deletarTudo(campo)
    campo.insert(0,r)
def raiz(campo):
    r = float(campo.get())**0.5
    deletarTudo(campo)
    campo.insert(0,r)


calculadora = Tk()
calculadora.title("Calculadora")
calculadora.geometry("300x350")

telinha = Entry(calculadora,width=20,font=("Verdana",15))
telinha.pack(pady=40)

div1 = Frame(calculadora,width=250,height=20,bg="blue")
div1.pack(pady=(0,10))

bt7 = Button(div1,width=7,text=7,command=lambda:inserir(telinha,"7"))
bt7.pack(side="left")
bt8 = Button(div1,width=7,text=8,command=lambda:inserir(telinha,"8"))
bt8.pack(side="left")
bt9 = Button(div1,width=7,text=9,command=lambda:inserir(telinha,"9"))
bt9.pack(side="left")
btd = Button(div1,width=7,text="/",command=lambda:inserir(telinha,"/"))
btd.pack(side="left")

div2 = Frame(calculadora,width=250,height=20,bg="blue")
div2.pack(pady=(0,10))

bt4 = Button(div2,width=7,text=4,command=lambda:inserir(telinha,"4"))
bt4.pack(side="left")
bt5 = Button(div2,width=7,text=5,command=lambda:inserir(telinha,"5"))
bt5.pack(side="left")
bt6 = Button(div2,width=7,text=6,command=lambda:inserir(telinha,"6"))
bt6.pack(side="left")
btm = Button(div2,width=7,text="*",command=lambda:inserir(telinha,"*"))
btm.pack(side="left")

div3 = Frame(calculadora,width=250,height=20,bg="blue")
div3.pack(pady=(0,10))

bt1 = Button(div3,width=7,text=1,command=lambda:inserir(telinha,"1"))
bt1.pack(side="left")
bt2 = Button(div3,width=7,text=2,command=lambda:inserir(telinha,"2"))
bt2.pack(side="left")
bt3 = Button(div3,width=7,text=3,command=lambda:inserir(telinha,"3"))
bt3.pack(side="left")
bta = Button(div3,width=7,text="+",command=lambda:inserir(telinha,"+"))
bta.pack(side="left")

div4 = Frame(calculadora,width=250,height=20,bg="blue")
div4.pack(pady=(0,10))

btap = Button(div4,width=7,text="↩",command=lambda:deletar(telinha))
btap.pack(side="left")
bt0 = Button(div4,width=7,text=0,command=lambda:inserir(telinha,"0"))
bt0.pack(side="left")
btp = Button(div4,width=7,text=".",command=lambda:inserir(telinha,"."))
btp.pack(side="left")
bts = Button(div4,width=7,text="-",command=lambda:inserir(telinha,"-"))
bts.pack(side="left")

div5 = Frame(calculadora,width=250,height=20,bg="blue")
div5.pack(pady=(0,10))

btc = Button(div5,width=7,text="C",command=lambda:deletarTudo(telinha))
btc.pack(side="left")
bti = Button(div5,width=7,text="=",command=lambda:resultado(telinha))
bti.pack(side="left")
btpi = Button(div5,width=7,text="π",command=lambda:inserir(telinha,"3.14"))
btpi.pack(side="left")
btr = Button(div5,width=7,text="√",command=lambda:raiz(telinha))
btr.pack(side="left")
calculadora.mainloop()