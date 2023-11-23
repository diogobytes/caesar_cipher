import logo

alphabet = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
   'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
  ]

def caesar(text,shift,direction):
  if direction == 'decode':
    shift *= -1
  message_output = ''
  for char in text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift
      message_output += alphabet[new_position]
    else:
      message_output += char
  print(f"The decoded  message is: {message_output}")

print(logo.logo)

user_response = True

while user_response:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  caesar(text=text,shift=shift,direction=direction)
  response = input("Type yes if you want to go again and no to end:\n")
  if(response == 'no'):
    user_response = False
  