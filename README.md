**      Password-Generator      **

A simple command-line password generator written in Python. You choose the total length and exact counts of symbols, capital letters, and numbers — the rest is filled with lowercase letters, and everything is shuffled for randomness.

*Features:*
    1. Custom total password length
    2. Exact counts for symbols, capital letters, and numbers
    3. Remaining characters auto-filled with lowercase letters
    4. Input validation (won't let counts exceed total length)
    5. Fully shuffled output — no predictable character order
   
*How it works:*
    1. Run the script
    2. Enter the total number of characters you want
    3. Enter how many should be symbols, capital letters, and numbers
    4. Get your randomly generated password

*Usage:*
python password_generator.py

*Example run:*

=== Password Generator ===
Total number of characters: 10
Number of symbols: 2
Number of capital letters: 3
Number of numbers: 2

Your generated password: K9@t3Lm#Rp
(Remaining 3 characters filled with lowercase letters)

*Requirements:*

   1. Python 3.x (uses only the built-in random and string modules — no extra installs needed)

*Possible future improvements:*

   1. Option to exclude ambiguous characters (e.g. 0, O, l, 1)
   2. Save generated passwords to a file
   3. GUI or web version


Author-
Kashish
