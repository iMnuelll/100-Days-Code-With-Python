alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(text, shift_amount, direction) :
    final_text = ""
    for i in (text) :
        find_indexNumber = alphabet.index(i)
        if direction == "decode" :
            find_indexNumber -= shift_amount
            if find_indexNumber < 0 :
                find_indexNumber += len(alphabet)
                final_text += alphabet[find_indexNumber]
            else :
                 final_text += alphabet[find_indexNumber]
        else :
            find_indexNumber += shift_amount
            if find_indexNumber >= len(alphabet) :
                find_indexNumber -= len(alphabet)
                final_text += alphabet[find_indexNumber]
            else :
                 final_text += alphabet[find_indexNumber]
    print(f"The {direction} text is {final_text}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text = text, shift_amount = shift, direction = direction)