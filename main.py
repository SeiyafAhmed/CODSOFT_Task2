from ttkbootstrap import *
import customtkinter as ctk

root = Window()
root.geometry("330x490")
root.title("Calculator")
root.resizable(False, False)
root.iconbitmap("./logo.ico")

top = Frame(root, style="info", width=290, height=50, padding=2)
top.pack(pady=20)
calc = Text(top, width=17, height=1, font=("dubai medium", 20), blockcursor=True, state="disabled", borderwidth=0, border=0)
calc.pack()

eq = ""

arithmetics = ["÷", "×", "+", "-"]

class CalButton:
    def __init__(self, master, value, color, colspan=1):
        self.value = value
        self.root = master
        width = colspan * 60 + (colspan-1)*10
        self.btn = ctk.CTkButton(self.root, text=value,border_color=color, text_color=color, fg_color="white", hover=False, border_width=3, width=width, height=60, font=("Arial black", 30, "bold"),  command=self.click)
        self.btn.pack(side=LEFT, padx=5, pady=5)

    def click(self):
        global eq
        calc.config(state="normal")

        if self.value.strip() == "AC":
            eq = ""
            calc.delete('1.0', END)

        elif self.value.strip() == "⬅":
            eq = eq[:-1]
            calc.delete('1.0', END)
            calc.insert("end", eq)

        elif self.value.strip() == "=":
            while "×" in eq:
                eq = eq.replace("×", "*")

            while "÷" in eq:
                eq = eq.replace("÷", "/")

            eq = str(eval(eq))
            try:
                if "." in eq:
                    eq = eq[:eq.index(".")+6]
            except:
                pass

            while eq[-1] == "0" and "." in eq:
                eq = eq[:-1]

            if eq[-1] == ".":
                eq = eq[:-1]

            calc.delete('1.0', END)
            calc.insert("end", eq)

        else:
            try:
                if eq[-1] not in arithmetics or self.value not in arithmetics:
                    eq += self.value
                    calc.insert("end", self.value)
                else:
                    eq = eq[:-1]
                    eq += self.value
                    calc.delete('1.0', END)
                    calc.insert("end", eq)

            except:
                eq += self.value
                calc.insert("end", self.value)
        calc.config(state="disabled")

primary = "#4582EC"
danger = "#D9534F"
warning = "#F0AD4E"
info = "#17A2B8"

del_btn = danger
nmbr_btn = primary
artmtc_btn = warning

buttons_data = [
    ["AC", del_btn, 2],
    ["⬅", del_btn, 1],
    ["÷", artmtc_btn, 1],
    ["7", nmbr_btn, 1],
    ["8", nmbr_btn, 1],
    ["9", nmbr_btn, 1],
    ["×", artmtc_btn, 1],
    ["4", nmbr_btn, 1],
    ["5", nmbr_btn, 1],
    ["6", nmbr_btn, 1],
    ["-", artmtc_btn, 1],
    ["1", nmbr_btn, 1],
    ["2", nmbr_btn, 1],
    ["3", nmbr_btn, 1],
    ["+", artmtc_btn, 1],
    ["0", nmbr_btn, 1],
    [".", nmbr_btn, 1],
    ["=", "#02B875", 2]
]

buttons = []
ln = 0
frames = []

for i, button_data in enumerate(buttons_data):
    if ln == 0 or ln == 4:
        frames.append(Frame(root, width=300))
        frames[-1].pack(side=TOP)
        ln = 0

    buttons.append(CalButton(frames[-1], button_data[0], button_data[1], button_data[2]))
    ln += button_data[2]

footer = Frame(root, style="dark",)
footer.pack(side=BOTTOM)
Label(footer, text="©2024 Seiyaf Ahmed ", style="inverse-dark", justify="right",).pack(padx=106)

root.mainloop()
