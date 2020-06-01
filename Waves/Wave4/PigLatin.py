vowels = ['a', 'e', 'o', 'i', 'u']

line = str(input("Please enter line: "))
newline = ""

for word in line.split():
    # In case of vowel
    if word[0] in vowels:
        newline += word + "way"
    # In case of consonant
    else:
        idx = 0
        goToEnd = word[0]
        for char in word[1:]:
            idx += 1
            if(char in vowels):
                newline += word[idx:] + goToEnd + "ay"
                break
            else:
                goToEnd += char

    newline += " "

print(newline)
