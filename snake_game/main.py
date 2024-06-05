from getkey import get_key

if __name__ == "__main__":
    my_get_key = get_key()

    while True:
        key = my_get_key()
        if key != 0:
            print(key)
        print(key)
        if key == 27:
            break
