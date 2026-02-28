def show():
    try:
        a = int(input("enter the number:"))
        print(a)
        return
    
    except Exception as e :
        print(e)
        return
        
    finally:    
        print("inside the finally")    
        
show()        