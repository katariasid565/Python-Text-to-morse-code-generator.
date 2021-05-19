from morse import MORSE_CODE_DICT
# -*- coding: utf-8 -*-
"""...........text to morse code generator program............."""
def encryption(message):
   my_cipher = ''
   for myletter in message:
      if myletter != ' ':
         my_cipher += MORSE_CODE_DICT[myletter] + ' '
      else:
         my_cipher += ' '
      return my_cipher

# This function is used to decrypt
# Morse code to English
def decryption(message):
   message += ' '
   decipher = ''
   mycitext = ''
   for myletter in message:
      # checks for space
      if (myletter != ' '):
         i = 0
         mycitext += myletter
      else:
         i += 1
         if i == 2 :
            decipher += ' '
         else:
            decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
            .values()).index(mycitext)]
            mycitext = ''
   return decipher

def main():
   my_message = "HELLO -SIDDHANT -SINGH"
   output = encryption(my_message.upper())
   print (output)
   my_message = ".--. -.-- - .... --- -.  -....- .--. .-. --- --. .-. .- -- "
   output = decryption(my_message)
   print (output)
# Executes the main function
if __name__ == '__main__':
   main()