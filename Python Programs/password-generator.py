import random
import string
import tkinter as tk

# Generate a random password of length n using the selected character sets
def generate_password(n, use_lowercase, use_uppercase, use_digits):
    choices = ""
    if use_lowercase:
        choices += string.ascii_lowercase
    if use_uppercase:
        choices += string.ascii_uppercase
    if use_digits:
        choices += string.digits

    return ''.join(random.choices(choices, k=n))

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Add a label and entry field to ask the user for the password length
length_label = tk.Label(root, text="Enter password length:")
length_entry = tk.Entry(root)
length_label.pack()
length_entry.pack()

# Add checkboxes for the user to select the character sets to include
lowercase_var = tk.IntVar()
lowercase_checkbox = tk.Checkbutton(root, text="Include lowercase letters", variable=lowercase_var)
lowercase_checkbox.pack()

uppercase_var = tk.IntVar()
uppercase_checkbox = tk.Checkbutton(root, text="Include uppercase letters", variable=uppercase_var)
uppercase_checkbox.pack()

digits_var = tk.IntVar()
digits_checkbox = tk.Checkbutton(root, text="Include digits", variable=digits_var)
digits_checkbox.pack()

# Add a "Generate" button
generate_button = tk.Button(root, text="Generate", command=lambda: generate_callback())
generate_button.pack()

# Add a label to display the generated password
password_label = tk.Label(root, text="")
password_label.pack()

# The generate button callback function
def generate_callback():
    # Get the password length from the entry field
    n = int(length_entry.get())

    # Get the selected character sets from the checkboxes
    use_lowercase = lowercase_var.get()
    use_uppercase = uppercase_var.get()
    use_digits = digits_var.get()

    # Generate a password using the selected character sets
    password = generate_password(n, use_lowercase, use_uppercase, use_digits)

    # Update the password label with the generated password
    password_label.config(text=password)

# Run the main loop
root.mainloop()

