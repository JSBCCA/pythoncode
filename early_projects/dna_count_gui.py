import tkinter

window = tkinter.Tk()

item = tkinter.StringVar()
item.set('')
text = tkinter.Text(window, width=40, height=11)
text.pack(side='top')

frame = tkinter.Frame(window)
frame.pack(side='top')

itemA = tkinter.StringVar()
itemA.set('')

itemT = tkinter.StringVar()
itemT.set('')

itemC = tkinter.StringVar()
itemC.set('')

itemG = tkinter.StringVar()
itemG.set('')


def count():
    dna = text.get('1.0', tkinter.END)
    iA = (dna).count('A')
    itemA.set(iA)
    iT = (dna).count('T')
    itemT.set(iT)
    iC = (dna).count('C')
    itemC.set(iC)
    iG = (dna).count('G')
    itemG.set(iG)


count_button = tkinter.Button(frame, text='Count', command=count)
count_button.pack(side='top')

label = tkinter.Label(frame, text='Num As:')
label.pack(side='left')
label = tkinter.Label(frame, textvariable=itemA)
label.pack(side='left')

label = tkinter.Label(frame, text='Num Ts:')
label.pack(side='left')
label = tkinter.Label(frame, textvariable=itemT)
label.pack(side='left')

label = tkinter.Label(frame, textvariable=itemG)
label.pack(side='right')
label = tkinter.Label(frame, text='Num Gs:')
label.pack(side='right')

label = tkinter.Label(frame, textvariable=itemC)
label.pack(side='right')
label = tkinter.Label(frame, text='Num Cs:')
label.pack(side='right')

window.mainloop()
