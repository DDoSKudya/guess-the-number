# **Guess Number**

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/p7?style=for-the-badge)

A mini-game in which you need to guess the number guessed by the program.

# **Installation**

You can decide for yourself whether to use a virtual environment or not, but no third-party libraries are used for this game.

You should use the recommended Python version.

You should run the file - run.py
```
python run.py
```

# **Exploitation**

After the launch run.py the program will prompt you to enter a number in the range from 1 to 100 or the stop word 'stop' (the range and stop word can be changed in the file 'constants.py '):

```
Guess the number from 1 to 5 (to finish the game, enter 'stop'):
Number: 
```

After entering, the proposed number is compared with the desired one and the result is output:

```
The hidden number 5.
Your number is 1.

You've lost!
```

Immediately the user has a choice: play on or stop (the keys are accepted: y, yes, Y, Yes, YES, n, no, N, No, NO):

```
Play some more? (Yes, No)
Answer: Yes
```

If an incorrect key is entered, the script will notify you about it:

```
You need to enter Yes or No.
```

At the end of the game, the user can get acquainted with the statistics of current games (total attempts and his wins):

```
Statistics:
Total attempts: 1,
Wins: 0.

The game is over.
```

Have a nice game!
