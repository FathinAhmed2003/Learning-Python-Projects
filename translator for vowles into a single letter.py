def translator(x):
    translation = ""
    for letter in x:
        if letter in "AEIOUYaeiouy":
            translation = translation + "k"
        else:
            translation = translation + letter
    return translation


print(translator(input("Phrase to translate: ")))
