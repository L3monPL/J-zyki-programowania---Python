import random

def main():
    print("Witaj w systemie bankowym!")
    name_list, acc_num_list, acc_blc_list = read_file()
    option = 0
    while option != 6:

        # gui
        banking_menu = ["1. Otwórz konto", "2. Zamknij konto", "3. Wypłać gotówkę",
                        "4. Wpłać gotówkę", "5. Informacje menadrzera", "6. Wyjdź"]

        for option in banking_menu:
            print(option)
        user_input = False

       # sprawdzanie opcji
        while not user_input:
            try:
                option = int(input("Wybierz opcje:"))
                if 0 < option < 7:
                    user_input = True
                else:
                    print("\nWybierz poprawny numer\n")
                    for option in banking_menu:
                        print(option)
            except:
                print("\nWybierz poprawny numer\n")
                for option in banking_menu:
                    print(option)

# opcje menu 
        if option == 1:
            name_list, acc_num_list, acc_blc_list = open_acc(name_list, acc_num_list, acc_blc_list)

        elif option == 2:
            name_list, acc_num_list, acc_blc_list = shutdown_acc(name_list, acc_num_list, acc_blc_list)

        elif option == 3:
            name_list, acc_num_list, acc_blc_list = cash_out(name_list, acc_num_list, acc_blc_list)

        elif option == 4:
            name_list, acc_num_list, acc_blc_list = add_money(name_list, acc_num_list, acc_blc_list)

        elif option == 5:
            report(name_list, acc_num_list, acc_blc_list)

        elif option == 6:
            exit(name_list, acc_num_list, acc_blc_list)


# wczytanie pliku tekstowego
def read_file():
    name_list = []
    acc_num_list = []
    acc_blc_list = []

# nadpisanie pliku tekstowego
    f = open("bank.txt", "r")
    lines = f.readlines()
    for line in lines:
        information = line.split()
        acc_num_list.append(information[0])
        acc_blc_list.append(float(information[1]))
        name_list.append(information[2])
    return name_list, acc_num_list, acc_blc_list


# otwieranie konta
def open_acc(name_list, acc_num_list, acc_blc_list):
    name = input("Wprowadz swój login:")
    print("Twój login:", name)
    name_list.append(name)
    number = str(random.randint(1, 1000000))
    print("Twój numer konta to:", number)
    acc_num_list.append(number)
    acc_blc_list.append(0.0)
    return name_list, acc_num_list, acc_blc_list


# zamukanie konta
def shutdown_acc(name_list, acc_num_list, acc_blc_list):
    account_number = input("\nWprowadz numer konta:\n")
    index = 0
    found = False
    for i in acc_num_list:
        if i == account_number:
            found = True
            break
        index = index + 1
    if found:
        print("\nTwoje konto zostało zamkięte!", name_list[index], "\n")
        del acc_num_list[index]
        del acc_blc_list[index]
        del name_list[index]

    else:
        print("\nPodany numer konta nie istnieje!\n")
    return name_list, acc_num_list, acc_blc_list


# wypłacanie 
def cash_out(name_list, acc_num_list, acc_blc_list):
    account_number = input("\nWprowadz numer konta:\n")
    index = 0
    found = False
    for i in acc_num_list:
        if i == account_number:
            found = True
            break
        index = index + 1
    if found:
        problem = True
        while problem:
            try:
                withdraw_amount = float(input("Wprowadz saldo do wypłaty:"))
                # The Amount is the new amount the customer has withdrawn
                if withdraw_amount < 0:  # if not a positive int print message and ask for input again
                    print("Wprowadź ponowanie kwotę wypłaty!")
                    break
                amount = acc_blc_list[index] - withdraw_amount
                # if the amount is greater than or = 0 it will take the amount away from the balance list.
                if amount > 0:
                    acc_blc_list[index] = acc_blc_list[index] - withdraw_amount
                    print("Saldo ", "$", format(withdraw_amount, ".2f"), " zostało pobrane z Twojego konta! ",
                          account_number,
                          sep="")
                    print("Twój stan konta wynosi ", "$", format(acc_blc_list[index], ".2f"), sep="")
                    print("")
                    problem = False
                else:
                    print("Nie masz wystarczających funduszy!",
                          name_list[index])
                    print("Twoje saldo po bieżącej wypłacie wynosi ", "$",
                          format(acc_blc_list[index], ".2f"), sep="")
                    print("")
                    break
            finally:
                return name_list, acc_num_list, acc_blc_list
    else:
        print("\n Podany numer konta nie istnieje! \n")
        return name_list, acc_num_list, acc_blc_list


def add_money(name_list, acc_num_list, acc_blc_list):
    account_number = input("\Wprowadz numer konta:\n")
    index = 0
    found = False
    for i in acc_num_list:
        if i == account_number:
            found = True
            break
        index = index + 1
    if found:
        problem = True
        while problem:
            try:
                deposit_amount = float(input("Wprowadz saldo do wpłaty:"))
                # The Amount of customer chooses to deposit
                if deposit_amount < 0:  # if not a positive int print message and ask for input again
                    print("Wprowadź ponowanie kwotę wpłaty!")
                    break
                amount = acc_blc_list[index] + deposit_amount
                # if the amount is greater than or = 0 it will added to the balance list.
                if amount > 0:
                    acc_blc_list[index] = acc_blc_list[index] + deposit_amount
                    print("Saldo ", "$", format(deposit_amount, ".2f"), " zostało dodane do Twojego konta! ",
                          account_number,
                          sep="")
                    print("Twój stan konta wynosi ", "$", format(acc_blc_list[index], ".2f"), sep="")
                    print("")
                    problem = False
                else:
                    print("Wprowadz poprawnie dane",
                          name_list[index])
                    print("Twoje saldo po bieżącej wpłacie wynosi ", "$",
                          format(acc_blc_list[index], ".2f"), sep="")
                    print("")
                    break
            finally:
                return name_list, acc_num_list, acc_blc_list
    else:
        print("\n Podany numer konta nie istnieje! \n")
        return name_list, acc_num_list, acc_blc_list


# dodatkowy raport
def report(name_list, acc_num_list, acc_blc_list):
    for i in range(len(acc_num_list)):
        print("\nKlient ", name_list[i], " którego numerem konta jest ", acc_num_list[i], "posiada $", acc_blc_list[i])
        total = sum(acc_blc_list)
    print("\nCałkowita kwota wpłat do banku wynosi", format(total, ".2f"))
    #largest_deposit = max(acc_blc_list)
    #print("\nNajwiększa wpłata wynosi $", str(largest_deposit), "i należy do " + (name_list[i] + "\n"))


def exit(name_list, acc_num_list, acc_blc_list):
    print("Dziękujemy za skorzystanie z naszych usług!")
    quit_file = open("bank.txt", "w")
    for i in range(len(acc_num_list)):
        save = acc_num_list[i] + " " + str(acc_blc_list[i]) + " " + name_list[i] + "\n"
        quit_file.write(save)
    quit_file.close()


main()
