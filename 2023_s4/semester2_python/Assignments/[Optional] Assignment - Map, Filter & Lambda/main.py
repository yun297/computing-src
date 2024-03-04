def map_square_numbers(lst):
    return list(map(lambda x: x**2, lst))

def filter_even_numbers(lst):
    return list(filter(lambda x: x%2 == 0, lst))

def celsius_to_fahrenheit(lst):
    return list(map(lambda x: x * 9/5 + 32, lst))

def string_length_counter(lst):
    return list(map(lambda x: len(x), lst))

def is_prime(int):
    if int == 1:
        return False
    elif int == 2:
        return True
    else:
        for i in range(2, int):
            if int % i == 0:
                return False
        return True
    
def filter_prime_numbers(lst):
    return list(filter(is_prime, lst))

def map_capitalize_strings(lst):
    return list(map(lambda x: x.capitalize(), lst))