import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        
        self.contacts = []
        
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()
        
        self.phone_label = tk.Label(root, text="Number:")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(root)
        self.phone_entry.pack()
        
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.pack()
        
        self.contact_listbox = tk.Listbox(root)
        self.contact_listbox.pack()
        
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack()
        
        self.load_button = tk.Button(root, text="Load Contacts", command=self.load_contacts)
        self.load_button.pack()
        
        self.save_button = tk.Button(root, text="Save Contacts", command=self.save_contacts)
        self.save_button.pack()
        
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name and phone:
            self.contacts.append((name, phone))
            self.contact_listbox.insert(tk.END, f"{name}: {phone}")
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter both name and phone.")
    
    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.contact_listbox.delete(index)
            del self.contacts[index[0]]
    
    def load_contacts(self):
        try:
            with open("contacts.txt", "r") as file:
                self.contacts = [line.strip().split(":") for line in file]
                self.contact_listbox.delete(0, tk.END)
                for contact in self.contacts:
                    self.contact_listbox.insert(tk.END, f"{contact[0]}: {contact[1]}")
        except FileNotFoundError:
            messagebox.showerror("Error", "File 'contacts.txt' not found.")
    
    def save_contacts(self):
        with open("contacts.txt", "w") as file:
            for contact in self.contacts:
                file.write(f"{contact[0]}:{contact[1]}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
