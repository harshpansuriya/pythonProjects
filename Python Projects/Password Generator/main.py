import random

charachter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@$%^&*(`)"

while 1:
    pass_Len = int(input("How Many length of your password you want: "))

    pass_Count = int(input("How Many Password you want: "))

    for x in range(0, pass_Count):
        password = ""

        for x in range(0, pass_Len):
            pass_Char = random.choice(charachter)
            password = password + pass_Char
        
        print ("Your Password is: ", password)

        #Let's Run It. 

        #Your Passwords are ready you can use it anywhere.
        # Thank You for Watching. 😊