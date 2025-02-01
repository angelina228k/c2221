import re


def safe_calculator(func):
    def wrapper(expression):
        try:

            if not re.match(r'^[\d+\-*/().\s]+$', expression):
                raise ValueError("Некоректний вираз: містить заборонені символи.")

            return func(expression)
        except ZeroDivisionError:
            return "Помилка: Ділення на нуль."
        except SyntaxError:
            return "Помилка: Синтаксична помилка у виразі."
        except ValueError as e:
            return f"Помилка: {e}"
        except Exception as e:
            return f"Невідома помилка: {e}"

    return wrapper


#safe_calculator
def calculate(expression):
    return eval(expression)


print(calculate("10 + 5 * 2"))  # 20
print(calculate("10 / 0"))
print(calculate("10 + abc"))
print(calculate("10 // 3"))