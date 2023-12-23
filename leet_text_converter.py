# LEET Alphabet
leet_alphabet = {
    'A': '4', 'B': '8', 'C': 'C', 'D': 'D', 'E': '3', 'F': 'F', 'G': '9', 'H': 'H',
    'I': '1', 'J': 'J', 'K': 'K', 'L': 'L', 'M': '44', 'N': 'N', 'O': '0', 'P': 'P',
    'Q': 'Q', 'R': 'R', 'S': '5', 'T': '7', 'U': 'U', 'V': 'V', 'W': 'VV', 'X': 'X',
    'Y': 'Y', 'Z': 'Z',
    
    '0': 'O', '1': 'I', '2': 'Z', '3': 'E', '4': 'A', '5': 'S', '6': 'G',
    '7': 'T', '8': 'B', '9': 'J'
}

# convert the normal text into LEET text
def convert_to_leets(message):
    leet_text = ""
    for char in message.upper():
        if char in leet_alphabet:
            leet_text += leet_alphabet[char]
        elif char == " ":
            leet_text += " "
    return leet_text.rstrip()

if __name__ == '__main__':
    message = input("Input your letters to convert into L337 text: ")
    leet_text = convert_to_leets(message)
    print(f"Your original message: {message}")
    print(f"This is your LEET text: {leet_text}")
