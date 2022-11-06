#amount due will always be 50(price of a coke)
amount_due = 50

#while loops = keep repeating if the outcome is true
while amount_due > 0:
    #print "Amount Due" string and then the value stored in "amount_due" variable
    print("Amount Due: " , amount_due)
    #ask for coin(must be an int)
    coin = int(input("Insert Coin: "))

    #[] this is a list
    #if coin is 25,10,5 then amount_due - coin
    if coin in [25, 10, 5]:
        amount_due -= coin

#abs() will always return positive value
change_owned = abs(amount_due)
print("Change Owned: " ,  change_owned)