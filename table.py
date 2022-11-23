import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def tableShow(contador,longitud, tiempo):
    root = tk.Tk()
    root.title('Tabla de  datos')
    root.geometry('620x200')

    # define columns
    columns = ('first_name', 'last_name', 'email')

    tree = ttk.Treeview(root, columns=columns, show='headings')

    # define headings
    tree.heading('first_name', text='Numero')
    tree.heading('last_name', text='Cantidad de elementos ')
    tree.heading('email', text='Tiempo de ejecucion')

    # generate sample data
    contacts = []
    for n in range(0, len(contador)-1):
        contacts.append((f'{contador[n]}', f'{longitud[n]}', f'{tiempo[n]}'))

    # add data to the treeview
    for contact in contacts:
        tree.insert('', tk.END, values=contact)


    tree.grid(row=0, column=0, sticky='nsew')

    # add a scrollbar
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

    # run the app
    root.mainloop()