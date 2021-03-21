def number_of_bottles():
    for i in range (100):
        saldo = 99 - i
        if saldo == 0:
            print("No more bottles of milk on the wall, no more bottles of milk.")
            print("Go to the store and buy some more, 99 bottles of milk on the wall.\n")
        elif saldo == 1:
            print(str(saldo) + " bottle of milk on the wall, " + str(saldo) + " bottle of milk.")
            print("Take one down and pass it around, no more bottles of milk on the wall.")
        else:
            print(str(saldo) + " bottles of milk on the wall, " + str(saldo) + " bottles of milk.")
            print("Take one down and pass it around, " + str(saldo - 1)+ " bottles of milk on the wall.\n")

number_of_bottles()