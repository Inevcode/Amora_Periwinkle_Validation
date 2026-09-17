#1.
seasons = ["spring", "summer", "fall", "winter"] #The choices
while True: #This is so the user can input again if the data is invalid
    favoriteSeason = input("Enter your favorite season: ")
    if favoriteSeason.lower() in seasons: #Checks if the inputted season is part of the choices
        print(f'Your favorite season is {favoriteSeason}')
        break
    elif favoriteSeason.lower() not in seasons:
        print("Invalid Season!")

#2.
while True:
    try: #Checks if the data type is invalid
        itemPrice = float(input("Enter the price of your item: "))
        if itemPrice > 0:
            print(f'The price of your item is {itemPrice: 2f}.')
            break
        else:
            print("Invalid price!")
    except:
        print("Invalid data!")
    
    

