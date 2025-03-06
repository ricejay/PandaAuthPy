# PandaAuthPy

PandaAuthPy is a Panda-Auth library for Python 🐍

## Installation
Install the package using pip:
```sh
pip install PandaAuthPy
```

## Usage
Import the module and create an instance of `PandaAuth`:
```python
from PandaAuth import PandaAuth

auth = PandaAuth()
```

### 1. Get Key
Generates a key URL for your service.
```python
service_name = "your_service"
print(auth.get_key(service_name))
```
**Returns:** A URL where the user can get the key.

### 2. Validate Key
Checks if the given key is valid.
```python
key = input("Enter your key: ")
if auth.validate_key(key, service_name):
    print("Key is valid.")
else:
    print("Key is invalid.")
```
**Returns:** `True` if the key is valid, otherwise `False`.

### 3. Validate Premium Key
Checks if the given key has premium access.
```python
key = input("Enter your key: ")
if auth.validate_premium_key(key, service_name):
    print("Key is premium.")
else:
    print("Key is not premium.")
```
**Returns:** `True` if the key has premium status, otherwise `False`.

### 4. Example
```python
from PandaAuthPy import PandaAuth

if __name__ == "__main__":
    auth = PandaAuth()
    
    service_name = "your_service"
    
    print(auth.get_key(service_name)) # Prints the key URL
    key = input("Enter your key: ")
    if auth.validate_key(key, service_name):
        if auth.validate_premium_key(key, service_name):
            print("Key is valid and premium.") # Return if key is premium
        else:
            print("Key is valid but not premium.") # Return if key is not premium
    else:
        print("Invalid key.") # Return if key is not valid
```