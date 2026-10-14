# 🔨 Blind Auction

> A command-line Python program that runs a secret-bid auction: every bidder enters a name and a bid, the screen is cleared between turns, and the highest bid wins.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-completed-brightgreen?style=for-the-badge)
![Project](https://img.shields.io/badge/project-personal-blueviolet?style=for-the-badge)

---

## 📌 About the Project

**Blind Auction** is an interactive console application written in Python. Bidders take turns typing their name and their bid. After each turn the program prints a block of blank lines so the next person cannot see the previous bid, which is what makes the auction "blind". When there are no more bidders, the program announces the winner.

This is a **personal project developed independently** as part of my programming portfolio. It was built to practise working with dictionaries and loops: storing each bidder's name together with their bid, repeating the input until the user says stop, and finding the highest value.

---

## 🎯 Learning Objectives

- **Dictionaries**: storing each bidder's name as a key and their bid as the value.
- **While loops with `break`**: repeating the input steps until the user answers `no`.
- **Type conversion**: turning the bid typed by the user into a number with `float()`.
- **Finding a maximum**: using `max()` with `key=name_and_bid.get` to get the name with the highest bid.
- **String methods**: using `.lower()` so the `yes`/`no` answer works in any letter case.
- **Output control**: using `print('\n' * 50)` to push earlier bids off the screen, and `print(..., end=' ')` to keep the winner on one line.
- **Raw strings**: using `r'''...'''` to print an ASCII-art gavel without escaping backslashes.

---

## ⚙️ How It Works

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│ Show logo    │ -> │ Ask name and │ -> │ Save the bid │ -> │ More bidders?│ -> │ Print the    │
│ and welcome  │    │ bid          │    │ in the       │    │ Clear screen │    │ winner       │
│ message      │    │              │    │ dictionary   │    │ and repeat   │    │ (highest bid)│
└──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘
```

### Code Walkthrough

```python
print("Welcome to Blind Auction Project")
print( r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')


name_and_bid = {}

name=input("What is your name? ")
price=float(input("What is your bid? R$"))

name_and_bid[name] = price

should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
print('\n'*50)
while True:
    name = input("What is your name? ")
    price = float(input("What is your bid? R$"))
    name_and_bid[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    print('\n'*50)
    if should_continue == "no":
        break

print('The winner is:',end=' ')
print(max(name_and_bid, key= name_and_bid.get),end=' ')
```

| Line / Section | Responsibility |
|---|---|
| First two `print` calls | Show the welcome message and the ASCII-art gavel (a raw string, so backslashes print as written) |
| `name_and_bid = {}` | Creates an empty dictionary that maps each bidder's name to their bid |
| First `input` pair | Reads the first bidder's name and bid (converted with `float()`) |
| `name_and_bid[name] = price` | Saves the bid in the dictionary |
| `should_continue = input(...)` | Asks whether there are more bidders and lowercases the answer |
| `print('\n'*50)` | Prints 50 blank lines to hide the previous bid |
| `while True` loop | Reads a name and a bid, saves them, asks again, clears the screen, and stops when the answer is `no` |
| `max(name_and_bid, key=name_and_bid.get)` | Returns the dictionary key (the name) whose value (the bid) is the highest |

**Technical note.** When `max()` receives a dictionary, it compares the keys by default. Passing `key=name_and_bid.get` changes the comparison so that each name is ranked by its bid instead, and the function still returns the name. If two bidders tie, `max()` returns the one who was added first.

**Known limitations** (this is a learning project, so these were left as they are):

- **Minimum of two bidders.** The answer to the first "Are there any other bidders?" question is read but not checked, so the auction always asks for a second bidder. The `no` answer takes effect from the second bidder onward.
- **No input validation.** A bid that is not a number (for example `abc`) stops the program with a `ValueError`.
- **Duplicate names.** Entering the same name twice replaces that person's earlier bid, because dictionary keys are unique.
- **Winner line shows the name only**, not the winning amount.

---

## 🚀 Getting Started

### Prerequisites

- [Python 3.x](https://www.python.org/downloads/) installed
- No external libraries required (only built-in functions are used)

### Installation and Execution

```bash
git clone https://github.com/guiggsp-hub/Blind-Auction.git
cd Blind-Auction
python main.py
```

### Sample Run

Between each turn the screen is cleared with blank lines, so the earlier answers are not visible to the next bidder. This is the sequence of questions and answers:

```
Welcome to Blind Auction Project

                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\

What is your name? Ana
What is your bid? R$100
Are there any other bidders? Type 'yes' or 'no': yes

[screen cleared]

What is your name? Bruno
What is your bid? R$250.5
Are there any other bidders? Type 'yes' or 'no': yes

[screen cleared]

What is your name? Carla
What is your bid? R$200
Are there any other bidders? Type 'yes' or 'no': no

[screen cleared]

The winner is: Bruno
```

---

## 🧠 Skills Demonstrated

`Python` · `Dictionaries` · `While Loops` · `Type Conversion` · `User Input` · `max() with key` · `String Methods` · `CLI Applications`

---

## 👤 Author

Developed independently by **Guilherme Garcia** as part of a personal programming portfolio.

[![GitHub](https://img.shields.io/badge/GitHub-guiggsp--hub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/guiggsp-hub)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Guilherme%20Garcia-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/guilherme-garcia-796633287/)
