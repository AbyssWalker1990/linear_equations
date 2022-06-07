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

    def numbers_unite(self, equation_side):

        self.equation_site = equation_side
        proper_equation_side = []
        digit = []

        for i in equation_side:
            if i.isdigit():
                digit.append(i)
            elif not i.isdigit():
                number = "".join(digit)
                if number != "":
                    proper_equation_side.append(number)
                proper_equation_side.append(i)
                digit = []
            else:
                print("Error")
        proper_equation_side.remove("$")
        return proper_equation_side

    def find_type_of_equation(self, left_side, right_side):

        length_left = len(left_side)
        length_right = len(right_side)
        a = float(left_side[0])
        b = float(right_side[0])

        # Simple equation with *
        if length_left == 2 and length_right == 1:
            print("Simple equation with *")
            SimpleEquation(a, b, is_simple=True)

        # Other variations of simple equations
        elif length_left == 3 and length_right == 1:
            print("ololo")
            math_operator = float(left_side[1])
            SimpleEquation(a, b, math_operator=math_operator)


class SimpleEquation:

    def __init__(self, a, b, is_simple=False, math_operator=""):
        self.math_operator = math_operator
        self.is_simple = is_simple
        self.b = b
        self.a = a

        if is_simple:
            self.simple_multiply()
        else:
            self.simple_non_multiply()

    def simple_multiply(self):
        result = self.b / self.a
        print("x=" + str(self.b) + "/" + str(self.a))
        print(f"x={result}")

    def simple_non_multiply(self):

        if self.math_operator == "-":
            if self.a < self.b:
                print("oops")
            else:
                result = self.a - self.b
                print(result)


if __name__ == "__main__":
    exercise = Equation("2x=4")
    exercise.divide_equation()
