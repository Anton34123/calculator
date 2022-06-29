class Calculate:

    def fraction(self):
        """Дробь"""
        return float(input("Введите числитель: "))\
               / float(input("Введите знаменатель: "))

    def __init__(self):
        """Выражение"""

        not_true = True
        while not_true:
            type_calculate = input("Введите тип вычисления (дробь, не дробь): ")
            if type_calculate == "дробь":
                self.operand_1 = self.fraction()
                print("Результат первой дроби:",  self.operand_1)
                not_true = False
            elif type_calculate == "не дробь":
                self.operand_1 = float(input("Введие первый операнд: "))
                not_true = False
            else:
                print("убедитесь в правильности ввода")

        not_true = True
        while not_true:
            type_calculate = input("Введите тип вычисления (дробь, не дробь): ")
            if type_calculate == "дробь":
                self.operand_2 = self.fraction()
                print("Результат второй дроби:",  self.operand_2)
                not_true = False
            elif type_calculate == "не дробь":
                self.operand_2 = float(input("Введие второй операнд: "))
                not_true = False
            else:
                print("убедитесь в правильности ввода")

        not_true = True
        while not_true:
            self.operator = input("Введие оператор (+-*/): ")
            not_true = False if self.operator in "+-*/" else True

    def get_result(self):
        if self.operator == "+":
            return self.operand_1 + self.operand_2
        if self.operator == "-":
            return self.operand_1 - self.operand_2
        if self.operator == "*":
            return self.operand_1 * self.operand_2
        if self.operator == "/":
            return self.operand_1 / self.operand_2
