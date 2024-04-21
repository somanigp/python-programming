alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  
def ceaser(text, shift, direction):
  result = ""
  alphabet_lenght = 26
  if direction == "decode": 
    shift *= -1 # if we put it inside the for loop , it will keep toggling as both shift and alphabet are outside of for loop
  else:
    alphabet_lenght *= -1
  for letter in text:
    if letter in alphabet:
      index = alphabet.index(letter)
      if ((index + shift > 25) and direction == "encode") or ((index - shift < 0) and direction == "decode") :
        index = index + shift + alphabet_lenght
      else:
        index = index + shift
      result += alphabet[index]
    else:
      result += letter
  print(result)

do_continue = True  
while do_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  if (direction.lower() == "encode") or (direction.lower() == "decode"):
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(text,shift%26,direction.lower()) # important as if shift it too large it will make it equivalent to what it was if shift was < 26. Note : 26 is len of alphabet so after 26 shift alphabet repeat
  else:
    print("Give proper response.")
  que = input("Do you wanna continue? Y or N\n").lower()
  if que == "n":
    do_continue = False

# def encrypt(text, shift): # arguments and parameter words can be same
#   result = []
#   text_list = list(text)
#   for i in range(len(text_list)):
#     if text_list[i] in alphabet:
#       index = alphabet.index(text_list[i])
#       # last index can only be 25 as total 26 letters in alphabet
#       if index + shift > 25:
#         index = index + shift - 26 # we need to remove 26 letters as 26(full set of alphabets) - no of letters from the.
#         # -26 as to get to 0 and not 1 as index of 'a' is 0. 26 is total no. of letters and we need to remove that 
#       else:
#         index = index + shift
#       result.append(alphabet[index])
#     else:
#       result.append(text_list[i])
#   print(''.join(result)) 

# def decrypt(text, shift):  # using strings and not lists    
#   result = ""
#   for letter in text:
#     if letter in alphabet:
#       index = alphabet.index(letter)
#       if index - shift < 0:
#         index = index - shift + 26
#       else:
#         index -= shift 
#       result += alphabet[index]
#     else:
#       result += letter 
#   print(result)

# do_continue = True  
# while do_continue:
#   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#   if direction.lower() == "encode":
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#     encrypt(text,shift)
#   elif direction.lower() == "decode":
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#     decrypt(text,shift)
#   else:
#     print("Give proper response.")
#   que = input("Do you wanna continue? Y or N\n").lower()
#   if que == "n":
#     do_continue = False