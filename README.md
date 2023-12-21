# NYPD App Backend

## Run

```python
python3 main.py --env local|dev|prod --debug
```

```docker
docker-compose up
```




Python's naming conventions are a set of guidelines established in PEP8, Python’s official style guide. Here are some of the key conventions:
pep8 documentation: [https://www.python.org/dev/peps/pep-0008/](https://peps.python.org/pep-0008/)


**Naming Styles**²:
    - **Snake Case**: All words lower case separated by underscores. This is primarily used for function and variable names. Example: `user_name`, `my_function`.
    - **Pascal Case**: The first letter of each word is capitalized. This is used for class names in Python. Example: `ClassName`, `MyClass`.
    - **Upper Case with Underscores**: All letters are upper case and words are separated by underscores. This is used for constants in Python. Example: `MAX_OVERFLOW`, `TOTAL`.

**Function Naming Conventions**⁴:
    - Verbs indicate an action like `calculate()`, `render()`, `fetch()` etc. This is the most common format.
    - Nouns describe or return a value like `name()`, `user()`.
    - Adjectives add specificity like `total_price()`.
    - Mixing nouns, verbs, and adjectives together builds descriptive names like `calculate_total_price()`.

By sticking to these naming conventions, your Python code will be more readable, maintainable, and in line with community standards².




To Run Pre Commit on PyCharm
Need to create a Symlink to the poetry executable
`sudo ln -s ~/.local/bin/poetry /usr/local/bin/poetry`