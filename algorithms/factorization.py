from processing import Module


class Factorization(Module):
    def __init__(self, **input):
        self.number = input['number']  

    @staticmethod
    def _get_requirements():
        return {"number": {"prompt": "Integer value", "type":int}}

    @staticmethod
    def _get_output_type(func_name):
        options = {
            "multiple_division_factorization": 
                {"factors": {"prompt":"List of integer values being factors", "type":list}},
            "divisors_list": 
                {"divisors": {"prompt": "List of integer values begin divisors (including 1)", "type": list}},
            "perfect_number":
                {"inline-return": {"prompt": "True/False", "type":bool}}
        }
        return options[func_name]

    def multiple_division_factorization(self):
        number = self.number
        factors = []

        # BEGIN
        current_factor = 2
        while number > 1:
            if not number % current_factor:
                factors.append(current_factor)
                number //= current_factor
            else:
                current_factor += 1

        return factors
        # END

    def divisors_list(self):
        number = self.number
        divisors = []

        # BEGIN
        for i in range(1, number//2+1):
            if not number%i:
                divisors.append(i)
        return divisors
        # END

    def perfect_number(self):
        number = self.number

        # BEGIN
        self.factors = self.divisors_list()
        return sum(self.factors) == number
        # END
