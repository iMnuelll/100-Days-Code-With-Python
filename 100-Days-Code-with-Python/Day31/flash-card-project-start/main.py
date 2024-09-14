from tkinter import *
import pandas as pd
import random

# Constants for the application
BACKGROUND_COLOR = "#B1DDC6"  # Background color for the window
NATION_FONT = ("Arial", 40, "italic")  # Font for displaying the language (e.g., "French")
WORD_FONT = ("Arial", 60, "bold")  # Font for displaying the word
random_words = {}  # This will hold the current word pair (French and English)

# ---------------------------------------------------------------- READ THE DATA ----------------------------------------------------------------
# Read the CSV file containing French and English words
# Convert the data into a list of dictionaries, where each dictionary represents a word pair
data = pd.read_csv("data/french_words.csv")
new_data = data.to_dict(orient="records")

# ---------------------------------------------------------------- Button Functions ----------------------------------------------------------------
def next_card():
  """
  Display the next random flashcard with a French word.
  This function will:
  - Cancel the flip timer (if one is running).
  - Pick a random word from the dataset (new_data).
  - Update the canvas to display the front of the card with the French word.
  - Start a new timer to automatically flip the card after 3 seconds.
  """
  global random_words, flip_timer
  window.after_cancel(flip_timer)  # Cancel any existing timer
  random_words = random.choice(new_data)  # Choose a random word
  card_canvas.itemconfig(canvas_image, image=card_front)  # Show the front of the card
  card_canvas.itemconfig(title, text="French", fill="black")  # Update the title to "French"
  card_canvas.itemconfig(words, text=random_words["French"], fill="black")  # Show the French word
  flip_timer = window.after(3000, flip_card)  # Flip the card after 3 seconds

def flip_card():
  """
  Flip the flashcard to show the English translation.
  This function will update the canvas to:
  - Display the back of the card.
  - Show the English translation of the French word.
  - Change the text color to white for better visibility.
  """
  card_canvas.itemconfig(canvas_image, image=card_back)  # Show the back of the card
  card_canvas.itemconfig(title, text="English", fill="white")  # Update the title to "English"
  card_canvas.itemconfig(words, text=random_words["English"], fill="white")  # Show the English word

def is_known():
  """
  Handle the event when the user knows the word (i.e., clicks the right button).
  This function will:
  - Remove the current word from the dataset (new_data).
  - Save the updated dataset to a new CSV file (word_to_learn.csv).
  - Move to the next flashcard by calling the next_card function.
  """
  global new_data
  new_data.remove(random_words)  # Remove the current word from the list
  # Save the updated list to a CSV file for future learning
  updated_data = pd.DataFrame(new_data)
  updated_data.to_csv("data/word_to_learn.csv", index=False)
  next_card()  # Show the next card

# ---------------------------------------------------------------- UI SETUP ----------------------------------------------------------------
# Create the main window for the flashcard application
window = Tk()
window.title("Flash Card")  # Set the window title
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)  # Set padding and background color

# Initialize the timer to flip the card after 3 seconds
flip_timer = window.after(3000, flip_card)

# ---------------------------------------------------------------- Image Setup ----------------------------------------------------------------
# Load the images for the buttons and flashcards
right_image = PhotoImage(file="images/right.png")  # Image for the "right" button (known word)
wrong_image = PhotoImage(file="images/wrong.png")  # Image for the "wrong" button (unknown word)
card_front = PhotoImage(file="images/card_front.png")  # Image for the front of the flashcard
card_back = PhotoImage(file="images/card_back.png")  # Image for the back of the flashcard

# ---------------------------------------------------------------- Canvas Setup ----------------------------------------------------------------
# Create the canvas where the flashcards will be displayed
card_canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, bd=0, highlightthickness=0)
canvas_image = card_canvas.create_image(400, 263, image=card_front)  # Display the front of the card initially
card_canvas.grid(column=0, row=0, columnspan=2, padx=50, pady=50)  # Position the canvas in the grid

# ---------------------------------------------------------------- Button Setup ----------------------------------------------------------------
# Create the right and wrong buttons and link them to their respective functions
right_button = Button(image=right_image, bd=0, highlightthickness=0, command=is_known)  # Right button (known word)
right_button.grid(column=1, row=1, padx=50, pady=25)

wrong_button = Button(image=wrong_image, bd=0, highlightthickness=0, command=next_card)  # Wrong button (unknown word)
wrong_button.grid(column=0, row=1, padx=50, pady=25)

# ---------------------------------------------------------------- Text Setup ----------------------------------------------------------------
# Create text elements for the title (language name) and the word
title = card_canvas.create_text(400, 150, text="", font=NATION_FONT)  # Position the title (e.g., "French" or "English")
words = card_canvas.create_text(400, 263, text="", font=WORD_FONT)  # Position the word (French or English)

# Show the first flashcard when the application starts
next_card()

# Start the Tkinter event loop
window.mainloop()
