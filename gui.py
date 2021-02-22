import tkinter
import tkinter.font as font


def from_rgb(rgb):
    return "#%02x%02x%02x" % rgb


def respond(event=None):
    value = "You: "
    value = value + userText.get("1.0", tkinter.END)
    userText.delete('1.0', tkinter.END)
    value = value + "ChatBot: " + "\n"
    chatText.configure(state='normal')
    chatText.insert('end', value)
    chatText.yview_pickplace("end")
    chatText.configure(state='disabled')


# DESIGN

chatWindow = tkinter.Tk()
chatWindow.title("ChatBot")
chatWindow.geometry("700x1000")
chatWindow.configure(bg=from_rgb((19, 155, 124)))

user = tkinter.StringVar()
bot = tkinter.StringVar()

img = tkinter.PhotoImage(file="Resources/logo_nou.png")
tkinter.Label(chatWindow, image=img, bg=from_rgb((19, 155, 124))).grid(row=0, column=0, sticky=tkinter.E)

# MENU BAR - optional
# fileMenu = tkinter.Menu(chatWindow)
# fileMenu.add_command(label='New...')
# fileMenu.add_cascade(label='Save As...')
# fileMenu.add_cascade(label='Exit', command=quit)
#
#
# mainMenu = tkinter.Menu(chatWindow)
# mainMenu.add_cascade(label='File', menu=fileMenu)
# mainMenu.add_command(label='Edit')
# mainMenu.add_command(label='Help')

# chatWindow.config(menu=mainMenu)

# TEXT BOXES

chatText = tkinter.Text(chatWindow, height=25, width=68, bg="white")
chatText.grid(row=1, column=0, sticky=tkinter.W)
chatText.insert('end', "ChatBot: Hello, my name is ChatBot and I will be your assistant.\nHow can I help you?\n")
chatText.configure(state='disabled')

scrollbar_chat = tkinter.Scrollbar(chatWindow, command=chatText.yview)
scrollbar_chat.place(x=679, y=355, height=505)

chatText.configure(yscrollcommand=scrollbar_chat.set)

userText = tkinter.Text(chatWindow, height=6.5, width=48, bg="white")
userText.grid(row=2, column=0, sticky=tkinter.W)
userText.bind('<Return>', respond)

scrollbar_user = tkinter.Scrollbar(chatWindow, command=userText.yview)
scrollbar_user.place(x=484, y=858, height=143)

userText.configure(yscrollcommand=scrollbar_user.set)

myFont = font.Font(family='Courier', size=20, weight='bold')
button = tkinter.Button(chatWindow, text="SEND", command=respond, background=from_rgb((19, 155, 124)),
                        font=myFont)
button.place(x=504, y=858, height=143, width=200)

chatWindow.mainloop()
# from tkinter import *
# from random import choice
#
# ask = ["hi", "hello"]
# hi = ["hi", "hello"]
# sq = ["whatsup", "kya kar rahe ho"]
# rp = ["nothing u say", "kuch nhi ap btao"]
# hr = ["who are you", "what is your name"]
# rh = ["i am a chatbot created by suraj singh"]
# emotion = ["i like you", "i love you"]
# express = ["i like you too"]  # you can add more conversation whatever you like
# error = ["sorry, i don't know", "what u said?", "can't recognise"]
#
# root = Tk()
# user = StringVar()
# bot = StringVar()
#
# root.title("SurajsBot ")
# Label(root, text=" user : ").pack(side=LEFT)
# Entry(root, textvariable=user).pack(side=LEFT)
# Label(root, text=" Bot  : ").pack(side=LEFT)
# Entry(root, textvariable=bot).pack(side=LEFT)
#
#
# def main():
#     question = user.get()
#     if question in ask:
#         bot.set(choice(hi))
#     elif question in sq:
#         bot.set(choice(rp))
#     elif question in hr:
#         bot.set(choice(rh))
#     elif question in emotion:
#         bot.set(choice(express))
#     else:
#         bot.set(choice(error))
#
#
# Button(root, text="speak", command=main).pack(side=LEFT)
#
# mainloop()
