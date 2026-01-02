🎨 ASCII Art Project (Python)

A simple menu-driven Python console application that prints ASCII art for letters, words, and numbers using predefined pattern data.
The project is designed for Windows terminal and focuses on basic Python concepts.

📌 About the Project

This project generates large ASCII art for:

Small letters

Capital letters

Small words

Capital words

Numbers

All ASCII designs are created using custom pattern data stored inside the program.
The user can also select a color for the ASCII output.

⭐ Features

✔ Menu-driven interface
✔ Color selection using keyboard
✔ Supports:

Small letters

Capital letters

Words

Numbers

✔ Uses basic Python only
✔ Color resets automatically after output
✔ Beginner / BCA friendly project

🧠 How It Works
🔤 ASCII Pattern Data

The project stores ASCII art patterns in two lists:

SMALL_PATTERNS → for small letters

BIG_DATA → for capital letters and numbers

Each character pattern:

Has 6 columns width

Uses index calculation to slice correct ASCII shape

🔢 Character Index Logic

Small letters

((ord(ch) - 96) - 1) * 6


Capital letters

(ord(ch.upper()) - 65) * 6


Numbers

(ord(ch) - 17) * 6

🖨 Printing Mechanism

ASCII art is printed row by row

Each character is printed side-by-side

Selected color is applied only to ASCII art

Color resets back to white after printing

📂 Project File
ascii_art_project.py


This file contains:

ASCII pattern data

Color selection logic

Menu interface

Printing functions

⚙ Installation
1️⃣ Install Python

Download from:
https://www.python.org/

2️⃣ Install Required Module
pip install colorama

3️⃣ Run the Program
python ascii_art_project.py

▶ Usage

After running the script, the following menu appears:

ASCII ART PROJECT

1. Small Letter
2. Capital Letter
3. Small Word
4. Capital Word
5. Numbers
6. Exit


Press 1–6 to select an option

Choose a color

Enter input as asked

ASCII art will be printed in selected color

🖼 Example Output

Input

A


Output (example)

 *** 
*   *
*****
*   *
*   *



⚠ Notes

Works only on Windows

Uses:

msvcrt.getch()

os.system("cls")

Color applies only to ASCII art

Code is intentionally kept basic

👨‍💻 Author

Usha Assudani

BCA Student

ASCII Art Project using Python
