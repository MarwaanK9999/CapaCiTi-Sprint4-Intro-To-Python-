import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=445
        height=534
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_801=tk.Button(root)
        GButton_801["bg"] = "#01aaed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_801["font"] = ft
        GButton_801["fg"] = "#000000"
        GButton_801["justify"] = "center"
        GButton_801["text"] = "View Transactions"
        GButton_801.place(x=20,y=70,width=402,height=72)
        GButton_801["command"] = self.GButton_801_command

        GLabel_258=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_258["font"] = ft
        GLabel_258["fg"] = "#333333"
        GLabel_258["justify"] = "center"
        GLabel_258["text"] = "What would you like to do?"
        GLabel_258.place(x=20,y=10,width=403,height=36)

        GButton_979=tk.Button(root)
        GButton_979["bg"] = "#01aaed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_979["font"] = ft
        GButton_979["fg"] = "#000000"
        GButton_979["justify"] = "center"
        GButton_979["text"] = "Balance Enquiry"
        GButton_979.place(x=20,y=160,width=402,height=72)
        GButton_979["command"] = self.GButton_979_command

        GButton_627=tk.Button(root)
        GButton_627["bg"] = "#01aaed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_627["font"] = ft
        GButton_627["fg"] = "#000000"
        GButton_627["justify"] = "center"
        GButton_627["text"] = "Debits"
        GButton_627.place(x=20,y=250,width=402,height=72)
        GButton_627["command"] = self.GButton_627_command

        GButton_67=tk.Button(root)
        GButton_67["bg"] = "#01aaed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_67["font"] = ft
        GButton_67["fg"] = "#000000"
        GButton_67["justify"] = "center"
        GButton_67["text"] = "Credits"
        GButton_67.place(x=20,y=340,width=402,height=72)
        GButton_67["command"] = self.GButton_67_command

        GButton_547=tk.Button(root)
        GButton_547["bg"] = "#01aaed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_547["font"] = ft
        GButton_547["fg"] = "#000000"
        GButton_547["justify"] = "center"
        GButton_547["text"] = "SIgn Out"
        GButton_547.place(x=20,y=430,width=402,height=72)
        GButton_547["command"] = self.GButton_547_command

    def GButton_801_command(self):
        print("command")


    def GButton_979_command(self):
        print("command")


    def GButton_627_command(self):
        print("command")


    def GButton_67_command(self):
        print("command")


    def GButton_547_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
