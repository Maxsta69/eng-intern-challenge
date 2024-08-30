import sys

# Braille to English dictionary
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OOO...": "d", "O..O..": "e",
    "OOOO..": "f", "OOOOO.": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OOO.O.": "n", "O..OO.": "o",
    "OOOOO.": "p", "OOOOOO": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OOO.OO": "y", "O..OOO": "z",
    ".....O": "cap", ".O.OO.": "num", "......": " "
}

# English to Braille dictionary
english_to_braille = {v: k for k, v in braille_to_english.items()}
english_to_braille.update({
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OOO...", "5": "O..O..",
    "6": "OOOO..", "7": "OOOOO.", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
})

# Translate Braille to English

def braille_to_text(braille):
    text = ""
    is_capital = False
    is_number = False

    for i in range(0, len(braille), 6):
        symbol = braille[i:i + 6]
        
        # If the symbol is a capital
        if symbol == "....0":
            is_capital = True
            continue
        # If the symbol is a number
        elif symbol == ".0.00.":
            is_number = True
            continue

        char = braille_to_english.get(symbol, "?")
        if is_capital:
            char = char.upper()
            is_capital = False

        if is_number:
            text += char
        else:
            text += char
            # If the symbol is a space
            if symbol == "......":
                is_number = False

    return text

# Translate English to Braille
def text_to_braille(text):
    braille = ""
    for char in text:
        if char.isupper():
            braille += "....0"
            char = char.lower()
        if char.isdigit():
            braille += ".0.00."
            braille += english_to_braille[char]
        else:
            braille += english_to_braille.get(char, "......")
        braille += " "

    return braille.strip()

# Main function to handle input
def main():
    if len(sys.argv) < 2:
        print("Usage: python braille_translator.py <string>")
        return
    
    input_string = sys.argv[1]

    if "0" in input_string or "." in input_string:
        # Input is Braille
        print(braille_to_text(input_string))
    else:
        # Input is English
        print(text_to_braille(input_string))

if __name__ == '__main__':
    main() 
