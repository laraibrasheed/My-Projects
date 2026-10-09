ones = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
        "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
        "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19}
tens = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90}
multipliers = {"thousand": 1000, "million": 1000000, "billion": 1000000000}

def words_to_number(text):
    words = text.lower().replace("-", " ").split()
    total = 0
    perform = 0

    for word in words:
        if word in ones:
            perform += ones[word]
        elif word in tens:
            perform += tens[word]
        elif word == "hundred":
            perform *= 100
        elif word in multipliers:
            perform *= multipliers[word]
            total += perform
            perform = 0
        elif word == "and": continue
        else:
            raise ValueError(f"Unknown word: {word}")
    return total + perform

word_input = input("Enter number in words: ")
result = words_to_number(word_input)
print("Number: ", result)