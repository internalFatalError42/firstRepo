import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD


def drop_inside_list_box(event):
    listb.insert('end', event.data)
    print(event.data)


def drop_inside_textbox(event):
    tbox.delete('1.0', 'end')
    if event.data.endswith(('.txt', '.csv')):
        with open(event.data, 'r') as file:
            for line in file:
                line = line.strip()
                tbox.insert('end', f'{line}\n')


root = TkinterDnD.Tk()
root.geometry('800x500')

listb = tk.Listbox(root, selectmode=tk.SINGLE, background='#1c9cd9')
listb.pack(fill=tk.X)
listb.drop_target_register(DND_FILES)
listb.dnd_bind('<<Drop>>', drop_inside_list_box)

tbox = tk.Text(root)
tbox.pack()
tbox.drop_target_register(DND_FILES)
tbox.dnd_bind('<<Drop>>', drop_inside_textbox)


root.mainloop()
