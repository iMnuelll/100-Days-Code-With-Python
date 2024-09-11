alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount) :
    cipher_text = ""
    for i in (plain_text) :
        find_indexNumber = alphabet.index(i)
        find_indexNumber += shift_amount
        if find_indexNumber >= len(alphabet) :
            find_indexNumber -= len(alphabet)
            cipher_text += alphabet[find_indexNumber]
        else :
            cipher_text += alphabet[find_indexNumber]
    print(f"The encoded text is {cipher_text}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text, shift_amount) :
  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
    normal_text = ""
    for i in (cipher_text) :
        find_indexNumber = alphabet.index(i)
        find_indexNumber -= shift_amount
        if find_indexNumber < 0 :
            find_indexNumber += len(alphabet)
            normal_text += alphabet[find_indexNumber]
        else :
             normal_text += alphabet[find_indexNumber]
    print(f"The decoded text is {normal_text}")

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encode" :
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode" :
    decrypt(cipher_text=text, shift_amount=shift)