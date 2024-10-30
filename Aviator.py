import random
import tkinter as tk
from tkinter import messagebox
import time

# Function to simulate the random crash point generation
def aviator_rng():
    return round(random.uniform(1.01, 100.00), 2)

# Function to start the game and animate the plane
def start_game():
    global game_active
    if game_active:
        return  # Prevent starting multiple rounds simultaneously
    game_active = True
    
    crash_point = aviator_rng()
    result_label.config(text="")
    
    # Clear canvas for plane animation
    canvas.delete("all")
    
    # Draw a simple "plane" using shapes
    body = canvas.create_rectangle(50, 90, 130, 110, fill="blue")  # Plane body
    wing_top = canvas.create_rectangle(70, 70, 110, 90, fill="gray")  # Top wing
    wing_bottom = canvas.create_rectangle(70, 110, 110, 130, fill="gray")  # Bottom wing
    cockpit = canvas.create_oval(120, 85, 135, 115, fill="lightblue")  # Cockpit window

    multiplier = 1.00
    
    for i in range(100):
        if multiplier >= crash_point:
            result_label.config(text=f"The plane crashed at: {crash_point}x")
            break
        multiplier = round(multiplier + 0.10, 2)
        canvas.move(body, 5, 0)  # Move plane body
        canvas.move(wing_top, 5, 0)  # Move top wing
        canvas.move(wing_bottom, 5, 0)  # Move bottom wing
        canvas.move(cockpit, 5, 0)  # Move cockpit
        result_label.config(text=f"Multiplier: {multiplier}x")
        canvas.update()
        time.sleep(0.05)  # Reduced delay for smoother movement
    
    # Record the score in the history
    crash_history.append(crash_point)
    update_history()
    
    # Ask to play again
    play_again = messagebox.askquestion("Play Again?", "Do you want to play again?")
    if play_again != 'yes':
        root.quit()
    
    game_active = False

# Function to update the previous crash points display
def update_history():
    history_text.delete(1.0, tk.END)
    history_text.insert(tk.END, "Previous Scores:\n")
    for score in crash_history:
        history_text.insert(tk.END, f"{score}x\n")

# Create the main application window
root = tk.Tk()
root.title("Aviator Game with Basic Plane Animation")
root.geometry("600x400")

# Initialize the game state
crash_history = []
game_active = False

# Create widgets
welcome_label = tk.Label(root, text="Welcome to the Aviator game!", font=("Arial", 16))
welcome_label.pack(pady=10)

# Start Game button
start_button = tk.Button(root, text="Start Game", command=start_game, font=("Arial", 14), bg="green", fg="white")
start_button.pack(pady=10)

# Canvas for plane animation
canvas = tk.Canvas(root, width=500, height=200, bg="lightblue")
canvas.pack(pady=10)

# Label for the result (multiplier or crash point)
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Text widget to display the previous crash points
history_text = tk.Text(root, height=6, width=30)
history_text.pack(pady=10)
history_text.insert(tk.END, "Previous Scores:\n")

# Run the application
root.mainloop()
