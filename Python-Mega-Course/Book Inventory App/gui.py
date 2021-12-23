"""
A program that stores book information:
Title, Author
Year, ISBN


User can:

View all records
Search an entry
Add an entry
Update an entrey
Delete
Close
"""


from tkinter import Label, Listbox, StringVar, Entry, Scrollbar, Button, Tk, END
import backend


def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    title_entry.delete(0, END)
    title_entry.insert(END, selected_tuple[1])
    author_entry.delete(0, END)
    author_entry.insert(END, selected_tuple[2])
    year_entry.delete(0, END)
    year_entry.insert(END, selected_tuple[3])
    ISBN_entry.delete(0, END)
    ISBN_entry.insert(END, selected_tuple[4])


def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), ISBN_text.get()):
        list1.insert(END, row)


def add_command():
    backend.insert(title_text.get(), author_text.get(),
                   year_text.get(), ISBN_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(),
                 year_text.get(), ISBN_text.get()))


def delete_command():
    backend.delete(selected_tuple[0])


def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(),
                   year_text.get(), ISBN_text.get())


window = Tk()
window.wm_title('BookStore')

"""
Create labels
"""

title_label = Label(window, text='Title')
title_label.grid(row=0, column=0)

author_label = Label(window, text='Author')
author_label.grid(row=0, column=2)

year_label = Label(window, text='Year')
year_label.grid(row=1, column=0)

ISBN_label = Label(window, text='ISBN')
ISBN_label.grid(row=1, column=2)


"""
Create entry widgets
"""

title_text = StringVar()
title_entry = Entry(window, textvariable=title_text)
title_entry.grid(row=0, column=1)

author_text = StringVar()
author_entry = Entry(window, textvariable=author_text)
author_entry.grid(row=0, column=3)

year_text = StringVar()
year_entry = Entry(window, textvariable=year_text)
year_entry.grid(row=1, column=1)

ISBN_text = StringVar()
ISBN_entry = Entry(window, textvariable=ISBN_text)
ISBN_entry.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

scrollbar = Scrollbar(window)
scrollbar.grid(row=2, column=2)

list1.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list1.yview)
list1.bind('<<ListboxSelect>>', get_selected_row)

"""
Create buttons
"""

view_all_button = Button(window, text='View all',
                         width=12, command=view_command)
view_all_button.grid(row=2, column=3)

search_entry_button = Button(
    window, text='Search entry', width=12, command=search_command)
search_entry_button.grid(row=3, column=3)

add_entry_button = Button(window, text='Add entry',
                          width=12, command=add_command)
add_entry_button.grid(row=4, column=3)

update_button = Button(window, text='Update', width=12, command=update_command)
update_button.grid(row=5, column=3)

delete_button = Button(window, text='Delete', width=12, command=delete_command)
delete_button.grid(row=6, column=3)

close_button = Button(window, text='Close', width=12, command=window.destroy)
close_button.grid(row=7, column=3)

window.mainloop()
