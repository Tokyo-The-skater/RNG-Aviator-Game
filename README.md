# RNG-Aviator-Game
This is a simple code exploring a random number generator using the aviator look alike game

Overview:
This project was created to explore and better understand how random number generators (RNGs) work. The Aviator game simulates a scenario where a random "crash point" is generated during gameplay, and the player's goal is to see how far the plane flies before it crashes. The crash point is generated randomly, mimicking the unpredictability of real-world RNGs used in games and other applications.


Purpose:
The main purpose of this project was to gain hands-on experience with random number generation, particularly within the context of a game. By creating a simple UI and incorporating RNG, I wanted to deepen my understanding of how random values are used in simulations, gaming mechanics, and decision-making algorithms.

Key Learning Objectives:
Explore how random numbers can influence game mechanics.
Learn how to generate random numbers using Python's random library.
Understand how to integrate random numbers into a graphical user interface (GUI).
Develop animations and dynamic visuals for a better user experience.
How It Works:
The game starts by generating a random crash point using Python's random.uniform() function. This crash point ranges between 1.01 and 100.00, simulating the unpredictability of real-life RNG events.
The plane "flies" across the screen, and the multiplier increases as time progresses.
If the multiplier reaches the randomly generated crash point, the plane "crashes," and the game ends.
The player's previous scores (crash points) are displayed, helping track performance over time.
Technologies Used
Python: The core logic, including random number generation, is written in Python.
Tkinter: Used for creating the graphical user interface (GUI) and animations.
PIL (Python Imaging Library): Optionally used to load images for a more realistic plane animation (not required in the basic version).
