import random as r


def list_maker(tnt):
    for i in range(1, 10):
        num = r.randint(1, 50)
        Num_list.append(num)

    print(tnt, Num_list)


def Average(txt):
    x = 0
    lenght = len(Num_list)
    print(f"The lenght of list: {lenght}")
    for i in Num_list:
        x = x + i
    print (f"this is x= {x} and this is len= {lenght}")
    Average = x / lenght
    print(f"{txt}{Average}")


def main():
    global Num_list
    Num_list = []
    list_maker("The List of numbers: ")
    Average("The Average of list is: ")


if __name__ == "__main__":
    main()