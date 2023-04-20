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

    def perfect_number(self):
        number = self.number

        # BEGIN
        self.factors = self.multiple_division_factorization()
        return sum(self.factors) == number
        # END
