VOWELS = "aeiou"
while True: 
    word = input("Enter a word ('quit' to quit): \n")
    word_low = word.lower()
    if word_low != "quit":
        
        if word_low[0] in VOWELS:
            pigword = word_low + "way"
        else:
            if len(word_low) == 1:
                pigword = word_low +"ay" 
            for index, ch in enumerate(word_low):
                if ch in VOWELS:
                    a = index
                    pigword = word_low[a:] + word_low[:a] + "ay"
                    break
        print(pigword)
    else:
        break
        
# Error message used in Coding Rooms test
#print("Can't convert empty string.  Try again.")