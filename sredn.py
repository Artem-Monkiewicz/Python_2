if __name__ == "__main__":
    a = 5
    b = 0
    try:
        result = a / b
        print(f"result{result}")
    except ValueError:
        print("Nie dzieli  się przez zero!")
    finally:
        print("Finally")
print("Koniec")
