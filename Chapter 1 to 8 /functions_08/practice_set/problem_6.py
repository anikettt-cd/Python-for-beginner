def inches_to_cm(inch):
    if (inch==0):
        return 0
    else:
        return (2.54 * inch)
    
n = int(input("enter the valuse of inch:"))

print(f"the corrsponding valuse for cm is : {inches_to_cm(n)} cm")