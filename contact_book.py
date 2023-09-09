import tkinter as tk
from tkinter import messagebox

# Create a list to store contacts
contacts = []

# Function to add a contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts.append({'Name': name, 'Phone': phone, 'Email': email, 'Address': address})
        clear_entries()
        update_contact_list()
    else:
        messagebox.showwarning("Warning", "Name and phone number are required.")

# Function to view contacts
def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

# Function to search for contacts
def search_contact():
    query = search_entry.get()
    search_results = [contact for contact in contacts if query.lower() in contact['Name'].lower() or query in contact['Phone']]
    contact_listbox.delete(0, tk.END)
    for result in search_results:
        contact_listbox.insert(tk.END, f"{result['Name']} - {result['Phone']}")

# Function to update a contact
def update_selected_contact():
    selected_index = contact_listbox.curselection()
    if selected_index:
        selected_contact = contacts[selected_index[0]]
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()

        selected_contact['Name'] = name
        selected_contact['Phone'] = phone
        selected_contact['Email'] = email
        selected_contact['Address'] = address

        update_contact_list()
    else:
        messagebox.showwarning("Warning", "Select a contact to update.")

# Function to delete a contact
def delete_selected_contact():
    selected_index = contact_listbox.curselection()
    if selected_index:
        contacts.pop(selected_index[0])
        update_contact_list()
        clear_entries()
    else:
        messagebox.showwarning("Warning", "Select a contact to delete.")

# Function to clear input entries
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Contact Manager")
root.geometry("680x520")

# Create input fields and labels
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

phone_label = tk.Label(root, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

address_label = tk.Label(root, text="Address:")
address_label.pack()
address_entry = tk.Entry(root)
address_entry.pack()

# Create buttons
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack()

search_label = tk.Label(root, text="Search:")
search_label.pack()
search_entry = tk.Entry(root)
search_entry.pack()

search_button = tk.Button(root, text="Search", command=search_contact)
search_button.pack()

update_button = tk.Button(root, text="Update Contact", command=update_selected_contact)
update_button.pack()

delete_button = tk.Button(root, text="Delete Contact", command=delete_selected_contact)
delete_button.pack()

# Create a listbox to display contacts
contact_listbox = tk.Listbox(root)
contact_listbox.pack()

# Populate the listbox with existing contacts
update_contact_list()

# Start the main loop
root.mainloop()