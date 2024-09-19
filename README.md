# **Number Guessing Game**

A fun Python-based number guessing game where the player tries to guess a randomly generated number within a specified range and a limited number of attempts. The game allows users to configure the number of attempts and the range of numbers, providing feedback after each guess.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)

## Project Overview

In this Number Guessing Game, the player must guess a randomly generated number within a user-defined range. Players can also specify the maximum number of attempts they are allowed. After each guess, the game will tell the player if their guess is too high or too low. The player wins by guessing the correct number within the allowed attempts or loses if they run out of guesses.

## Features
* **Customizable Range**: Players can specify a range of numbers to guess from.
* **Adjustable Number of Attempts**: Players can set the maximum number of guesses allowed.
* **Input Validation**: Handles invalid input (e.g., non-numeric values, out-of-range guesses).
* **Replayability**: Option to play again after the game ends.
* **Exit Option**: Players can quit the game at any time by entering 'q'.

## Installation
1. Clone the repository:

       git clone https://github.com/your-username/number-guessing-game.git
    
       cd number-guessing-game

3. Ensure Python 3.x is installed on your machine. No additional libraries are required.

## Usage
To run the game, simply execute the following command in your terminal:

    python number_guessing_game.py

Gameplay:

1. The game will prompt you to input how many guesses (attempts) you would like.
2. You will then be asked to define the minimum and maximum range for the random number.
3. The game will generate a random number within the specified range, and you'll try to guess it.
4. After each guess, the game will tell you if your guess is too high or too low.
5. If you guess the correct number within the allowed attempts, you win! If not, the game will reveal the correct answer after you run out of guesses.
6. You can play again or exit the game by following the prompts.

Example:

    How many guesses would you like? (Enter 'q' to quit) 5
    Please enter the minimum number: 1
    Please enter the maximum number: 100
    Attempts remaining: 5
    Please enter a guess between 1 and 100 (or 'q' to quit): 50
    Too low, try again.
    Attempts remaining: 4
    Please enter a guess between 1 and 100 (or 'q' to quit): 75
    Too high, try again.
    ...
    CORRECT, the answer was

## Contributing

Contributions are welcome! If you'd like to contribute to this guessing game project, please follow these steps:

1. Fork the repository: Click on the "Fork" button at the top right of this page to create your own copy of the repository.
2. Clone the repository: Clone your fork to your local machine using:

       git clone https://github.com/your-username/guessing-game.git
3. Create a new branch: Create a new branch for your feature or bugfix:

       git checkout -b feature-or-bugfix-name

4. Make your changes: Implement your feature or fix the bug. Make sure to test your changes thoroughly.
5. Commit your changes: Commit your changes with a descriptive commit message:

        git commit -m "Add feature/fix bug: description of your changes"
6. Push your changes: Push the changes to your forked repository:

        git push origin feature-or-bugfix-name

7. Create a pull request: Open a pull request from your forked repository back to the main repository. Provide a detailed description of the changes you've made and why they should be merged.
