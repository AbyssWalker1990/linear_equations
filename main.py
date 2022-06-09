class Equation:

    def __init__(self, equation):
        self.equation = equation

    """Method that dividing equations into 2 lists and preparing these objects for 
    formatting and converting into right types    
    """

    def divide_equation(self):
        # Creating 2 lists with left and right sides of equation
        equation_list_left = []
        equation_list_right = []
        for i in self.equation:
            if i == "=":
                break
            equation_list_left.append(i)
        length = len(equation_list_left)
        # Adding garbage symbol for further filtering purpose in the loops in numbers_unite() method
        equation_list_left.append("$")

        count = 0
        for i in self.equation:
            count += 1
            if count > length + 1:
                equation_list_right.append(i)
        # Adding garbage symbol for further filtering purpose in the loops in numbers_unite() method
        equation_list_right.append("$")

        # Uniting string number together and adding to the new proper lists
        proper_equation_list_left = self.numbers_unite(equation_list_left)
        proper_equation_list_right = self.numbers_unite(equation_list_right)
        self.find_type_of_equation(proper_equation_list_left, proper_equation_list_right)

    @staticmethod
    def numbers_unite(equation_side):
        """Uniting all numbers, that for now are divided, into 1 object
        and adding it to a new list, ready for further actions to get result
        """
        proper_equation_side = []
        digit = []
        count = 1  # Counter for separate "-" symbol from index 0 from another indexes
        for i in equation_side:
            if i.isdigit():
                digit.append(i)
            elif not i.isdigit() and i == "-" and count == 1:
                digit.append(i)
            elif not i.isdigit():
                number = "".join(digit)
                if number != "":
                    proper_equation_side.append(number)
                proper_equation_side.append(i)
                digit = []
            else:
                print("Error")
            count += 1
        proper_equation_side.remove("$")
        return proper_equation_side

    @staticmethod
    def find_type_of_equation(left_side, right_side):

        length_left = len(left_side)
        length_right = len(right_side)
        """Fix an issue with minus symbol before number, that causes exception.
        Forcing search for minus and if it exists - convert string object into
        float with this minus
        """

        for i in left_side[0]:
            if i == "-":
                x = left_side[0].lstrip("-")
                left_side[0] = float(x) - float(x) * 2

        # Creating list with variables for further calculations in SimpleEquation class
        prep_value = Equation.preparing_values_for_simple(left_side, right_side)
        # Simple equation with *
        if length_left == 2 and length_right == 1:
            print("Simple equation with *")
            a, b = prep_value[0], prep_value[1]
            SimpleEquation(a, b, is_simple=True, orientation=False)
        elif length_left == 1 and length_right == 2:
            a, b = prep_value[0], prep_value[1]
            SimpleEquation(a, b, is_simple=True, orientation=True)
        # Simple equation with all another basic math operators
        elif length_left == 3 and length_right == 1 and left_side[0] != "x":
            a, b = prep_value[0], prep_value[1]
            math_operator = prep_value[2]
            SimpleEquation(a, b, math_operator=math_operator, orientation=False)
        elif length_left == 3 and length_right == 1 and left_side[0] == "x":
            a, b = prep_value[0], prep_value[1]
            math_operator = prep_value[2]
            SimpleEquation(a, b, math_operator=math_operator, orientation=True)
        else:
            print("other variation")

    @staticmethod
    def preparing_values_for_simple(left_side, right_side):
        """Checking for the right values for simplest equations like 4x=8
        and creating a list
        """
        math_operators = ("+", "-", "/", "*")
        operator = "$"      # Defining operator to avoid error if it will not be define while checking
        is_math_operator_left = False
        is_math_operator_right = False
        equation_variable = "x"
        values = []

        # Checking if we have math operators in both sides of equation
        for i in math_operators:
            for item in left_side:
                if i == item:
                    is_math_operator_left = True
            for item in right_side:
                if i == item:
                    is_math_operator_right = True
        # packing numbers in the right variables and creating a list
        if not is_math_operator_left and not is_math_operator_right:
            if left_side[0] != equation_variable:
                a = float(left_side[0])
            else:
                a = float(left_side[1])
            if right_side[0] != equation_variable:
                b = float(right_side[0])
            else:
                b = float(right_side[1])
        elif is_math_operator_left and left_side[0] != equation_variable:
            a = float(left_side[0])
            b = float(right_side[0])
            operator = left_side[1]
        elif is_math_operator_left and left_side[0] == equation_variable:
            a = float(left_side[2])
            b = float(right_side[0])
            operator = left_side[1]
        elif is_math_operator_right:
            a = float(right_side[0])
            b = float(left_side[0])
            operator = right_side[1]
        elif is_math_operator_right and right_side[0] != equation_variable:
            a = float(right_side[2])
            b = float(left_side[0])
            operator = right_side[1]
        values.append(a)
        values.append(b)
        values.append(operator)
        return values


class SimpleEquation:
    """Initializing this object from formatted previously input.
    Contains methods that can solve simplest equations.
    """
    def __init__(self, a, b, is_simple=False, math_operator="", orientation=False):
        self.orientation = orientation
        self.math_operator = math_operator
        self.is_simple = is_simple
        self.b = b
        self.a = a

        if is_simple:
            self.simple_multiply()
        else:
            self.simple_non_multiply()

    def simple_multiply(self):
        # Result for standart (like 2x=4)
        result = self.b / self.a
        # Printing process for reversed (4=2x) or standart (2x=4)
        if self.orientation:
            result = self.a / self.b
            print("x=" + str(self.a) + "/" + str(self.b))
        else:
            print("x=" + str(self.b) + "/" + str(self.a))
        print(f"x={result}")

    def simple_non_multiply(self):

        if self.math_operator == "+":
            print(f"x={self.b}-{self.a}")
            result = self.b - self.a
        elif self.math_operator == "-":
            print(f"x={self.a}-{self.b}")
            result = self.a - self.b
        elif self.math_operator == "/" and not self.orientation:
            print(f"x={self.a}/{self.b}")
            result = self.a / self.b
        elif self.math_operator == "/" and self.orientation:
            print(f"x={self.b}/{self.a}")
            result = self.b * self.a
        print(result)


if __name__ == "__main__":
    while True:
        inp = input("Введіть рівняння: ")
        exercise = Equation(inp)
        exercise.divide_equation()
