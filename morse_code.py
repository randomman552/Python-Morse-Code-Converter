import sys
import os

#Morse code translation dict
translation_dict = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}
#Extra characters, these are not in morse code
extra_chars = {
    " ": "[SPACE]",
    ",": "[COMMA]",
    "?": "[QUESTION]",
    "!": "[EXCLAMATION]",
    ".": "[STOP]",
    "-": "[MINUS]",
    "+": "[ADD]",
    "=": "[EQUAL]",
    "/": "[DIVIDE]",
    "<": "[LESS-THAN]",
    ">": "[GREATER-THAN]",
    "\\": "[BACKSLASH]",
    "(": "[OPEN-BRACKET]",
    ")": "[CLOSE-BRACKET]",
    "[": "[OPEN-SQUARE-BRACKET]",
    "]": "[CLOSE-SQUARE-BRACKET]",
    "{": "[OPEN-CURLY-BRACKET]",
    "}": "[CLOSE-CURLY-BRACKET]",
    "'": "[APOSTROPHE]",
    "#": "[HASH]",
    ":": "[COLON]",
    ";": "[SEMI-COLON]",
    "_": "[UNDERSCORE]",
    '"': "[SPEECH]",
    "£": "[POUND]",
    "$": "[DOLLAR]",
    "%": "[PERCENT]",
    "^": "[EXPONENT]",
    "&": "[AND]",
    "*": "[ASTERIX]",
    "~": "[SQUIGLE]",
    "@": "[AT]",
}
#Alphabet dict used for checking whether is morse code or not.
alphabet = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "v": 0,
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0,
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
}

def morse_to_eng(text):
    text = text.split()
    output = ""
    for item in text:
        for key in translation_dict:
            if item == translation_dict[key]:
                output += key
                break
        for key in extra_chars:
            if item.lower() == extra_chars[key].lower():
                output += key
                break
    return output

def eng_to_morse(text, use_extra_chars=False):
    output = ""
    for char in text:
        if char.lower() in translation_dict:
            output += translation_dict[char.lower()] + " "
        elif char.lower() in extra_chars and use_extra_chars:
            output += extra_chars[char.lower()] + " "
    return output[:len(output) - 1]

def is_it_morse(text):
    for letter in alphabet:
        alphabet[letter] = text.count(letter)
    for letter in alphabet:
        if alphabet[letter] > 0:
            return False
    return True

if __name__ == "__main__":
    args = sys.argv
    with_extra_chars = False
    while True:
        if len(args) > 1:
            text = args[1]
            if len(args) > 2:
                if args[2].lower() == "false" or args[2].lower() == "f" or args[2].lower() == "0":
                    with_extra_chars = False
                elif args[2].lower() == "true" or args[2].lower() == "t" or args[2].lower() == "1":
                    with_extra_chars = True
        else:
            print("Enter command or text to be converted:")
            text = input("> ")
        #Check for commands
        if text.lower() == "quit" or text.lower() == "exit":
            quit()
        elif text.lower() == "exchar":
            with_extra_chars = not(with_extra_chars)
            if with_extra_chars:
                print("Extra chars will now be replaced with [CHARACTER]. E.g. ? will be replaced with [QUESTION]. Maybe i will come up with new morse codes for these.")
            else:
                print("Characters not part of morse will be ignored")
        elif text.lower() == "clear":
            os.system("cls")
        elif text.lower() == "help":
            print("Quit: Closes program")
            print("Exchar: Enables extra characters")
            print("Clear: Clears the screen")
        else:
            #Check whether the entered text is morse code or normal text
            isMorse = is_it_morse(text)
            if not(isMorse):
                print(eng_to_morse(text, with_extra_chars))
            elif isMorse:
                print(morse_to_eng(text))
            else:
                #If mode check fails, allow the user to decide
                while True:
                    mode = input("Unable to determine mode, enter manually: ")
                    if mode.lower() == "encode":
                        print(eng_to_morse(text, with_extra_chars))
                        break
                    elif mode.lower() == "decode":
                        print(morse_to_eng(text))
                        break
        if len(args) > 1:
            quit()
