if Bet == 'red':
        if Score in Red:
            print(f"You win! +{Amount}")
            print(f"Your new balance is: ${Balance + int(Amount)}")
            Balance += int(Amount)

    elif Bet == 'black':
        if Score in Black:
            print(f"You win! +{Amount}")
            print(f"Your new balance is: ${Balance + int(Amount)}")
            Balance += int(Amount)

    elif Bet == 'green':
        if Score in Green:
            print(f"You win! +{Amount * 14}")
            print(f"Your new balance is: ${Balance + int(Amount * 14)}")
            Balance += int(Amount * 14)

    elif Bet == 'odd':
        if (Score & 1) != 0:
            print(f"You win! +{Amount}")
            print(f"Your new balance is: ${Balance + int(Amount)}")
            Balance += int(Amount)

    elif Bet == 'even':
        if (Score & 1) == 0:
            print(f"You win! +{Amount}")
            print(f"Your new balance is: ${Balance + int(Amount)}")
            Balance += int(Amount)
    
    elif Bet in Score:
        print(f"You win! +{Amount * 36}")
        print(f"Your new balance is: ${Balance + int(Amount * 36)}")
        Balance += int(Amount * 36)