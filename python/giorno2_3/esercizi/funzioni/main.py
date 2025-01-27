def pow_list(values):
    return [value ** 2 for value in values]
result = pow_list([1,2,3])
print(result)

def count_words(given_str):
    words = given_str.split()
    return len(words)
given_str = "hello world"
print(count_words(given_str))

def reverse_string(rstr):
    # Check if the input is None
    if rstr is None:
        return "Invalid input"
    # Check if the input is a number
    if isinstance(rstr,(int, float)):
        rstr = str(rstr)
    #check if the input is a string
    if isinstance(rstr,str):
        return "".join(reversed(rstr))

print(reverse_string("hello"))
print(reverse_string("1234"))
print(reverse_string(None))

def factorial(n):
    if n == 0:
        return 1
    if n < 0:
        return "It is not possible to define factorials for negative number"
    result = 1
    for i in range (1, n + 1):
        result *= i
    return result

print(factorial(5))

def is_palindrome (pstr):
    if pstr == pstr[::-1]:
        return True
    else:
        return False

text1 = "racecar"
print(is_palindrome(text1))

def sum_even_numbers(n):
    total = 0
    for num in n:
        if num % 2 == 0:
            total += num
    return total

numbers1 = [1,2,3,4,5]
print(sum_even_numbers(numbers1))

def find_max (numbers):
     bigger = max(numbers)
     return bigger

numbers2 = [3, 1, 4, 1, 5]
print(find_max(numbers2))

def count_vowels(vow):
    if isinstance(vow, str):
        vowels = "aeiou"
        count = 0
        for words in vow:
            if words.lower() in vowels:
                count += 1
        return count
    if isinstance(vow,int):
        return "This function is not applicable to numbers"
print(count_vowels("hello"))
print(count_vowels(1))



















