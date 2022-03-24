import tkinter as tk
import tkinter.font as tkFont


class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_999 = tk.Button(root)
        GButton_999["bg"] = "#01aaed"
        GButton_999["borderwidth"] = "4px"
        ft = tkFont.Font(family='Times', size=28)
        GButton_999["font"] = ft
        GButton_999["fg"] = "#000000"
        GButton_999["justify"] = "center"
        GButton_999["text"] = "Register"
        GButton_999.place(x=10, y=280, width=579, height=91)
        GButton_999["command"] = self.GButton_999_command

        GButton_777 = tk.Button(root)
        GButton_777["bg"] = "#01aaed"
        GButton_777["borderwidth"] = "4px"
        ft = tkFont.Font(family='Times', size=28)
        GButton_777["font"] = ft
        GButton_777["fg"] = "#000000"
        GButton_777["justify"] = "center"
        GButton_777["text"] = "Sign In"
        GButton_777.place(x=10, y=380, width=579, height=91)
        GButton_777["command"] = self.GButton_777_command

        GLabel_179 = tk.Label(root)
        GLabel_179["bg"] = "#393d49"
        ft = tkFont.Font(family='Times', size=10)
        GLabel_179["font"] = ft
        GLabel_179["fg"] = "#333333"
        GLabel_179["justify"] = "center"
        GLabel_179["text"] = "label"
        GLabel_179.place(x=10, y=10, width=573, height=156)

        GMessage_450 = tk.Message(root)
        GMessage_450["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times', size=10)
        GMessage_450["font"] = ft
        GMessage_450["fg"] = "#333333"
        GMessage_450["justify"] = "center"
        GMessage_450["text"] = "Welcome to our banking application, making your life easier"
        GMessage_450.place(x=10, y=180, width=572, height=81)

    def GButton_999_command(self):
        print("command")

    def GButton_777_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
