### SOLID principle 

* just to double check and go thru

### Iterators and generators
* to extract theory essentials

### Decorators
* to extract theory essentials

```
def name_of_decor_func(function):
    def wrapper():
        ...
    return wrapper 
```
```
def decor_name(n):     # Declair decor's name with parameter for the decorator 
    def decorator(function):    # Declair decorator takes function which will decorate 
        def wrapper(*args, **kwargs):   # Logic implementation
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper 
    return decorator 
 
 
@repeat(4)
def say_hi():
    print("Hello")      
```