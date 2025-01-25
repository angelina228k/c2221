def divider(a, b):
    if a < b:
        raise ValueError("a менше, ніж b")
    if b > 100:
        raise IndexError("b більше 100")
    return a / b


data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key, value in data.items():
    try:

        if not isinstance(key, (int, float)) or not isinstance(value, (int, float)):
            raise TypeError(f"Некоректний тип даних: key={key}, value={value}")


        res = divider(key, value)
        result.append(res)
    except ZeroDivisionError:
        print(f"Ділення на нуль: key={key}, value={value}")
    except ValueError as e:
        print(f"ValueError: {e}, key={key}, value={value}")
    except IndexError as e:
        print(f"IndexError: {e}, key={key}, value={value}")
    except TypeError as e:
        print(f"TypeError: {e}, key={key}, value={value}")
    except Exception as e:
        print(f"Невідома помилка: {e}, key={key}, value={value}")

print("Результати:")