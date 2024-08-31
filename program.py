from messages import *


def fun0(message: dict):
    if message.get("type") == "AccountCreated":
        print("if - first branch")
    elif message.get("type") == "AccountDeleted":
        print("if - 2nd branch")
    elif message.get("type") == "AccountUpdated":
        print("if - 3rd branch")
    else:
        print("if - else, nothing")


def fun1(message):
    match message:
        case {"type": "AccountCreated"}:
            print("matched first", message)
        case {"type": "AccountDeleted"}:
            print("matched second", message)
        case {"type": "AccountUpdated"}:
            print("matched 3rd", message)
        case _:
            print("matched nothing")


if __name__ == '__main__':
    for m in c, d, u1, u2, mal:
        fun0(m)

    for m in c, d, u1, u2, mal:
        fun1(m)


