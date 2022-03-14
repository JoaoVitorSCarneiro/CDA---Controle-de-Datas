"""
Projeto de Controle de Datas Automático

João Vitor Soares Carneiro
"""

import asyncio
import tkinter
import CDATelBot
import CDA
from tkinter import *


window = Tk()


def chamabot():
    asyncio.run(CDATelBot.start(text="La vai bot"))
    pass


def checadata():
    asyncio.run(CDA.__checardata__())
    pass


btn1 = tkinter.Button(window, text="Checagem de Datas", fg='blue', command=checadata)
btn1.config(width=20, height=2)

btn2 = tkinter.Button(window, text="BOT", fg='blue', command=chamabot)
btn2.config(width=10, height=2)

btn1.pack(padx=10, pady=5)
btn2.pack(padx=10, pady=5)

window.title('CDA-Controle de Datas')
window.geometry("300x200+10+20")

window.mainloop()

