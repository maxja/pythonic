Python learning playground [→ru](README.ru.md)
===

This repository will document my learning journey with the Python language and its supporting tools.

> **Disclaimer**: I have some prior experience with Python, particularly with Python 2.

## Commitment

I will be following various books and will provide code samples and notes based on what I have learned and understood.
All references to books will be accompanied by links leading to a reference list.

## Books references

1. [Think Python, 2nd ed by Allen B. Downey][1]

## About Language

Python is an interpreted language.

## REPL — <ins>R</ins>ead <ins>E</ins>valuate <ins>P</ins>rint <ins>L</ins>oop

Some languages, mostly interpreted ones, do have a so-called REPL, or interactive console, that reads given input,
tries to evaluate what it's got as an input, prints out the result or error description, and starts awaiting
a new input.

It allows testing algorithmic hypotheses step by step.

To run the Python REPL, just execute `$ python` or `$ python3` this will run the subroutine and print out the input invitation started with `>>>`.

> To exit from it, simply call the globally available method `exit()`.

## Setup

Python 3 (hereinafter Python) — the target version of the language that interests me in the learning process.

Python can be installed as a standalone package, and there are many ways to do this, varying from one operating system
to another.

Allen Downey, the author of the book ["Python Basics"][1], suggests using the online service [Python Anywhere](https://www.pythonanywhere.com/), although there are many other platforms available, such as [Google Colab](https://colab.google/).


## Dive into

### Essential

#### print

The print function is one of the main functions and is located in the global namespace. At first glance, it "simply" outputs the given value "to the screen." However, in reality, everything is a bit more complex.

The print method first checks the type of the passed object, and if it is not a string, it invokes conversion.
Moreover, the thesis that print outputs "to the screen" is also incorrect. By default, print outputs to the specified
output stream, which points to sys.stdout, but the output stream can also be specified by passing it as an argument
during the call.

Allen Downey, the author of the book ["Python Basics"][1], notes only one difference between the calling formats
in Python2 and Python3 - the absence of parentheses around the call arguments in the second version. In reality, however, parentheses can be present,
but the composition of the call arguments is significantly different:

[Python2](https://docs.python.org/3/library/functions.html#print)
```python
import sys
print(>>sys.stdout, "Hello world\n")
```

[Python3](https://docs.python.org/3/library/functions.html#print)
```python
import sys
print("Hello world\n", file=sys.stdout)
```

#### Arithmetic operations: + - * / **

* `+` — addition
* `-` — subtraction
* `*` — multiplication
* `/` — division
* `**` — exponentiation

#### Bit logic operations: ^

* `^` — XOR

[1]: <https://www.goodreads.com/book/show/14514306-think-python> "Think Python, 2nd ed by Allen B. Downey"
