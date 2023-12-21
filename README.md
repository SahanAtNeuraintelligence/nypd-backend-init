# NYPD App Backend

## Run

```python
python3 main.py --env local|dev|prod --debug
```

```docker
docker-compose up
```




Python's naming conventions are a set of guidelines established in PEP8, Python’s official style guide¹². Here are some of the key conventions:

1. **General Python Naming Conventions**²:
    - Names are case-sensitive.
    - Names cannot start with a digit.
    - Names can contain letters, numbers, and underscores.

2. **Naming Styles**²:
    - **Snake Case**: All words lower case separated by underscores. This is primarily used for function and variable names. Example: `user_name`, `my_function`.
    - **Pascal Case**: The first letter of each word is capitalized. This is used for class names in Python. Example: `ClassName`, `MyClass`.
    - **Camel Case**: First letter of each word is capitalized except the first word. This is not commonly used in Python. Example: `myVariable`, `isInstance`.
    - **Upper Case with Underscores**: All letters are upper case and words are separated by underscores. This is used for constants in Python. Example: `MAX_OVERFLOW`, `TOTAL`.

3. **Names to Avoid**²:
    - Never use characters ‘l’ (lowercase letter el), ‘O’ (uppercase letter oh), or ‘I’ (uppercase letter eye) as single-character variable names. These can be easily mistaken in certain fonts for ‘1’ (one), ‘0’ (zero), and ‘|’ (pipe), respectively.
    - Reserved words in Python cannot be used as variable names. These include ‘for’, ‘while’, ‘if’, ‘else’, etc.

4. **Function Naming Conventions**⁴:
    - Verbs indicate an action like `calculate()`, `render()`, `fetch()` etc. This is the most common format.
    - Nouns describe or return a value like `name()`, `user()`.
    - Adjectives add specificity like `total_price()`.
    - Mixing nouns, verbs, and adjectives together builds descriptive names like `calculate_total_price()`.

By sticking to these naming conventions, your Python code will be more readable, maintainable, and in line with community standards².

Source: Conversation with Bing, 21/12/2023
(1) PEP 8 – Style Guide for Python Code | peps.python.org. https://peps.python.org/pep-0008/.
(2) Naming Convention In Python [With Examples] - Python Guides. https://pythonguides.com/python-naming-conventions/.
(3) Python Function Naming Conventions and Best Practices. https://llego.dev/posts/python-function-naming-conventions-best-practices/.
(4) Python Naming Conventions: Python Explained - Bito. https://bito.ai/resources/python-naming-conventions-python-explained/.
