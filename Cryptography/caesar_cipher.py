# Caesar's cipher shifts each letter by a number of letters. If shift takes you past end of alphabet, just rotate back to front
# Special chars/ symbols stay unencrypted
# Original case should persist in translation
# Shifted Alphabet: +3 defghijklmnopqrstuvwxyzabc

# Hint: Use built-in ord() and chr() functionns
# ord() gives you number representation of a letter (remember uppercase and lowercase letters are represented differently)
# chr()

# Encyption Rule: c = (x + n) % 26


def caesars_cipher(s, k):
    translation = ''
    for i in range(len(s)):
        letter = s[i]
        # deal w/ uppercase letters
        if letter.isupper():
            translation += chr((ord(letter) + k-65) % 26 + 65)
        # deal w /lowercase letters
        else:
            translation += chr((ord(letter) + k - 97) % 26 + 97)

    return translation


print(caesars_cipher("ABC", 3))  # DEF
print(caesars_cipher("hello kitty", 5))  # DEF
