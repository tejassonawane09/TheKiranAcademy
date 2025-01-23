# Predefined Functions in Python

Predefined functions are the functions provided by Python that you can use directly without creating them. They help perform common tasks quickly and efficiently.

## Common Predefined Functions

### `print()`
- **Purpose:** Displays output on the screen.
```python
print("Hello, World!")
# Output: Hello, World!
```

### `len()`
- **Purpose:** Returns the number of elements in a string, list, or other collections.
```python
text = "Hello"
print(len(text))
# Output: 5
```

### `type()`
- **Purpose:** Returns the data type of a variable.
```python
num = 10
print(type(num))
# Output: <class 'int'>
```

### `input()`
- **Purpose:** Takes input from the user.
```python
name = input("Enter your name: ")
print("Hello, " + name)
# Output: Enter your name: Kanon
#         Hello, Kanon
```

### `max()` and `min()`
- **Purpose:** Returns the largest (max) or smallest (min) value in a collection.
```python
numbers = [10, 20, 30, 40]
print(max(numbers))  # Largest
print(min(numbers))  # Smallest
# Output: 40
#         10
```

### `round()`
- **Purpose:** Rounds a number to the nearest integer or specified decimal places.
```python
result = 3.14159
print(round(result, 2))  # Round to 2 decimal places
# Output: 3.14
```

### `abs()`
- **Purpose:** Returns the absolute value of a number.
```python
num = -5
print(abs(num))
# Output: 5
```

### `sum()`
- **Purpose:** Adds all elements in a list or collection.
```python
numbers = [1, 2, 3, 4]
print(sum(numbers))
# Output: 10
```

### `id()`
- **Purpose:** The `id()` function in Python returns the unique memory address of an object as an integer.
```python
x = 10
print(id(x))
```
