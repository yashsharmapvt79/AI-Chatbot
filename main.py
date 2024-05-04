from Login import *
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from PIL import Image, ImageTk, ImageSequence
import datetime
import pyttsx3
import wikipedia
import webbrowser as wb

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Function to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to load password
PASSWORD_FILE = "passwords.txt"
def load_password():
    try:
        with open(PASSWORD_FILE, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

# Function to save password
def save_password(password):
    with open(PASSWORD_FILE, "w") as file:
        file.write(password)

# Function to change password
def change_password():
    speak("Please enter your current password:")
    current_password = simpledialog.askstring("Change Password", "Enter Current Password", show='*')
    print("Current Password:", current_password)  # Debugging
    saved_password = load_password()
    print("Saved Password:", saved_password)  # Debugging

    if current_password == saved_password:
        new_password = simpledialog.askstring("Change Password", "Enter New Password", show='*')
        if new_password:
            speak("Password changed successfully!")
            save_password(new_password)
    else:
        speak("Incorrect password! Please try again.")

def wishme():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak('Good Morning Team!')
    elif 12 <= hour < 18:
        speak('Good Afternoon Team!')
    else:
        speak('Good Evening Team!')

def perform_task():
    # Perform the task associated with the command
    command = command_entry.get().lower()

    if 'change password' in command:
        new_password = change_password()
        if new_password:
            command_entry.delete(0, tk.END)
            command_entry.insert(0, new_password)
        else:
            speak('Sorry, I didn\'t understand that command.')
    if 'exit' in command:
        speak('Exiting program.')
        main_window.destroy()
    else:
        if 'wikipedia' in command:
            speak('Enter Your Query !!')
            query = command_entry.get()
            print(wikipedia.search(query))
        elif 'music' in command:
            speak('Tell Me Of which language or song you wanna listen ')
            language_or_song = command_entry.get()
            speak('Opening Music results related to ' + language_or_song)
            wb.open('https://open.spotify.com/search/' + language_or_song)
        elif 'youtube' in command:
            speak('Type the Result you want from Youtube')
            pe = simpledialog.askstring("Youtube search", "Enter Result (leave empty for main page):")
            if not pe:
               speak("Ok, opening Youtube")
               wb.open('https://www.youtube.com/')
            else:
               speak("OK, opening regarding " + pe)
               wb.open('https://www.youtube.com/results?search_query=' + pe)
        elif 'instagram' in command:
          speak('OK, opening Instagram.')
          speak('Any specific profile?')
          profile_name = simpledialog.askstring("Instagram Profile", "Enter profile name (leave empty for main page):")
          if not profile_name:
              speak("Ok, opening Instagram.")
              wb.open('https://www.instagram.com/')
          else:
              speak("OK, opening regarding " + profile_name)
              wb.open('https://www.instagram.com/' + profile_name)
        elif 'twitter' in command:
            speak('OK, opening Twitter.')
            wb.open('https://www.twitter.com/')
        elif 'whatsapp' in command:
            speak('Let\'s see some WhatsApp messages.')
            wb.open('https://web.whatsapp.com/')
        elif 'amazon' in command:
            speak('What do you want to search for on Amazon?')
            search_item = command_entry.get()
            wb.open('https://www.amazon.in/s?k=' + search_item)
        elif 'flipkart' in command:
            speak('What do you want to search for on Flipkart?')
            search_item = command_entry.get()
            wb.open('https://www.flipkart.com/search?q=' + search_item)
        elif 'zomato' in command:
            speak('Opening Zomato.')
            wb.open('https://www.zomato.com/')
        else:
            speak('Sorry, I didn\'t understand that command.')

# Function to clear search bar
def clear_search_bar():
    command_entry.delete(0, tk.END)

# Function to process command
def process_command():
    command_entry.config(state=tk.DISABLED)
    perform_task()
    clear_search_bar()
    command_entry.config(state=tk.NORMAL)

def main():
    global main_window
    main_window = tk.Tk()
    main_window.title("AI Chatbot")
    main_window.geometry("600x400")

    # Menu Bar
    menubar = tk.Menu(main_window)
    main_window.config(menu=menubar)
    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Exit", command=main_window.quit)

    # Load Background Image
    background_image = Image.open("g.gif")
    background_image = background_image.resize((600, 400))
    gif_path = "g.gif"
    gif = Image.open(gif_path)
    frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif)]
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(master=main_window, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    def update_frame(idx=0):
        background_label.configure(image=frames[idx])
        main_window.after(50, update_frame, (idx + 1) % len(frames))

    update_frame()

    wishme()
    speak('Welcome everyone!')
    speak('Enter your commands for me!')

    # Style for buttons
    style = ttk.Style()
    style.configure("Custom.TButton", foreground="#800080", background="white")

    # Command Label
    command_label = ttk.Label(main_window, text="Command:", font="Arial",background="#800080")
    command_label.place(x=50, y=350)

    # Command Entry
    global command_entry
    command_entry = ttk.Entry(main_window, width=50)
    command_entry.place(x=150, y=350)

    # Send Button
    command_button = ttk.Button(main_window, text="Send", command=process_command, style="Custom.TButton")
    command_button.place(x=500, y=350)
    password_button = tk.Button(main_window, text="Change Password", command=change_password)
    password_button.place(x=400, y=350)
    main_window.mainloop()

main()
