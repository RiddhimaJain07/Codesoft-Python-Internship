import tkinter as tk
from tkinter import messagebox

contacts = {}

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts[name] = [phone, email, address]
        update_list()
        messagebox.showinfo("Success", "Contact Added Successfully")

def update_list():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name} - {details[0]}")

def delete_contact():
    selected = contact_list.curselection()
    if selected:
        item = contact_list.get(selected)
        name = item.split(" - ")[0]
        del contacts[name]
        update_list()

def search_contact():
    keyword = search_entry.get().lower()
    contact_list.delete(0, tk.END)

    for name, details in contacts.items():
        if keyword in name.lower() or keyword in details[0]:
            contact_list.insert(tk.END, f"{name} - {details[0]}")

def update_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name in contacts:
        contacts[name] = [phone, email, address]
        update_list()
        messagebox.showinfo("Success", "Contact Updated Successfully")
    else:
        messagebox.showerror("Error", "Contact Not Found")            

root = tk.Tk()
root.title("Contact Management System")
root.geometry("500x400")

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Address").pack()
address_entry = tk.Entry(root)
address_entry.pack()

tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)

tk.Label(root, text="Search by Name or Phone").pack()
search_entry = tk.Entry(root)
search_entry.pack()

tk.Button(root, text="Search", command=search_contact).pack(pady=5)

contact_list = tk.Listbox(root, width=50)
contact_list.pack(pady=10)

root.mainloop()