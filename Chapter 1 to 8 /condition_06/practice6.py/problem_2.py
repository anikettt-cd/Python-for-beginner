sub1 = int(input("Enter marks obtained in subject: "))
sub2 = int(input("Enter maximum marks for the subject: "))
sub3 = int(input("Enter marks obtained in subject: "))

percentage = ((sub1 + sub2 + sub3) / 300) * 100

if percentage >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33:
    print("You have passed the exam: percentage =", percentage)
else:
    print("You have failed the exam.")
