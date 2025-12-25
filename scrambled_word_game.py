#https://replit.com/@miltosgmakris/20251129W

from tkinter import *
from tkinter import messagebox
import random
nwords = ['window', 'python', 'door', 'computer', 'keyboard', 'backyard', 'notebook', 'airplane', 'headphones', 'microphone']
rwords = ['dowwin', 'thonpy', 'rodo', 'putcomer', 'ybdrowek', 'yardback', 'booknote', 'nerplaia', 'phoneshead', 'phoronecim']
i = random.randint(0, len(nwords)-1)
nword = nwords[i]
rword = rwords[i]
def start():
  main_window = Tk()
  main_window.title('Scrambled Words')
  main_window.geometry('500x500')
  main_window.configure(background='#ffff99')
  def check():
    user_word = get_input.get().lower()
    if user_word != nword:
      messagebox.showerror('Wrong!', 'You have to try again...')
      get_input.delete(0, END)
    else:
      messagebox.showinfo('Well done!', 'You found it...')
      main_window.destroy()
  word = Label(
    text=rword,
    bg='#e6ffff',
    font='Titillium 20 bold'
  )
  word.pack(pady=(20,10))
  get_input = Entry(
    font='none 20 bold',
    borderwidth=10,
    justify='center'
  )
  get_input.pack()
  submit = Button(
    text='Submit',
    width=18,
    borderwidth=10,
    command=check
  )
  submit.pack()
  main_window.mainloop()

start()