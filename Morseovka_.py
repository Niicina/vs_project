	
#uzivatel nejprve vlozi text, ktery chce prelozit do Morseovy abecedy

message = message.upper()
#slovnik Morseovy abecedy je ve formatu uppercase. V pripade zadani vety v lowercase, prepise vetu na uppercase.

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}		

#slovnik na preklad Morseovy abecedy

def encrypt(message):
    	sifra = ''
    for pismeno in message:
        if pismeno != ' ': 				

#Vyhledá slovník a přidá odpovídající Morseovu abecedu spolu s mezerou pro různé znaky
            

	sifra += MORSE_CODE_DICT[pismeno] + ' '
        	else:
# označuje různé znaky
# a označuje různá slova
            

	sifra += ' '
    return sifra 			

#vrací šifru

print(encrypt(message))			
#vypíše šifru v morseově abecedě

input()
#na ukončení programu musí uživatel stisknout Enter
