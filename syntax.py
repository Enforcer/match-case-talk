class Coffee:
    pass


class Tea:
    pass

latte = Coffee()

match latte:
    case Coffee():
        print("It's caffee latte or latte machiato!")
    case Tea():
        print("It's Matcha Latte")
    case _:
        print("Huh, no idea what is it")

