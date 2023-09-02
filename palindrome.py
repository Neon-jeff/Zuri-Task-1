# Ayo Wagmi!, this is an oop Implementation for a cascading palindrome checker

# ----------------User Guide-------------------
# avoid space when using numbers as inputs
# use such numbers as strings instead

class Checker():
    def __init__(self,param):
        # to initialize the params as attributes and call the validating func.
        param=self.validate_param(param)
        if param is None:
            raise Exception(f"Invalid input, input a number or a word")
        self.param=param

    def validate_param(self,input):
        # validates the user input
        if type(input) == int:
            # set the input to a string for manipulation with string methods
            input=str(input)
            return input
        if type(input) ==str:
            return input
        elif type(input) !=str or type(input) !=int:
            return None

    def checker(self):
        check_arr=self.param.split(' ')
        result=[]
        for word in check_arr:
            if word[::-1] == word:
                result.append(word)
        if len(result)==0:
            print("No palindrome word (number) found")
        return f"Found the following palindrome(s) {result}"



# A test object to use, change the input to any desired choice
word=Checker(1230321)

# test object result is gotten here
print(word.checker())
