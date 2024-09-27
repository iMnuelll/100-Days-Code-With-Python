from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
# Define color constants for the UI
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

# Font settings for the timer
FONT_NAME = "Courier"

# Time intervals (in minutes) for the Pomodoro technique
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Global variables for the number of repetitions and the timer object
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """Resets the timer, stopping any ongoing countdown and resetting the UI."""
    global reps
    
    # Cancel the ongoing timer
    window.after_cancel(timer)
    
    # Reset UI elements
    timer_label.configure(text="Timer", fg="black")
    canvas.itemconfig(timer_text, text="00:00")
    check_label.configure(text="")
    
    # Reset the repetitions count
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """Starts the timer based on the current Pomodoro session (work, short break, or long break)."""
    global reps
    reps += 1  # Increment the session count
    
    # Convert time from minutes to seconds
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    # Determine the type of session (work, short break, or long break) and start countdown
    if reps % 8 == 0:  # Every 8th session is a long break
        count_down(long_break_sec)
        timer_label.configure(text="Long Break", fg=RED)
    elif reps % 2 == 0:  # Every 2nd session is a short break
        count_down(short_break)
        timer_label.configure(text="Short Break", fg=PINK)
    else:  # All other sessions are work sessions
        count_down(work_sec)
        timer_label.configure(text="Work", fg=GREEN)
      
    # For Testing
    if reps % 8 == 0:  # Every 8th session is a long break
        count_down(long_break_sec)
        timer_label.configure(text="Long Break", fg=RED)
    elif reps % 2 == 0:  # Every 2nd session is a short break
        count_down(short_break)
        timer_label.configure(text="Short Break", fg=PINK)
    else:  # All other sessions are work sessions
        count_down(work_sec)
        timer_label.configure(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(time):
    """Handles the countdown mechanism and updates the timer display.
    
    Args:
        time (int): The current time left (in seconds) for the countdown.
    """
    # Calculate minutes and seconds remaining
    count_min = math.floor(time / 60)
    count_sec = time % 60
    
    # Add leading zero to seconds if less than 10
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    # Add leading zero to minutes if less than 10
    if count_min < 10:
        count_min = f"0{count_min}"
    
    # Update the UI with the remaining time
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    
    # Continue counting down or start the next session if time runs out
    if time > 0:
        global timer
        timer = window.after(1000, count_down, time - 1)  # Recursively call the countdown every second
    else:
        # When the countdown reaches zero, start the next session
        start_timer()
        
        # Add a check mark for each completed work session
        if reps % 2 == 0:
            current_text = check_label['text']
            check_label.configure(text=current_text + "✔")

# ---------------------------- UI SETUP ------------------------------- #
# Window setup
window = Tk()
window.title("Pomodoro Clock")  # Set the title of the window
window.config(padx=100, pady=50, bg=YELLOW)  # Set window padding and background color

# Canvas setup for the timer display and tomato image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image_file = PhotoImage(file='tomato.png')  # Load an image of a tomato
canvas.create_image(100, 112, image=image_file)  # Display the tomato image on the canvas
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 12, "bold"))
canvas.grid(column=1, row=1)  # Position the canvas on the grid

# Label for the timer heading
timer_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg="black")
timer_label.grid(column=1, row=0)

# Buttons for starting and resetting the timer
start_button = Button(text="Start", font=(FONT_NAME, 12, "bold"), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 12, "bold"), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Label to display check marks for completed work sessions
check_label = Label(font=(FONT_NAME, 8, "bold"), bg=YELLOW, fg="green")
check_label.grid(column=1, row=3)

# Start the Tkinter main loop to run the application
window.mainloop()