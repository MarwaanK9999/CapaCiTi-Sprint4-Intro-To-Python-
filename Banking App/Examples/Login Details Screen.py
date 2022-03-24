import tkinter as tk
import tkinter.font as tkFont


class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width = 722
        height = 251
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_865 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=12)
        GLabel_865["font"] = ft
        GLabel_865["fg"] = "#333333"
        GLabel_865["justify"] = "center"
        GLabel_865["text"] = "Username:"
        GLabel_865.place(x=30, y=70, width=70, height=25)

        GLabel_651 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=12)
        GLabel_651["font"] = ft
        GLabel_651["fg"] = "#333333"
        GLabel_651["justify"] = "center"
        GLabel_651["text"] = "PIN:"
        GLabel_651.place(x=420, y=70, width=70, height=25)

        GLineEdit_634 = tk.Entry(root)
        GLineEdit_634["bg"] = "#ffffff"
        GLineEdit_634["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_634["font"] = ft
        GLineEdit_634["fg"] = "#333333"
        GLineEdit_634["justify"] = "center"
        GLineEdit_634["text"] = ""
        GLineEdit_634.place(x=120, y=60, width=292, height=38)

        GLineEdit_563 = tk.Entry(root)
        GLineEdit_563["bg"] = "#ffffff"
        GLineEdit_563["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_563["font"] = ft
        GLineEdit_563["fg"] = "#333333"
        GLineEdit_563["justify"] = "center"
        GLineEdit_563["text"] = ""
        GLineEdit_563.place(x=480, y=60, width=218, height=38)

        GLabel_330 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=16)
        GLabel_330["font"] = ft
        GLabel_330["fg"] = "#333333"
        GLabel_330["justify"] = "center"
        GLabel_330["text"] = "Enter Login Details"
        GLabel_330.place(x=20, y=10, width=676, height=34)

        GButton_171 = tk.Button(root)
        GButton_171["bg"] = "#01aaed"
        ft = tkFont.Font(family='Times', size=10)
        GButton_171["font"] = ft
        GButton_171["fg"] = "#000000"
        GButton_171["justify"] = "center"
        GButton_171["text"] = "Confirm Details"
        GButton_171.place(x=10, y=180, width=350, height=57)
        GButton_171["command"] = self.GButton_171_command

        GButton_859 = tk.Button(root)
        GButton_859["bg"] = "#01aaed"
        ft = tkFont.Font(family='Times', size=10)
        GButton_859["font"] = ft
        GButton_859["fg"] = "#000000"
        GButton_859["justify"] = "center"
        GButton_859["text"] = "Back"
        GButton_859.place(x=360, y=180, width=350, height=57)
        GButton_859["command"] = self.GButton_859_command

    def GButton_171_command(self):
        print("command")

    def GButton_859_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
