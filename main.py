from tkinter import *
import pyperclip

characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '&', "'", '@', ')', '(',
              ':', ',', '=', '!', '.', '-', '×', '%', '+', '"', '?', '/']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
         '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---',
         '...--', '....-', '.....', '-....', '--...', '---..', '----.', '.-...', '.----.', '.--.-.', '-.--.-', '-.--.',
         '---...', '--..--', '-...-', '-.-.--', '.-.-.-', '-....-', '-..-', '.-.-.', '.-..-.', '..--..', '-..-.',
         '.--.-']
direction = 'e'


def encode():
    text = text_input.get(1.0, "end-1c").upper()
    res = []
    for char in text:
        if char == ' ':
            res.append("/ ")
        else:
            res.append(f"{morse[characters.index(char)]} ")
    result = ''.join(res)
    text_output.grid(column=0, row=6, columnspan=3)
    copy.grid(column=2, row=7, pady=20)
    text_output.delete(1.0, "end")
    text_output.insert(1.0, result)


def decode():
    code = text_input.get(1.0, "end-1c").split(' ')
    res = []
    for char in code:
        if char == '/':
            res.append(' ')
        elif char == '':
            continue
        elif char not in morse:
            error.grid(column=0, row=4, columnspan=3, padx=50)
        else:
            error.grid_forget()
            res.append(characters[morse.index(char)])
    result = ''.join(res)
    text_output.grid(column=0, row=6, columnspan=3)
    copy.grid(column=2, row=7, pady=20)
    text_output.delete(1.0, "end")
    text_output.insert(1.0, result.title())


def switch():
    global direction
    error.grid_forget()
    if direction == 'e':
        title.config(text="Morse to Text.")
        switch_button.config(text="Text to Morse")
        direction = 'd'
    else:
        title.config(text="Text to Morse.")
        switch_button.config(text="Morse to Text")
        direction = 'e'


def convert():
    global direction
    if direction == 'd':
        decode()
    else:
        encode()


def copy_to_clipboard():
    pyperclip.copy(text_output.get(1.0, "end-1c"))


window = Tk()
window.title("Morse translator")
window.minsize(600, 400)
window.config(padx=50, pady=20)

title = Label(window, text="Text to Morse.", fg="green", font=("Helvetica", 32))
title.grid(column=1, row=0)

switch_button = Button(text="Morse to Text", command=switch, fg="green", font=("Helvetica", 12), padx=5)
switch_button.grid(column=1, row=1, pady=20)

input_label = Label(text="Enter your text:", pady=5)
input_label.grid(column=0, row=2)

text_input = Text(width=60, height=8, padx=10, pady=10)
text_input.grid(column=0, row=3, columnspan=3)

error = Label(text="Please type only morse code.", fg="red")

convert = Button(text="Convert", width=14, command=convert, font=("Helvetica", 12))
convert.grid(column=2, row=5, pady=20)

text_output = Text(width=60, height=8, padx=10, pady=10)

copy = Button(text="Copy to clipboard", command=copy_to_clipboard, font=("Helvetica", 12))


window.mainloop()
