Python journey [→ru](README.ru.md)
===

In this repository, I will document my journey of learning the Python language
and related tools.

> [!NOTE]
>
> **Something to note**: I already have experience in writing applications
> in Python, but I've decided to update, enhance, and systematize my knowledge.

## Commitment

As the main sources, I will use various books, official documentation,
and courses. I will provide code examples and notes, accompanying them
with references to the materials.

## Learning plan

To start, I will develop a learning plan, not overly detailed but ensuring
a certain sequence of material mastery.

Each significant stage will conclude with practical work, indicated by
a diamond symbol on the following schedule.

```mermaid
%%{init: {'theme':'neutral'}}%%
gantt
  dateFormat off
  axisFormat %d
  todayMarker off

  general               :general,    0, 2h
  basic functions       :basic,      after general, 2h
  literals              :literals,   after basic, 2h
  operators             :operators,  after literals, 2h
  variables             :var_const,  after operators, 3h
  types                  :types,      after var_const, 3h
  Scripts :milestone, m1
  functions             :def,        after types, 3h
  conditional branching :branching,  after def, 5h
  loops, generators     :loops,      after branching, 8h
  input / output        :io,         after loops, 3h
  import                :import,     after io, 5h
  exception handling    :exceptions, after import, 6h
  Simple applications :milestone, m2
  classes               :class,      after exceptions, 12h
  decorators            :decorators, after class, 6h
  json, xml, etc.       :file_formats, after decorators, 5h
  Data processing applications :milestone, m3
  documentation         :docs,       after file_formats, 3h
  testing               :testing,    after docs, 8h
  debug                 :debug,      after testing, 8h
  containers            :containers, after debug, 6h
  type system           :type_system, after containers, 5h
  Utilities :milestone, m4
  serialization / de-   :serialization, after type_system, 4h
  streams               :streams, after serialization, 8h
  concurrency           :concurrency, after streams, 16h
  Services :milestone, m5
  net                   :net, after concurrency, 8h
  ipc                   :ipc, after net, 4h
  extensions            :extensions, after ipc, 12h
  A grade applications :milestone, m6
```

## Books references

1. [Think Python, 2nd ed by Allen B. Downey](https://www.goodreads.com/book/show/14514306-think-python)
2. [Illustrated Guide to Python 3 by Matt Harrison](https://www.goodreads.com/book/show/36522990-illustrated-guide-to-python-3)

## About the Language

Python[^1] is a high-level, portable, dynamically typed[^2],
interpreted language with a garbage collection.

The language was developed by Guido van Rossum in 1991.

The language gained popularity by the time the second version was released.
The current version is the third, and it is considered the most up-to-date.

### Syntax and semantics

Python code is designed with readability in mind,
as it is visually formatted using indentation, and expressions are usually
not adorned with auxiliary symbols. The conventional semicolon,
which separates instructions, is often omitted, as the expression concludes
at the end of the line.

However, the `;` symbol may be used in specific cases when it is necessary
to write instructions on a single line.

The language lacks the conventional curly braces for delineating blocks
of instructions; this role is fulfilled by visual formatting with
a mandatory consistent indentation for instructions at the same level.

Spaces and tabs can be used as indentation characters,
but they should not be mixed within the same file.

### Language evolution

Despite its age, Python continues to evolve actively under the guidance
of the community and committees at the foundation[^3].

The language's development is carried out through the
Proposal Evaluation Process (PEP)[^4], from which the language description
is formed.

The language is characterized by a motto that defines the direction
of its development.

#### Zen of Python

There is a concise and eloquent way to describe the principles
guiding Python developers. These principles are known as the "Zen of Python"
and have their own PEP 20[^5].

> The Zen of Python, by Tim Peters
>
> Beautiful is better than ugly. <br />
> Explicit is better than implicit. <br />
> Simple is better than complex. <br />
> Complex is better than complicated. <br />
> Flat is better than nested. <br />
> Sparse is better than dense. <br />
> Readability counts. <br />
> Special cases aren't special enough to break the rules. <br />
> Although practicality beats purity. <br />
> Errors should never pass silently. <br />
> Unless explicitly silenced. <br />
> In the face of ambiguity, refuse the temptation to guess. <br />
> There should be one-- and preferably only one --obvious way to do it. <br />
> Although that way may not be obvious at first unless you're Dutch. <br />
> Now is better than never. <br />
> Although never is often better than *right* now. <br />
> If the implementation is hard to explain, it's a bad idea. <br />
> If the implementation is easy to explain, it may be a good idea. <br />
> Namespaces are one honking great idea -- let's do more of those! <br />

## Execution and Modes

To run a Python application or a standalone script, you need an interpreter
— an application capable of reading instructions in a human-readable language
and transforming them into instructions understood by a computing machine.

The advantage of interpreted languages over compiled ones is that
compilation tasks are performed directly when the program is launched,
without the need for additional building steps. This enhances code portability
and speeds up the development process. However, the execution
of interpreted code will never be as fast as that of a pre-compiled application
written in a lower-level language.

Python instructions can be executed either sequentially or as a program saved
in a file or a series of files.

To execute instructions sequentially, the REPL
(<ins>R</ins>ead <ins>E</ins>valuate <ins>P</ins>rint <ins>L</ins>oop)
mode is activated. In this mode, the interpreter awaits user input,
determining the end of an instruction when a new line is encountered.
The interpreter then attempts to execute the input and outputs the result
or an error, returning to await further input.

Running an application is a more common scenario, where the interpreter
immediately receives an entry point and attempts to execute
all subsequent instructions.

As an application may consist of one or more files, running an application
involves providing the path to the file or target directory as a Python
call argument. When specifying a directory, the interpreter looks for
the entry point in the `__main__.py` file.

Running Python is possible both on a local machine after installation[^6]
and in containerized environments[^7].

For the convenience of running simple scripts, you can use online services
such as [Python Anywhere](https://www.pythonanywhere.com/),
[Replit](https://replit.com/), or use [Google Colab](https://colab.google/)
as a REPL.

> [!NOTE]
>
> To exit the interpreter's REPL, call the globally available `exit()` method.

> [!NOTE]
>
> In Python, there is a "ahead of time compilation" stage where the interpreter
> converts the text version of Python code into bytecode, which is then executed.
> Such files are stored in the `__pycache__` directory, which should not be
> added to version control repositories by default.

## Basic functions

### print

One of the fundamental functions in any programming language
is the output function.

The `print` function automatically checks the type of the passed object.
If the object is not a string, the function converts its value to
a string format. By default, `print` outputs the result to the standard
output stream (`sys.stdout`), which usually means displaying it on the screen.
However, the output stream can be explicitly specified by passing it as
an argument when calling the function.

Allen Downey notes a slight difference in function calls between Python 2
and Python 3, specifically the absence of parentheses around arguments
in Python 2. However, in Python 3, the format with explicit indication
of the output stream through the file argument is used:

[Python2](https://docs.python.org/3/library/functions.html#print)
```python
>>> import sys
>>> print(>>sys.stdout, "Hello world\n")
```

[Python3](https://docs.python.org/3/library/functions.html#print)
```python
>>> import sys
>>> print("Hello world\n", file=sys.stdout)
```

These examples illustrate the syntax for different Python versions,
where in Python 2, `>>` is used to specify the output stream,
and in Python 3, the file argument is used for explicitly indicating
the output stream.

### input

In the context of data input in Python, there is the input function[^8].
Similar to the `print` function, `input` is globally accessible.

The `input` function allows you to switch the program's execution to
a waiting-for-input mode. When input is provided, and the user presses
the "Enter" key, input captures all the characters entered earlier.
The result is returned as a string.

```python
>>> input("Say my name: ")
Say my name: Mr. White
'Mr. White'
```

#### dir

The `dir` function returns a list of names available in the specified scope[^9].
If called without arguments, the current scope is selected.
If an object is passed to the function, dir returns a list of its methods
and attributes.

### help

The built-in help function[^10] is a powerful tool, especially in REPL mode.
Without arguments, calling the function initiates an interactive documentation
index search console. If the name of a function or class is specified,
the interpreter will attempt to find the corresponding element among those
registered in the current environment and provide help for it.

> [!NOTE]
> I won't go into detail on all the built-in functions. However,
> it's worth noting their importance and variety. For a detailed description
> of each function, you can refer to the official documentation[^11].

> [!TIP]
>
> The `help` method can also be used with the builtins argument
> to get detailed help. Alternatively, the `dir` method can be called with
> the `__builtins__` argument to display a list of registered names.

```python
>>> help('builtins')
Help on built-in module builtins:

NAME
    builtins - Built-in functions, types, exceptions, and other objects.
...
```

```python
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', ...
```

> [!NOTE]
>
> It is important to avoid redefining reserved names of built-in objects
> and functions. This can lead to unpredictable results and hard-to-trace errors
> in the code. Interfering with reserved names can also cause naming conflicts,
> making the code harder for other developers to understand.
> If you need to use similar names, it's better to choose more specific ones
> or add prefixes to avoid conflicts.

## Literals, Boolean Values, and None

Literals[^12] are significant combinations of characters that can be represented
as strings[^13] or numbers[^14].

### Strings

String literals[^13] in Python are distinguished by the presence of quotes
on both sides. Quotes can be single (`'`), double (`"`),
or a series of single (`'''`) or double (`"""`) quotes.

```python
'It\'s a string literal'

"This is also a string literal"

'''
It's is a multi
line string
'''

"""
And this is a also multi
line string
"""
```

Differences in the type and quantity of quotes are determined by the meaning
of the characters contained in the literal. This allows avoiding the need for
escaping characters in some cases.

For example: `'''My name is 'Max\''''`.

As seen in the example, in a string enclosed in three single quotes,
it's not necessary to escape a single quote inside.
However, it is necessary to escape the same single quote at the end of
the string to separate it from the closing sequence.

To avoid such misunderstandings, it is recommended to consider which characters
will be inside the string and use the opposite type of quotes.

For example, this can prevent problems: `"""My name is 'Max'"""`.

Additionally, string literals can have control prefixes `f`, `r`, `u`, and `b`.
Where `f` specifies that the string contains variable formatting,
`r` indicates that the literal represents a "raw" string, i.e.,
a string where all characters are treated as written,
`u` indicates that the string uses Unicode encoding, and `b` indicates that
the string is represented as a sequence of bytes.

```python
>>> r'\Hello \People' # Raw string
'\\Hello \\People'

>>> u'This string in a Unicode format' # Backward capability from Python2
'This string in a Unicode format'

>>> f'x={1+1} y={{1,2,3,4,5}}' # Formatted string
'x=2 y={1,2,3,4,5}'

>>> b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'.decode('utf-8')
'τoρνoς'
```

### Numbers

Numeric literals[^14] are a set of characters consisting of the sign indicating
whether the number belongs to the subset of positive or negative real numbers
(`+`, `-`), the number format indicator (`0b` for binary, `0o` for octal,
`0x` for hexadecimal), digits `0,1` for binary, `0..7` for octal,
`0..9` for decimal, and in the case of hexadecimal numbers, the letters `A..F`.
The dot (`.`) is used as a separator between the integer and fractional parts
of the number.

Floating-point numbers can be written in exponential form using the postfix `e`
and specifying the exponent.

```python
# integers
0
41
0b101001
0o51
0x29
2_023
-41
```

> [!CAUTION]
>
> An integer decimal number cannot start with the digit 0.

```python
# floats
0.
0.30684931506
.30684931506
0.2023e4
306_849.0e-6
```

In addition to integers[^15] and floating-point numbers[^16], there is also
a notation for the literal of an imaginary number[^17].

```python
# imaginary
3.14j
1e100j
```

With the introduction of PEP 515[^18], it became possible to visually separate
digits with the underscore `_` character.

### Boolean values<a name="boolean"></a>

Boolean values, describing logical states[^19], are predefined and have
a fixed notation: `True` and `False`.

### None

`None` is a reserved word that expresses the absence of a value[^20]
and has a fixed notation.

## Operators<a name="opertors"></a>

Various operators are used to perform operations on numbers, strings,
and boolean values.

### Arithmetic Operations[^21]

| | Operator |       String        |    Number    |    Boolean    |
|-|:---------|:--------------------|-------------:|--------------:|
|1|  L + R   |  'a' + 'b' = 'ab'   |  1 + 2 = 3   |   T + T = 2   |
| |  L - R   |            -        |  1 - 2 = -1  |   F - T = -1  |
|1|  L * R   |    'a' * 3 = 'aaa'  | -1 * 2 = -2  |   T * T = 1   |
| |  L / R   |            -        |  1 / 2 = 0.5 |   F / T = 0.0 |
| |  L ** R  |            -        |  5 ** 2 = 25 |  T ** T = 1   |
| |  L // R  |            -        |  5 // 2 = 2  |  T // T = 1   |
|1|  L % R   | '%s' % 100 = '100'  |   5 % 2 = 1  |   T % T = 0   |

### Bitwise Operations[^22]

| | Operator |       String        |    Number    |    Boolean    |
|-|:---------|:--------------------|-------------:|--------------:|
| |  L ^ R   |            -        |   5 ^ 2 = 7  |   F ^ T = T   |
| |  L & R   |            -        |   5 & 2 = 0  |   F & T = F   |
| |  L \| R  |            -        |   5 | 2 = 7  |   F | T = T   |
| |  L << R  |            -        |  5 << 2 = 20 |  T << T = 2   |
| |  L >> R  |            -        |  5 >> 2 = 1  |  T >> T = 0   |
| |    ~R    |            -        |      ~2 = -3 |      ~T = -2  |

### Comparison Operations[^23]

| | Operator |       String        |    Number    |    Boolean    |
|-|:---------|:--------------------|-------------:|--------------:|
| |  L == R  | 'a' == 'b' = F      |  5 == 2 = F  |  F == T = F   |
| |  L != R  | 'a' != 'b' = T      |  5 != 2 = T  |  F != T = T   |
| |  L > R   |  'a' > 'b' = F      |   5 > 2 = T  |   F > T = F   |
| |  L >= R  | 'a' >= 'b' = F      |  5 >= 2 = T  |  F >= T = F   |
| |  L < R   |  'a' < 'b' = T      |   5 < 2 = F  |   F < T = T   |
| |  L <= R  | 'a' <= 'b' = T      |  5 <= 2 = F  |  F <= T = T   |

### Logical Operations[^24]

| | Operator |       String        |    Number    |    Boolean    |
|-|:---------|:--------------------|-------------:|--------------:|
| |  L and R |'a' and 'b' = 'b'    | 5 and 2 = 2  | F and T = F   |
| |  L or R  | 'a' or 'b' = 'a'    |  5 or 2 = 5  |  F or T = T   |
| |   not R  |    not 'b' = F      |   not 2 = F  |   not T = F   |
|*| L is R   | 'a' is 'b' = F      |  5 is 2 = F  |  F is T = F   |
|*|L is not R| 'a' is not 'b' = T  |5 is not 2 = T|F is not T = T |

`*` - The is and is not operators are used to check the identity
of object identifiers; they do not compare values.

All the mentioned operations are applicable to both numbers and boolean values.

The language follows the principle of implicit type conversion,
allowing such behavior. In some cases, a number is converted to a boolean type,
and in other cases, a boolean type is converted to a number.
You can identify such cases based on the result of the operation.

`1` - String literals have three specially overridden arithmetic operators: `+`,
which concatenates strings, `*`, which repeats a string a specified number
of times, and `%`, which formats a string using formatting specifications[^25].
Other arithmetic operations for strings are not defined.

> [!TIP]
> When comparing boolean values, it is advisable to prioritize logical operators
> over bitwise operators.

> [!TIP]
>
> The language allows for multiple comparisons, such as `1 < 3 > 2`.
> This type of comparison is known as a range check.

## Variables

Variables are used to reference original or intermediate values.
As Matt Harrison notes, variables can be thought of as labels pointing
to values that can be reused over and over.

```python
name = 'Maksim Kalenich'
year = 1982
```

### Variables Names

The language has restrictions on variable names. A variable can consist of
Latin alphabet letters, digits, and underscores. However, a variable cannot
start with a digit.

Additionally, the language has a list of reserved words[^26] that
the interpreter will not allow as variable names.

> [!TIP]
>
> By calling `help('keywords')`, a short reference will be presented.
> Alternatively, you can import the keyword module and access its
> kwlist variable, which contains the list of reserved words.
>
> ```python
> >>> import keyword
> >>> keyword.kwlist
> ```

In addition to reserved words, Matt Harrison does not recommend using names
of built-in language elements, the list of which is available from
the [`__builtins__`](#help) variable.

It is considered good practice, both in general and specifically in Python,
to give variables descriptive names that indicate the values they point to.

Furthermore, it's worth noting that the language documentation suggests
a specific variable naming convention[^27]: `snake_case`, where names are given
in lowercase letters, and if the name consists of multiple parts,
the parts are joined by underscores.

### Declaration and Initialization of Variables

Initially, the syntax of Python only allowed for variable declaration
with initialization. However, starting from version 3.6, it became possible
to declare a variable by specifying its type without providing
an initializing value.

```python
favorite_book = "The Hitchhiker's Guide to the Galaxy"
current_book: str
```

The assignment operator `=` is used to initialize a variable,
creating a representation of the assigned value as an object.

Each object is assigned an identifier, a description of the value's type,
and a reference count.

The reference count is necessary for the Python runtime environment because
it is responsible for the lifespan of values and timely memory cleanup,
not the developer.

> [!TIP]
>
> To obtain the identifier of an object, there is a built-in method called `id`.
>
> ```python
> >>> id(favorite_book)
> 4423523640 # yours would be different
> ```
>
> To get the type of the value represented by an object, you can use the
> built-in method `type`.
>
> ```python
> >>> type(favorite_book)
> <class 'str'>
> ```
>
> To get the reference count value for a specific object, you can use the
> `getrefcount` method from the `sys` package.
>
> ```python
> >>> import sys
> >>> sys.getrefcount(favorite_book)
> 2
> ```
>
> If you create another variable and assign the same object to it,
> the reference count will increase.
>
> ```python
> >>> favorite_guide = favorite_book
> >>> sys.getrefcount(favorite_book)
> 3
> ```
>
> When calling `getrefcount`, the reference count returned is one more than
> the expected count because a temporary reference is added as an argument
> during the function call.

### Variable Redefinition

Since Python is a dynamically-typed language, a variable can be redefined with
a value of a type different from the one it previously pointed to.

```python
>>> num = '1'
>>> id(num)
4423584600
>>> type(num)
<class 'str'>

>>> num = int(num)
>>> id(num)
4423523640
>>> type(num)
<class 'int'>
```

In this case, one value can be associated with multiple variables.

If you check the `id` of an already registered value, it will be the same as
the identifier returned from the variable.

```python
>>> num2 = num
>>> id(num)
4423523640

>>> id(num)
4423523640

>>> id(1)
4423523640
```

> [!NOTE]
>
> In fact, the identifier is a representation of the address of the value
> in memory. It may and will change from one run of the application to another.

> [!WARNING]
>
> Despite the language allowing variable redefinition by assigning values of
> different types, it is a bad idea. This complicates the determination of
> why the variable changed its type and under what circumstances it happened.

### Deferred Access to Operation Result in REPL

The result of an expression that was not assigned to a variable in time
will be lost. However, Python provides intermediate storage for
the computed value. It is available in a variable named `_`.

```python
>>> 100 + 1
101
>>> _
101
```

I learned about this feature from Matt Harrison's book.

### Assignment with evaluation

The assignment operator can be combined with some operators from the list,
allowing the reassignment of the value for the variable on the left.

#### Arithmetic Operations[^21]

| Operator   |       Number       |
|:-----------|-------------------:|
||                         x = 10 |
|   L += R   |  x += 2  # x = 12  |
|   L -= R   |  x -= 3  # x = 9   |
|   L *= R   |  x *= 3  # x = 27  |
|   L /= R   |  x /= 10 # x = 2.7 |
|  L **= R   | x **= 2  # x = 7.29|
|  L //= R   | x //= 2  # x = 3.0 |
|   L %= R   |  x %= 2  # x = 1.0 |

#### Bitwise Operations[^22]

| Operator   |       Number       |
|:-----------|-------------------:|
||                          x = 5 |
|   L ^= R   |   x ^= 2 # x = 7   |
|   L &= R   |   x &= 2 # x = 2   |
|  L \|= R   |  x \|= 4 # x = 6   |
|  L <<= R   |  x <<= 2 # x = 24  |
|  L >>= R   |  x >>= 3 # x = 3   |

---

[^1]: <https://www.python.org/> "Python official site"
[^2]: <https://en.wikipedia.org/wiki/Python_(programming_language)> "Python on Wikipedia"
[^3]: <https://legacy.python.org/psf/committees/> "Python Software Foundation"
[^4]: <https://peps.python.org/pep-0000/> "Python Enhancement Proposals"
[^5]: <https://peps.python.org/pep-0020/> "The Zen of Python"
[^6]: <https://www.python.org/downloads/> "Python download page"
[^7]: <https://hub.docker.com/_/python> "Docker image for Python"
[^8]: <https://docs.python.org/3/library/functions.html?highlight=input#input> "Input function, Python documentation"
[^9]: <https://docs.python.org/3/library/functions.html?highlight=dir#dir> "Dir function, Python documentation"
[^10]: <https://docs.python.org/3/library/functions.html?highlight=help#help> "Help function, Python documentation"
[^11]: <https://docs.python.org/3/library/functions.html> "Built-in functions, Python documentation"
[^12]: <https://docs.python.org/3/reference/lexical_analysis.html#literals> "Literals, Python documentation"
[^13]: <https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals> "String literals, Python documentation"
[^14]: <https://docs.python.org/3/reference/lexical_analysis.html#numeric-literals> "Numeric literals, Python documentation"
[^15]: <https://docs.python.org/3/reference/lexical_analysis.html#integer-literals> "Integer literals, Python documentation"
[^16]: <https://docs.python.org/3/reference/lexical_analysis.html#floating-point-literals> "Floating point number literals, Python documentation"
[^17]: <https://docs.python.org/3/reference/lexical_analysis.html#imaginary-literals> "Imaginary number literals, Python documentation"
[^18]: <https://peps.python.org/pep-0515/> "PEP 515 – Underscores in Numeric Literals, Python documentation"
[^19]: <https://docs.python.org/3/library/stdtypes.html#boolean-type-bool> "Boolean Type, Python documentation"
[^20]: <https://docs.python.org/3/reference/datamodel.html#none> "None, Python documentation"
[^21]: <https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex> "Arithmetic operators, Python documentation"
[^22]: <https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types> "Bitwise operators, Python documentation"
[^23]: <https://docs.python.org/3/library/stdtypes.html#comparisons> "Comparisons operators, Python documentation"
[^24]: <https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not> "Logical operators, Python documentation"
[^25]: <https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting> "String formatting, Python documentation"
[^26]: <https://docs.python.org/3/reference/lexical_analysis.html#keywords> "Reserved keywords, Python documentation"
[^27]: <https://peps.python.org/pep-0008/#naming-conventions> "PEP 008 — Naming Conventions, Python documentation"
[^28]: <https://en.wikipedia.org/wiki/IEEE_754> "IEEE 754 on Wikipedia"
[^29]: <https://docs.python.org/3/tutorial/floatingpoint.html#floating-point-arithmetic-issues-and-limitations> "Floating Point Arithmetic: Issues and Limitations, Python documentation"
[^30]: <https://docs.python.org/3/library/decimal.html#module-decimal> "Decimal fixed point and floating point arithmetic, Python documentation"
[^31]: <https://docs.python.org/3/library/fractions.html#module-fractions> "Rational numbers, Python documentation"
[^32]: <https://docs.python.org/3/library/math.html#module-math> "Mathematical functions, Python documentation"
[^33]: <https://en.wikipedia.org/wiki/Lazy_evaluation> "Lazy evaluation on Wikipedia"
[^34]: <https://en.wikipedia.org/wiki/String_(computer_science)> "String on Wikipedia"
[^35]: <https://docs.python.org/3/library/functions.html#func-bytes> "Bytes function, Python documentation"
[^36]: <https://docs.python.org/3/library/functions.html#func-bytearray> "Bytearray function, Python documentation"
[^37]: <https://docs.python.org/3/library/stdtypes.html#str> "Builtin str function, Python documentation"
[^38]: <https://docs.python.org/3/library/functions.html#format> "Format method of str type, Python documentation"
[^39]: <https://docs.python.org/3/reference/lexical_analysis.html#f-strings> "F-string literals, Python documentation"
[^40]: <https://docs.python.org/3/library/string.html> "Methods of str type, Python documentation"
[^41]: <https://docs.python.org/3/library/stdtypes.html#tuples> "Tuple type, Python documentation"
[^42]: <https://docs.python.org/3/library/stdtypes.html#tuple> "Builtin function tuple, Python documentation"
[^43]: <https://docs.python.org/3/library/stdtypes.html#lists> "List type, Python documentation"
[^44]: <https://docs.python.org/3/library/functions.html#func-list> "Builtin function list, Python documentation"
[^45]: <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset> "Set type, Python documentation"
[^46]: <https://en.wikipedia.org/wiki/Set_theory> "Set theory on Wikipedia"
[^47]: <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict> "Dict type, Python documentation"
[^48]: <https://docs.python.org/3/library/stdtypes.html#ranges> "Ranges, Python documentation"
[^49]: <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/uname.html> "Specification on uname command"
