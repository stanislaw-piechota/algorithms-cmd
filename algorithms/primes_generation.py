from processing import Module

class Primes_generation(Module):
    def __init__(self, **input):
        self.max_number = input['n']

    @staticmethod
    def _get_requirements():
        return {'n': {"type": int, "prompt": "Boundary of set [2, n]"}}
    
    @staticmethod
    def _get_output_type(func_name):
        options = {
            "eratosthenes_sieve": 
                {'primes': {"type": list, "prompt": "List of prime numbers between [2, n]"}},
            "upgraded_eratosthenes_sieve": 
                {'primes': {"type": list, "prompt": "List of prime numbers between [2, n]"}}
        }
        return options[func_name]
    
    def eratosthenes_sieve(self):
        n = self.max_number
        primes = []

        # BEGIN
        booleans = [False, False] + [True for _ in range(2, n+1)]
        multiple_limit = int(n**0.5)
        
        for number in range(2, multiple_limit+1):
            if not booleans[number]: continue
            multiple = number**2
            while multiple <= n:
                booleans[multiple] = False
                multiple += number
        for number in range(2, n+1):
            if booleans[number]: primes.append(number)

        return primes
        # END

    def upgraded_eratosthenes_sieve(self):
        n = self.max_number
        primes = [2]

        # BEGIN
        m = n//2
        booleans = [True for _ in range(m)]
        index = 1
        p, q = 3, 4

        while q < m:
            if booleans[index]:
                k = q
                while k < m:
                    booleans[k] = False
                    k += p
            index += 1
            p += 2
            q += p//2 - 2
        for i in range(1, m):
            if booleans[i]:
                primes.append(2*i+1)

        return primes
        # END
