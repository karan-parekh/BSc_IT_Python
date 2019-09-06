import tkinter as tk


def print_message():
	username = username_entry.get()
	my_message = tk.Message(root, text="User {} has successfully logged in".format(username))
	my_message.grid(columnspan=2, row=3)


root = tk.Tk(className="Login App")

# Main frame
main_frame = tk.Frame(root)
main_frame.pack()

# # First Name label
# first_name = tk.Label(main_frame, text="Enter First Name")
# first_name.grid(column=0, row=0)
#
# # Last Name label
# last_name = tk.Label(main_frame, text="Enter Last Name")
# last_name.grid(column=1, row=0)

# Username Label
username_label = tk.Label(main_frame, text="Username")
username_label.grid(column=0, row=0)

# Password Label
password_label = tk.Label(main_frame, text="Password")
password_label.grid(column=0, row=1)

# Username Entry
username_entry = tk.Entry(main_frame)
username_entry.grid(column=1, row=0)

# Password Entry
password_entry = tk.Entry(main_frame, show="*")
password_entry.grid(column=1, row=1)

# Login Button
login_button = tk.Button(main_frame, text="Login", command=print_message)
login_button.grid(columnspan=2, row=3)

# Keep me logged in checkbox
logged_in_checkbox = tk.Checkbutton(main_frame, text="Keep me Logged in")
logged_in_checkbox.grid(columnspan=2, row=2)

root.mainloop()
