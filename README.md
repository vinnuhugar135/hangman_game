# Task 1: Hangman Game

A simple text-based Hangman game for the console.

## Features
- 5 predefined words (no file or API required)
- Maximum of 6 incorrect guesses
- Basic console input/output (no graphics or audio)
- Input validation (single letters only, no repeated guesses)
- ASCII hangman drawing and a "play again" option

## Concepts Used
`random`, `while loop`, `if-else`, `strings`, `lists`

## Requirements
Python 3.6 or newer (no external libraries needed)

## How to Run
```
python hangman.py
```
(use `python3 hangman.py` on macOS/Linux if needed)

## How to Play
1. A random word is chosen and shown as underscores.
2. Type one letter at a time.
3. Correct letters are revealed; wrong letters add to the hangman.
4. Win by guessing the whole word before 6 wrong guesses.

## Project Structure
```
hangman_game/
├── hangman.py   # the game
└── README.md    # this file
```
