p1 = "click here"
p2 = "Buy now"
p3 = "Limited time offer"
p4 = "Subscribe today"
p5 = "Free gift inside"

comment = input("Enter your comment : ")

if (p1 in comment ) or (p2 in comment) or (p3 in comment) or (p4 in comment) or (p5 in comment):
    print("This is a spam comment")
    
else:
    print("This is not a spam comment")