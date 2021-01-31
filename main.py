# Author Info;
# Github | rlyonheart
# Twitter | rly0nheart
# Instagram | rlyonheart


# importing required modules #
import sys
from termcolor import cprint

cprint('''
 
      #   #   ##  ###   ##  ###    ##  ##  ##  ###
     # # # # #  # #  # #    #     #   #  # # # #  #
     #  #  # #  # ###   ##  ###   #   #  # # # ###
     #     # #  # #  #    # #     #   #  # # # #  #
     #     #  ##  #  #  ##  ###    ##  ##  ##  #  # v1.0\n''','yellow',attrs=['bold'])

inp = input('\t> Morse DeCodr\n   \t> Morse EnCodr\n\t \n\t $')

# function to decode morse code #
def morse_decode():
	
	ui = input('\n\t Enter morse code: ')
	# morse code alphabet #
	dit_dah = '\t A'
	dah_dit_dit_dit = '\t B'
	dit_dit_dah_dit = '\t C'
	dah_dit_dit = '\t D'
	dit = '\t E'
	dah_dit_dah_dit = '\t F'
	dah_dah_dit = '\t G'
	dit_dit_dit_dit = '\t H'
	dit_dit = '\t I'
	dit_dah_dah_dah = '\t J'
	dah_dit_dah = '\t K'
	dit_dah_dit_dit = '\t L'
	dah_dah = '\t M'
	dah_dit = '\t N'
	dah_dah_dah = '\t O'
	dit_dah_dah_dit = '\t P'
	dah_dah_dit_dah = '\t Q'
	dit_dah_dit = '\t R'
	dit_dit_dit = '\t S'
	dah = '\t T'
	dit_dit_dah = '\t U'
	dit_dit_dit_dah = '\t V'
	dit_dah_dah = '\t W'
	dah_dit_dit_dah = '\t X'
	dah_dit_dah_dah = '\t Y'
	dah_dah_dit_dit = '\t Z'
	
	# morse code numbers #
	dah_dah_dah_dah_dah = '\t 0'
	dit_dah_dah_dah_dah = '\t 1'
	dit_dit_dah_dah_dah = '\t 2'
	dit_dit_dit_dah_dah = '\t 3'
	dit_dit_dit_dit_dah = '\t 4'
	dit_dit_dit_dit_dit = '\t 5'
	dah_dit_dit_dit_dit = '\t 6'
	dah_dah_dit_dit_dit = '\t 7'
	dah_dah_dah_dit_dit = '\t 8'
	dah_dah_dah_dah_dit = '\t 9'
	
	if ui == '.-':
		print(dit_dah)
	elif ui == '-...':
		print(dah_dit_dit_dit)
	elif ui == '..-.':
		print(dit_dit_dah_dit)
	elif ui == '-..':
		print(dah_dit_dit) 
	elif ui == '.':
	    print(dit)
	elif ui == '-.-.':
	    print(dah_dit_dah_dit)
	elif ui == '--.':
	    print(dah_dah_dit)
	elif ui == '....':
		print(dit_dit_dit_dit)
	elif ui == '..':
	    print(dit_dit)
	elif ui == '.---':
	    print(dit_dah_dah_dah)
	elif ui == '-.-':
	    print(dah_dit_dah)
	elif ui == '.-..':
	    print(dit_dah_dit_dit)
	elif ui == '--':
	    print(dah_dah)
	elif ui == '-.':
	    print(dah_dit)
	elif ui == '---':
	    print(dah_dah_dah)
	elif ui == '.--.':
	    print(dit_dah_dah_dit)
	elif ui == '--.-':
	    print(dah_dah_dit_dah)
	elif ui == '.-.':
	    print(dit_dah_dit)
	elif ui == '...':
	    print(dit_dit_dit)
	elif ui == '-':
		print(dah)
	elif ui == '..-':
	  print(dit_dit_dah)
	elif ui == '...-':
	  print(dit_dit_dit_dah)
	elif ui == '.--':
	  print(dit_dah_dah)
	elif ui == '-..-':
	  print(dah_dit_dit_dah)
	elif ui == '-.--':
	  print(dah_dit_dah_dah)
	elif ui == '--..':
	  print(dah_dah_dit_dit)
	  
	  # numbers
	elif ui == '-----':
	  print(dah_dah_dah_dah_dah)
	elif ui == '.----':
	  print(dit_dah_dah_dah_dah)
	elif ui == '..---':
	  print(dit_dit_dah_dah_dah)
	elif ui == '...--':
	  print(dit_dit_dit_dah_dah)
	elif ui == '....-':
	  print(dit_dit_dit_dit_dah)
	elif ui == '.....':
	  print(dit_dit_dit_dit_dit)
	elif ui == '-....':
	  print(dah_dit_dit_dit_dit)
	elif ui == '--...':
	  print(dah_dah_dit_dit_dit)
	elif ui == '---..':
	  print(dah_dah_dah_dit_dit)
	elif ui == '----.':
	  print(dah_dah_dah_dah_dit)
	elif 'exit' in ui.lower():
		sys.exit('\t [E79] Program terminated by user.')
	else:
		print('\t [E101]Invalid Input')
		
def morse_encode():
  ui = input('\n\t Enter Text/Number: ')
  
  # morse code #
  A = '\t .-'
  B = '\t -...'
  C = '\t ..-.'
  D = '\t ...'
  E = '\t .'
  F = '\t -.-.'
  G = '\t --.'
  H = '\t ....'
  I = '\t ..'
  J = '\t .---'
  K = '\t ..-'
  L = '\t .-..'
  M = '\t --'
  N = '\t -.'
  O = '\t ---'
  P = '\t .--.'
  Q = '\t --.-'
  R = '\t .-.'
  S = '\t ...'
  T = '\t -'
  U = '\t ..-'
  V = '\t ...-'
  W = '\t .--'
  X = '\t -..-'
  Y = '\t -.--'
  Z = '\t --..'
  
  if ui.lower() == 'a':
    print(A)
  elif ui.lower() == 'b':
    print(B)
  elif ui.lower() == 'c':
    print(C)
  elif ui.lower() == 'd':
    print(D)
  elif ui.lower() == 'e':
    print(E)
  elif ui.lower() == 'f':
    print(F)
  elif ui.lower() == 'g':
    print(G)
  elif ui.lower() == 'h':
    print(H)
  elif ui.lower() == 'i':
    print(I)
  elif ui.lower() == 'j':
    print(J)
  elif ui.lower() == 'k':
    print(K)
  elif ui.lower() == 'l':
    print(L)
  elif ui.lower() == 'm':
    print(M)
  elif ui.lower() == 'n':
    print(N)
  elif ui.lower() == 'o' :
    print(O)
  elif ui.lower() == 'p':
    print(P)
  elif ui.lower() == 'q':
    print(Q)
  elif ui.lower() == 'r':
    print(R)
  elif ui.lower() == 's':
    print(S)
  elif ui.lower()=='t':
    print(T)
  elif ui.lower() == 'u':
    print(U)
  elif ui.lower() == 'v':
    print(V)
  elif ui.lower() == 'w':
    print(W)
  elif ui.lower() == 'x':
    print(X)
  elif ui.lower() == 'y':
    print(Y)
  elif ui.lower() == 'z' :
    print(Z)
    
  # number inputs #
  elif ui == '0':
    print('\t -----')
  elif ui == '1':
    print('\t .----')
  elif ui == '2':
    print('\t ..---')
  elif ui == '3':
    print('\t ...--')
  elif ui == '4':
    print('\t ....-')
  elif ui == '5':
    print('\t .....')
  elif ui == '6':
    print('\t -....')
  elif ui == '7':
    print('\t --...')
  elif ui == '8':
    print('\t ---..')
  elif ui == '9':
    print('\t ----.')
  elif 'exit' in ui.lower():
    sys.exit('\t Program terminated by user.')
  else:
    print('\t [E101] Invalid Input')
    sys.exit('\t [E79] Program terminated.')
  
if __name__ == '__main__':
  while True: # main loop
    if 'decode' in inp:
    	morse_decode()
    elif 'encode' in inp:
    	morse_encode()
    elif 'exit' in inp.lower():
    	sys.exit('\t [E79] Program terminated by user.')
    else:
    	print('\n\t [E101] Invalid Input')
    	sys.exit('\t [E0] Program terminated.')
  
               # END ©2020 #
