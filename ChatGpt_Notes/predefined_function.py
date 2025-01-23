#Predefined Functions in Python
'''Predefined functions are the functions provided by Python that you can use directly without creating them. 
They help perform common tasks quickly and efficiently.'''

#Common Predefined Functions
print()
    # Purpose: Displays output on the screen.
print("Hello, World!")
    # Output:Hello, World!
    
    
#len()
    # Purpose: Returns the number of elements in a string, list, or other collections.
text = "Hello"
print(len(text))
    # Output:6 
    

#type()
    # Purpose: Returns the data type of a variable.
num = 10
print(type(num))
    # Output: <class 'int'>
    
    
#input()
    #Purpose: Takes input from the user.
name = input("Enter your name: ")
print("Hello, " + name)
    # Output: Enter your name: Kanon
    # Hello, Kanon
    
    
#max() and min()
    #Purpose: Returns the largest (max) or smallest (min) value in a collection.
numbers = [10, 20, 30, 40]
print(max(numbers))  # Largest
print(min(numbers))  # Smallest
    #Output:40 10
    
      
#round()
    #Purpose: Rounds a number to the nearest integer or specified decimal places.
result = 3.14159
print(round(result, 2))  # Round to 2 decimal places
    #Output:3.14
    
    
#abs()
    #Purpose: Returns the absolute value of a number.
num = -5
print(abs(num))
    #Output: 5
        
    
#sum()
    #Purpose: Adds all elements in a list or collection.
numbers = [1, 2, 3, 4]
print(sum(numbers))
    #Output:10
    
#id()
    #Purpose:The id() function in Python returns the unique memory address of an object as an integer.
x = 10
print(id(x))
