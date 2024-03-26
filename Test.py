def get_op(op_list):
    while True:
        try:
            value = input(f"Podaj operacje: ")
            if value not in op_list:
                raise ZnakError("Błędny znak operacji! Może być tylko: +, -, *, /")
                break
        except:
            print("Wartość jest zła! Błędny znak operacji! Może być tylko: +, -, *, /")
    return value


op = get_op(["+", "-", "*", "/"])
