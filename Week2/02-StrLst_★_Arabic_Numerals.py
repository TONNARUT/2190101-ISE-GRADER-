"""
def number_to_words_no_library(number):
     words = {
        "0": "zero", "1": "one", "2": "two", "3": "three", 
        "4": "four", "5": "five", "6": "six", "7": "seven", 
        "8": "eight", "9": "nine"
    }
     return " ".join(words[digit] for digit in number if digit.isdigit())

number = input()
result = number_to_words_no_library(number)
print(number,"-->",result)
"""

def number_to_words(n):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    return words[n]
n = int(input())
result = number_to_words(n)
print(n,"-->",result)
