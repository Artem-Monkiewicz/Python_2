# 27 = esc
# 299 lewo
# 301 prawo
# 296 gora
# 304 dol

import msvcrt


def get_key():
    if msvcrt.kbhit():
        key = ord(msvcrt.getch())
        if key == 27:  # ESC
            return None
        return key
    return None


if __name__ == "__main__":
    while True:
        key = get_key()
        if key is not None:
            print(f"Pressed key: {key}")
