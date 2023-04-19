from processing import Module


class Factorization(Module):
    def __init__(self, number):
        self.number = number
    

    @staticmethod
    def _get_requirements():
        return {"number": {"prompt": "Integer value", "type":int}}
    

    @staticmethod
    def _get_output_type():
        return {"factors": {"prompt":"List of integer values being factors", "type":list}}


    def multiple_test_division(self):
        number = self.number
        factors = []

        current_factor = 2
        while number > 1:
            if not number % current_factor:
                factors.append(current_factor)
                number //= current_factor
            else:
                current_factor += 1

        return factors
    
