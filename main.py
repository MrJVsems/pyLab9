import tkinter as tk
import re
from tkinter import INSERT

window = tk.Tk()
window.title("Проверка регулярных выражений")

frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_form.pack()

labels = [
    "Регулярное выражение:",
    "Текст:",
]

for idx, text in enumerate(labels):
    label = tk.Label(master=frm_form, text=text)
    label.grid(row=idx, column=0, sticky="e")

entryRegular = tk.Entry(master=frm_form, width=50)
entryRegular.grid(row=0, column=1)

entryText = tk.Entry(master=frm_form, width=50)
entryText.grid(row=1, column=1)


textTk = tk.Text(window)
textTk.pack(side=tk.BOTTOM)


def clear():
    entryRegular.delete(0, len(entryRegular.get()))
    entryText.delete(0, len(entryText.get()))
    textTk.delete("1.0", tk.END)


def check_out():
    textTk.delete("1.0", tk.END)
    if entryRegular.get() == "" or entryText.get() == "":
        textTk.insert(INSERT, "Заполните пожалуйста параметры")
        return
    try:
        re.compile(pattern=fr'{entryRegular.get()}')
    except:
        textTk.insert(INSERT, "Регулярное выражение написано не верно!")
    else:
        regstr = entryRegular.get()
        text = entryText.get()
        if len(re.findall(fr'{regstr}', text)) == 0:
            return
        textTk.insert(INSERT, text)
        for m in re.finditer(fr'{regstr}', text):
            index = m.start()
            readytext = text[:index] + text[index]
            textTk.tag_add(f"{index}_text", f"1.{index}", f"1.{index + len(m[0])}")
            textTk.tag_config(f"{index}_text", background="yellow")


frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

btn_submit = tk.Button(master=frm_buttons, text="Проверить", command=check_out)
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

btn_clear = tk.Button(master=frm_buttons, text="Удалить", command=clear)
btn_clear.pack(side=tk.RIGHT, ipadx=10)

frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

window.mainloop()
