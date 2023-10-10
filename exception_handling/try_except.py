# exception are the user side error
# # try except block is used to display the error to the user


# while True:
#     try:
#         x=int(input("enter the number"))
#         y=int(input("enter the second number"))
#         z=x/y
#         print(f"div = {z}")
#         break

#     except ZeroDivisionError:
#         print("cannot divible by zero")
#     except TypeError:
#         print("enter correct value")
#     except ValueError:
#         print("enter a valid number")
#     finally:
#         print("thank u")
    
while True:
    try:
        x=int(input("enter a number"))
        if x%2==0:
            print(f"{x} is even number")
            break
        else:
            print(f"{x} is an odd number")
            

    except TypeError:
        print("enter correct value")
    except ValueError:
        print("enter valid number")
    finally:
        print("thank u")
