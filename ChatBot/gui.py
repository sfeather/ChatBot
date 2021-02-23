import tkinter
import tkinter.font as font
import speech_rec
import web_search as ws
import warnings
warnings.filterwarnings("ignore")


def from_rgb(rgb):
    return "#%02x%02x%02x" % rgb


def respond(event=None):
    input_string = userText.get("1.0", 'end-1c')
    if input_string[0] == '\n':
        input_string = input_string[1:]
    value = "You: " + input_string + "\n"
    keyword = input_string.split(' ', 1)[0]

    # WEB SEARCH
    response_text = ws.search_on_web(keyword, input_string)

    userText.delete('1.0', tkinter.END)
    value = value + "ChatBot: " + response_text + "\n"
    chatText.configure(state='normal')
    chatText.insert('end', value)
    chatText.yview_pickplace("end")
    chatText.configure(state='disabled')


def speak():
    text = userText.get("1.0", 'end-1c')
    chatText.configure(state='normal')
    # chatText.insert('end', '   --- YOU CAN NOW SPEAK ---\n')
    # chatText.yview_pickplace("end")
    # for Romanian, ro-RO
    # for English, en-US
    input_string = speech_rec.speak_func('en-US', chatText)
    text = text + input_string
    keyword = input_string.split(' ', 1)[0]

    # WEB SEARCH
    response_text = ws.search_on_web(keyword, input_string)

    if input_string == 'Sorry, we could not recognize your voice':
        value = 'ChatBot: Sorry, I could not recognize your voice. Try again or write your message below!\n'
        chatText.insert('end', value)
        chatText.yview_pickplace("end")
        chatText.configure(state='disabled')
        return
    value = "You: " + text + "\n" + "ChatBot: " + response_text + "\n"
    userText.delete('1.0', tkinter.END)
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

chatText = tkinter.Text(chatWindow, height=30, width=84, bg="white")
chatText.grid(row=1, column=0, sticky=tkinter.W)
chatText.insert('end', "ChatBot: Hello, my name is ChatBot and I will be your assistant.\nHow can I help you?\n")
chatText.configure(state='disabled')

scrollbar_chat = tkinter.Scrollbar(chatWindow, command=chatText.yview, width=17)
scrollbar_chat.place(x=679, y=352, height=515)

chatText.configure(yscrollcommand=scrollbar_chat.set)

userText = tkinter.Text(chatWindow, height=7, width=59, bg="white")
userText.grid(row=2, column=0, sticky=tkinter.W)
userText.bind('<Return>', respond)

scrollbar_user = tkinter.Scrollbar(chatWindow, command=userText.yview, width=17)
scrollbar_user.place(x=478, y=868, height=130)

userText.configure(yscrollcommand=scrollbar_user.set)

myFont = font.Font(family='Courier', size=20, weight='bold')
button = tkinter.Button(chatWindow, text="SEND", command=respond, background=from_rgb((19, 155, 124)),
                        font=myFont)
button.place(x=498, y=868, height=135, width=100)

mic_button = tkinter.Button(chatWindow, text="SPEAK", command=speak,
                            background=from_rgb((19, 155, 124)), font=myFont)
mic_button.place(x=597, y=869, height=135, width=100)

chatWindow.mainloop()
