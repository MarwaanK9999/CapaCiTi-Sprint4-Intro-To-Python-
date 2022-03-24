import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=505
        height=182
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_11=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_11["font"] = ft
        GLabel_11["fg"] = "#333333"
        GLabel_11["justify"] = "right"
        GLabel_11["text"] = "Current Available Balance:"
        GLabel_11.place(x=20,y=30,width=259,height=62)

        GMessage_771=tk.Message(root)
        GMessage_771["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=14)
        GMessage_771["font"] = ft
        GMessage_771["fg"] = "#333333"
        GMessage_771["justify"] = "center"
        GMessage_771["text"] = ""
        GMessage_771.place(x=290,y=30,width=185,height=62)

        GButton_683=tk.Button(root)
        GButton_683["bg"] = "#01aaed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_683["font"] = ft
        GButton_683["fg"] = "#000000"
        GButton_683["justify"] = "center"
        GButton_683["text"] = "View Available Balance"
        GButton_683.place(x=10,y=120,width=226,height=52)
        GButton_683["command"] = self.GButton_683_command

        GButton_491=tk.Button(root)
        GButton_491["bg"] = "#01aaed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_491["font"] = ft
        GButton_491["fg"] = "#000000"
        GButton_491["justify"] = "center"
        GButton_491["text"] = "Button"
        GButton_491.place(x=270,y=120,width=226,height=52)
        GButton_491["command"] = self.GButton_491_command

    def GButton_683_command(self):
        print("command")


    def GButton_491_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
