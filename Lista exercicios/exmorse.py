alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..',
         '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']

def morse_decrypter(morse_code):
    palavras_morse = morse_code.split(' / ')
    mensagem_decodificada = []

    for palavra in palavras_morse:
        letras_morse = palavra.split(' ')
        palavra_decodificada = ''

        for letra in letras_morse:
            if letra in morse:
                indice = morse.index(letra)
                palavra_decodificada += alfabeto[indice]
            else:
                palavra_decodificada += '?'
        
        mensagem_decodificada.append(palavra_decodificada)
    return ' '.join(mensagem_decodificada)

def main():
    morse_code = input("digite o código Morse para descriptografar: ")
    decoded_message = morse_decrypter(morse_code)
    print(f"Mensagem decodificada: {decoded_message}")

main()
