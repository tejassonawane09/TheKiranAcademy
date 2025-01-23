# `print` Function Attributes

## `value`
The object(s) to be printed. Multiple values can be separated by commas.  
**Required**

```python
print("Hello", "World")  # Prints multiple values
# Output: Hello World
```

## `sep`
Specifies the separator between multiple values.  
**Default:** `' '` (space)

```python
print("Python", "is", "fun", sep="-")
# Output: Python-is-fun
```

## `end`
Specifies what to print at the end of the output.  
**Default:** `'\n'` (newline)

```python
print("Hello", end=", ")
print("World!")
# Output: Hello, World!
```

## `file`
Specifies the file or stream to write the output.  
**Default:** `sys.stdout`

```python
with open("output.txt", "w") as f:
    print("Writing to a file", file=f)
# This writes "Writing to a file" into output.txt.
```

## `flush`
If `True`, forces the output to be written immediately.  
**Default:** `False`

```python
import time
for i in range(3):
    print(i, end=" ", flush=True)
    time.sleep(1)
```

## Key Notes
- `sep`: Change how values are separated (e.g., space, comma, hyphen).
- `end`: Customize what happens after the print (e.g., no newline, custom text).
- `file`: Redirect output (e.g., to a file).
- `flush`: Useful for real-time output (e.g., progress bars).
