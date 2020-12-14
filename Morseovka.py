message=input('Vloz text na preklad:')			
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
#Vyhledá slovník a přidá
# odpovídající Morseova abeceda
# spolu s mezerou k oddělení
# morseovy kódy pro různé znaky
            sifra += MORSE_CODE_DICT[pismeno] + ' '
        else:
            # 1 označuje různé znaky
            # a 2 označuje různá slova
            sifra += ' '
    return sifra
#vrací šifru
