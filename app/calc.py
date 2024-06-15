import app
import math


class InvalidPermissions(Exception):
    pass


class Calculator:
    def add(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Los argumentos deben ser de tipo int o float")
        return x + y


    def subtract(self, x, y):
        self.check_types(x, y)  # Verificar que x e y sean números
        return x - y

    def multiply(self, x, y):
        if not app.util.validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissions('User has no permissions')

        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_types(x, y)  # Verificar que x e y sean números
        if y == 0:
            raise ValueError("Division by zero is not possible")
        return x / y

    def power(self, x, y):
        self.check_types(x, y)
        return x ** y

    def square_root(self, x):
        self.check_type(x)
        if x < 0:
            raise ValueError("Square root is not defined for negative numbers")
        return math.sqrt(x)

    def log_base_10(self, x):
        self.check_type(x)
        if x <= 0:
            raise ValueError("Logarithm is not defined for non-positive numbers")
        return math.log10(x)

    def check_types(self, *args):
        for arg in args:
            try:
                float_arg = float(arg)  # Convertir el argumento a float
            except ValueError:
                raise TypeError("Parameters must be numbers")
            if not isinstance(float_arg, (int, float)):
                raise TypeError("Parameters must be numbers")

    def check_type(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("Parameter must be a number")


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print(result)
