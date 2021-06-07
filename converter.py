translation_map = {
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


def to_morse(text: str) -> str:
    text = text.lower()
    output = ""
    for char in text:
        output = f"{output} {translation_map.get(char, char)}"
    return output


def to_plaintext(morse: str) -> str:
    output = ""
    for morse in morse.split(" "):
        for char in translation_map:
            if translation_map.get(char) == morse:
                output = f"{output}{char}"
                break
    return output
