import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=603
        height=510
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GListBox_914=tk.Listbox(root)
        GListBox_914["bg"] = "#ffffff"
        GListBox_914["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_914["font"] = ft
        GListBox_914["fg"] = "#333333"
        GListBox_914["justify"] = "center"
        GListBox_914.place(x=20,y=20,width=560,height=391)

        GButton_819=tk.Button(root)
        GButton_819["bg"] = "#01aaed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_819["font"] = ft
        GButton_819["fg"] = "#000000"
        GButton_819["justify"] = "center"
        GButton_819["text"] = "View Transactions"
        GButton_819.place(x=20,y=430,width=262,height=61)
        GButton_819["command"] = self.GButton_819_command

        GButton_698=tk.Button(root)
        GButton_698["bg"] = "#01aaed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_698["font"] = ft
        GButton_698["fg"] = "#000000"
        GButton_698["justify"] = "center"
        GButton_698["text"] = "Back"
        GButton_698.place(x=320,y=430,width=262,height=61)
        GButton_698["command"] = self.GButton_698_command

    def GButton_819_command(self):
        print("command")


    def GButton_698_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
