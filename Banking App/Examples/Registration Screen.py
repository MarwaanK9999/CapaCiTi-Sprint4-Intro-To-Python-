import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=244
        height=508
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLineEdit_817=tk.Entry(root)
        GLineEdit_817["bg"] = "#ffffff"
        GLineEdit_817["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_817["font"] = ft
        GLineEdit_817["fg"] = "#333333"
        GLineEdit_817["justify"] = "center"
        GLineEdit_817["text"] = ""
        GLineEdit_817.place(x=10,y=90,width=222,height=39)

        GLabel_945=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_945["font"] = ft
        GLabel_945["fg"] = "#333333"
        GLabel_945["justify"] = "left"
        GLabel_945["text"] = "Enter Username:"
        GLabel_945.place(x=10,y=50,width=224,height=30)

        GLineEdit_473=tk.Entry(root)
        GLineEdit_473["bg"] = "#ffffff"
        GLineEdit_473["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_473["font"] = ft
        GLineEdit_473["fg"] = "#333333"
        GLineEdit_473["justify"] = "center"
        GLineEdit_473["text"] = ""
        GLineEdit_473.place(x=10,y=190,width=222,height=39)

        GLabel_297=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_297["font"] = ft
        GLabel_297["fg"] = "#333333"
        GLabel_297["justify"] = "left"
        GLabel_297["text"] = "Enter Starting Balance:"
        GLabel_297.place(x=10,y=150,width=224,height=30)

        GLineEdit_538=tk.Entry(root)
        GLineEdit_538["bg"] = "#ffffff"
        GLineEdit_538["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_538["font"] = ft
        GLineEdit_538["fg"] = "#333333"
        GLineEdit_538["justify"] = "center"
        GLineEdit_538["text"] = ""
        GLineEdit_538.place(x=10,y=290,width=222,height=39)

        GLabel_698=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_698["font"] = ft
        GLabel_698["fg"] = "#333333"
        GLabel_698["justify"] = "left"
        GLabel_698["text"] = "Enter PIN:"
        GLabel_698.place(x=10,y=250,width=224,height=30)

        GButton_809=tk.Button(root)
        GButton_809["bg"] = "#01aaed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_809["font"] = ft
        GButton_809["fg"] = "#000000"
        GButton_809["justify"] = "center"
        GButton_809["text"] = "Confirm Details"
        GButton_809.place(x=10,y=360,width=225,height=48)
        GButton_809["command"] = self.GButton_809_command

        GLabel_306=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_306["font"] = ft
        GLabel_306["fg"] = "#333333"
        GLabel_306["justify"] = "left"
        GLabel_306["text"] = "Enter account Details"
        GLabel_306.place(x=10,y=10,width=224,height=38)

    def GButton_809_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
