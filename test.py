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