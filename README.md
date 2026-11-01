### Hangman (Python CLI)

An interactive, text-based implementation of the classic Hangman word-guessing game built with standard Python. Designed to provide quick entertainment with zero external dependencies, robust input validation, and real-time session tracking.

#### Overview

Hangman challenges players to deduce randomly selected programming-related words within a finite number of attempts (8 attempts). Every decision counts: accurate guesses reveal letters in the masked word, while inaccurate guesses deplete available attempts.

#### Features

- **Zero Dependencies**: Built entirely with Python's standard library (`random`, `enum`).
- **Input Validation**: Ensures valid user input by enforcing single lowercase English letters and preventing duplicate guess penalties.
- **Scoreboard & State Tracking**: Keeps track of total wins and losses during active sessions.
- **Interactive Menu**: Simple commands to start games (`play`), inspect scoreboard statistics (`results`), or quit (`exit`).

#### Getting Started

##### Prerequisites

- Python 3.10+ (utilizes modern `match`/`case` pattern matching)

##### Installation & Execution

1. Clone the repository:
   ```bash
   git clone https://github.com/original-xiobin/Hangman.git
   cd Hangman

2. Run the game:
   python task/Hangman/hangman.py

Game Rules & Commands
•
Menu Navigation:
◦
play: Starts a new round with 8 guess attempts.
◦
results: Displays lifetime wins and losses for the current session.
◦
exit: Terminates the program.
•
Guessing:
◦
Enter one lowercase letter from a to z per turn.
◦
Repeated guesses or invalid characters trigger helpful prompts without expending attempts.
◦
Guess all letters correctly before attempts reach zero to win!

Project Structure
•
hangman.py: Core game engine handling input loops, validations, word masking, and game state.
License
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# Copyright (C) 2026
