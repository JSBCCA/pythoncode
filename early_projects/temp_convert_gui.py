import tkinter


class Converter:
    """Convert F to C."""

    def __init__(self, parent):
        """Create the GUI."""

        self.parent = parent
        self.frame = tkinter.Frame(parent)
        self.frame.pack()

        self.label = tkinter.Label(self.frame, text='Temperature:')
        self.label.grid(row=0, columnspan=3)

        self.item = tkinter.StringVar()
        self.item.set('')
        self.entry = tkinter.Entry(self.frame, textvariable=self.item)
        self.entry.grid(row=1, columnspan=3)

        self.label = tkinter.Label(self.frame, text='Output:')
        self.label.grid(row=2, column=0)

        self.cel_item = tkinter.StringVar()
        self.cel_item.set('')
        self.label = tkinter.Label(self.frame, textvariable=self.cel_item)
        self.label.grid(row=2, column=1)

        self.switch_button = tkinter.Button(self.frame,
                                            text='To °F',
                                            command=self.convert2)
        self.switch_button.grid(row=3, column=0)

        self.convert_button = tkinter.Button(self.frame,
                                             text='To °C',
                                             command=self.convert)
        self.convert_button.grid(row=3, column=1)

        self.quit_button = tkinter.Button(self.frame,
                                          text='Quit',
                                          command=self.quit_click)
        self.quit_button.grid(row=3, column=2)

    def celsius_conv(self, f):
        """Takes a temperature in degF and converts to degC."""
        if f == 0:
            return -17.7778
        else:
            return (f - 32.0) * (5.0 / 9.0)

    def fahren_conv(self, c):
        """Takes a temp in degC and converts to degF."""
        if c == 0:
            return 32
        else:
            return c * (9.0 / 5.0) + 32

    def convert(self):
        try:
            c = self.celsius_conv(float(self.item.get()))
            self.cel_item.set(c)
        except ValueError:
            self.cel_item.set('Type a number!')

    def convert2(self):
        try:
            f = self.fahren_conv(float(self.item.get()))
            self.cel_item.set(f)
        except ValueError:
            self.cel_item.set('Type a number!')

    def quit_click(self):
        """Handle click on 'quit' button."""

        self.parent.destroy()


if __name__ == '__main__':

    root = tkinter.Tk()
    conv = Converter(root)

    tkinter.mainloop()
