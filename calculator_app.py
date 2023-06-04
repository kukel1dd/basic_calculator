"""A calulator class that preforms all of the basic operations."""
class Calculator:
    def __init__(self, number0, number1):
        stored_answer = 0
        self.number0 = number0
        self.number1 = number1

    def addition( number0, number1, stored_answer=None):
        """A simple function for addition"""
        try:
            answer = (number0) + (number1)
            print(answer)
            return answer
            # stored_answer += answer
        except(ValueError):
            answer = float(number0) + float(number1)
            print(answer)
            return answer
        #         # answer += stored_answer
        #     except(ValueError):
        #         print("Please don't use letters.")
    
    
    def subtraction( number0, number1):
        """A simple function for subtraction."""
        try:
            answer = int(number0) - int(number1)
            print(answer)
            return answer
        except(ValueError):
            answer = float(number0) - float(number1)
            print(answer)
            return answer



    def multiplication( number0, number1):
        """A simple function for multiplication."""
        if number0 is int or number1 is int:

            try:
                answer = int(number0) * int(number1)
                print(answer)
                return answer
            except(ValueError):
                answer = float(number0) * float(number1)
                print(answer)
                return answer
        else:
            answer = float(number0) * float(number1)
            if (answer).is_integer() == True:
                answer = int(answer)
                print(answer)
                return answer
            else:
                answer = round(answer,3)
                print(answer)
                return answer


    def division(number0, number1):
        """A function for division that will give you an int as output if you get a whole number."""
        zerodizisionerror = ''
        try:
            answer = number0 / number1
            if (answer).is_integer() == True:
                print(int(answer))
                print('Here1')
                return answer
            else:
                answer = round(answer, 3) 
                print("Here2")
                print(answer)
                return round(answer,3)

        except( ValueError, ZeroDivisionError):
            if number1 == 0:
                print("Zero division error")
            else:
                answer = float(number0)/ float(number1)
                if (answer).is_integer() == True:
                        print("3")
                        print(int(answer))
                        return answer
                elif (answer).is_integer() == False:
                        answer = round(answer, 3) 
                        print("4")
                        print(answer)
                        return round(answer, 3)
                else:
                    print('I dont know how you got here.')
                    pass    
    
    def choose_operation(opperator):
        """A function to choose which opperation you want to invoke."""
        if opperator == '+':
            Calculator.addition(number0=None, number1=None)
        elif opperator == "-":
            Calculator.subtraction(number0=None, number1=None)
        elif opperator == "*":
            Calculator.multiplication(number0=None, number1=None)
        elif opperator == "/":
            Calculator.division(number0=None, number1=None)
        elif opperator == None:
            pass
        else:
            print("Sorry...")


    def convert(number0,number1):
        number0 = int(number0)
        number1 = int(number1)

Calculator.division(number0=0, number1=9)
