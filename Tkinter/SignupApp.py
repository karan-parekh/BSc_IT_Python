import tkinter as tk


def check_password(event):
    username = username_entry.get()
    password = password_entry.get()
    re_enter = re_enter_entry.get()
    if password != re_enter:
        print("Passwords do not match please try again")
    else:
        print("{} Registered Successfully".format(username))


root = tk.Tk(className="Signup App")

# Main frame
main_frame = tk.Frame(root)
main_frame.pack()

# First Name label
username_label = tk.Label(main_frame, text="Select Username")
username_label.grid(column=0, row=0)

# Password Label
password_label = tk.Label(main_frame, text="Enter Password")
password_label.grid(column=0, row=1)

# Password Label
re_enter_label = tk.Label(main_frame, text="Re-enter Password")
re_enter_label.grid(column=0, row=2)

# Username Entry
username_entry = tk.Entry(main_frame)
username_entry.grid(column=1, row=0)

# Password Entry
password_entry = tk.Entry(main_frame, show="*")
password_entry.grid(column=1, row=1)

# Password Entry
re_enter_entry = tk.Entry(main_frame, show="*")
re_enter_entry.grid(column=1, row=2)

# Signup Button
signup_button = tk.Button(main_frame, text="Signup")
signup_button.bind("<Button-1>", check_password)
signup_button.grid(columnspan=2, row=4)

# Terms and conditions checkbox
terms_and_conditions = tk.Checkbutton(main_frame, text="Agree to Terms and Conditions")
terms_and_conditions.grid(columnspan=2, row=3)

root.mainloop()
