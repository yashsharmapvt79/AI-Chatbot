import tkinter as tk
import webbrowser as wb
from tkinter import messagebox
from customtkinter import *
from PIL import Image
import main



# Import the main module
# Login.py
# Your existing code for Login.py# Import main.py
# Define the initial username and password
INITIAL_USERNAME = "yash"
INITIAL_PASSWORD = "yash"

def authenticate(username, password):
    return username == INITIAL_USERNAME and password == INITIAL_PASSWORD
def signup_clicked():
    # Open the HTML file in the default web browser
    wb.open("h.html")
def forgot_password():
    def send_reset_instructions():
        email = email_entry.get()
        if not email:
            messagebox.showerror("Invalid Email", "Please enter your email address.")
            return
        # Implement your logic to send reset instructions to the user's email
        messagebox.showinfo("Reset Instructions Sent", "Instructions to reset your password have been sent to your email.")

    forgot_password_window = tk.Toplevel()
    forgot_password_window.title("Forgot Password")
    forgot_password_window.geometry("400x150")
    
    email_label = CTkLabel(master=forgot_password_window, text="Enter your email:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 12))
    email_label.pack(anchor="w", padx=10, pady=10)

    email_entry = CTkEntry(master=forgot_password_window, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
    email_entry.pack(anchor="w", padx=10, fill="x")

    send_button = CTkButton(master=forgot_password_window, text="Send Reset Instructions", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", command=send_reset_instructions)
    send_button.pack(anchor="center", pady=10)


def login():
    def login_clicked():
        username = username_entry.get()
        password = password_entry.get()
        if authenticate(username, password):
            messagebox.showinfo("Success", "Login successful!")
            login_window.destroy()
            main.main_application()  # Open the main application
        else:
            messagebox.showerror("Error", "Incorrect username or password!")

    app = CTk()
    app.geometry("600x480")
    app.resizable(0,0)
    
    side_img_data = Image.open("side-img.png")
    email_icon_data = Image.open("email-icon.png")
    password_icon_data = Image.open("password-icon.png")

    side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 480))
    email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20,20))
    password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17,17))
    
    CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left")

    frame = CTkFrame(master=app, width=300, height=480, fg_color="#ffffff")
    frame.pack_propagate(0)
    frame.pack(expand=True, side="right")

    CTkLabel(master=frame, text="Welcome Back!", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
    CTkLabel(master=frame, text="Sign in to your account", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

    CTkLabel(master=frame, text="  Username :", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
    username_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
    username_entry.pack(anchor="w", padx=(25, 0))

    CTkLabel(master=frame, text="  Password:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
    password_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*")
    password_entry.pack(anchor="w", padx=(25, 0))

    CTkButton(master=frame, text="Login", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225, command=login_clicked).pack(anchor="w", pady=(40, 0), padx=(25, 0))
    CTkButton(master=frame, text="Sign Up", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225, command=signup_clicked).pack(anchor="w", pady=(10, 0), padx=(25, 0))
    forgot_password_button = CTkButton(master=frame, text="Forgot Password?", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225, command=forgot_password)
    forgot_password_button.pack(anchor="w", pady=(10, 0), padx=(25, 0))

    app.mainloop()

login()
if __name__ == "__main__":
    main.main_application()  # Execute main_application from main.py if Login.py is run directly

