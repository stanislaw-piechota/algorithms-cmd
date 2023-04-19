from processing import Module


class Primality(Module):
    def __init__(self, **input):
        self.number = input['number']


    @staticmethod
    def _get_requirements():
        return {"number": {"prompt": "Integer value", "type": int}}
    

    @staticmethod
    def _get_output_type():
        return {"inline-return": {"prompt":"True/False", "type": bool}}


    def naive_test(self):
        number = self.number

        for i in range(2, int(number**0.5)+1):
            if not number % i:
                return False
        return True
    