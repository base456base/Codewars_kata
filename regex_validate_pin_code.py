"""   
    ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot 
   contain anything but exactly 4 digits or exactly 6 digits.

   Example
    "1234"   -->  true
    "12345"  -->  false
    "a234"   -->  false

"""

def validate_pin(pin):
    return pin.isdigit() and len(pin) in (4,6)

print(validate_pin("123a"))