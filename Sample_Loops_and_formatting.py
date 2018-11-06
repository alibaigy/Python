# Some class examples

number = float(input("Enter a number: "))

while number >= 1:
    print("number: ", number,"___", number / 2.0)
    number -= 1

# ------ Example menu 1
    
choice = input("Enter your choice (1,2,3,4): ")

while choice != '4':
    if choice == '1':
        print("You selected 1 ...")
    elif choice == '2':
        print("You selected 2 ...")
    elif choice == '3':
        print("You selected 3 ...")
        
    choice = input("Enter your choice (1,2,3,4): ")

    
# ------ Example menu 2    
  
while True:
    
    choice = input("Enter your choice (1,2,3,4): ")
    
    if choice == '1':
        print("You selected 1 ...")
    elif choice == '2':
        print("You selected 2 ...")
    elif choice == '3':
        print("You selected 3 ...")
    elif choice == '4':
        break


# ------ Example multiplication table  
number = int(input("Enter am integer: "))

for row in range(1,number+1):
    for col in range(1, 11):
        print('{:5d}'.format(row * col), end = "") 
    print()

# ------ Example string formatting 
Sal01 = 40000
Sal02 = 50000
print("The employee salary is between {} and {}".format(Sal01,Sal02))
print("The employee salary is between {:.2f} and {:.2f}".format(Sal01,Sal02))
    
    
    