import random
class Encryptor:
    def __init__(self, *numbers):

     self.__numbers = list(numbers)
        self.__result = None

    def __perform_random_operation(self):
        """
        Виконує випадкову математичну операцію над числами.
        Операції: додавання, множення, різниця, середнє значення.
        """
        operation = random.choice(["sum", "product", "difference", "average"])
        if operation == "sum":
            self.__result = sum(self.__numbers)
        elif operation == "product":
            self.__result = 1
            for num in self.__numbers:
                self.__result *= num
        elif operation == "difference":
            self.__result = self.__numbers[0]
            for num in self.__numbers[1:]:
                self.__result -= num
        elif operation == "average":
            self.__result = sum(self.__numbers) / len(self.__numbers)

    def __str__(self):

        self.__perform_random_operation()
        return f"Результат обчислень: {self.__result}"

if __name__ == "__main__":

    encryptor = Encryptor(10, 20, 30)

    try:
        print(encryptor.__numbers)
    except AttributeError:
        print("Числа приховані. Прямий доступ заборонений!")
 print(encryptor)
    print(encryptor)