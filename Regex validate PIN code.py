def validate_pin(pin):
    print(pin)
    
    if len(pin) == 4 or len(pin) ==6:
        print("first if")
        if pin.isnumeric() == True:
            print("Second if")
            return True
        
    return False