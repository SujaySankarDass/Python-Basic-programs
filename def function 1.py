# def create_pin():

# create_pin()

def login():
    attempts =0
    max_attempts = 3
    while max_attempts > attempts:
        pin=input("Enter your pin:")
        if len(pin) == 4 and pin.isdigit():
            pin = int(pin)
            print("Login successful !")
            break
        else:
            print("wrong pin, try again")
            if attempts == max_attempts:
                print("wrong pin, try again")
                print("Maximum attempts reached. Please try again later.")
                break
            attempts += 1
    return pin
login()