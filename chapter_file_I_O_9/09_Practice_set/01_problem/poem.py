with open("poem.txt","r") as f:
    data = f.read()
    if ("twinkle" in data):
        print("twinkle is present")
    else:
        print("twinkle id not present")
         f.close()