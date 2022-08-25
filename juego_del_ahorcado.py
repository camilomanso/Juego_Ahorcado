import os
import random 
   

def read_data(filepath ="./archivos/data.txt"):
    words = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip().upper())
    return words


def main():
    data = read_data(filepath="./archivos/data.txt")
    chosen_word = random.choice(data)
    chosen_word_list = [letter for letter in chosen_word]
    chosen_word_list_underscores = ["_"] * len(chosen_word_list)
    letter_index_dict = {}
    for index, letter in enumerate(chosen_word):
        if not letter_index_dict.get(letter):
            letter_index_dict[letter] = []
        letter_index_dict[letter].append(index)

    letter_wrong = ""
    
    while True:
        os.system("cls")
        print("¡Adivina la palabra!")
        for element in chosen_word_list_underscores:
            print(element + " ", end="")
        print("\n")

        letter = input("Ingresa una letra: ").strip().upper()
        
        assert letter.isalpha(), "Solo puedes ingresar letras"
        if letter in chosen_word_list:
            for index in letter_index_dict[letter]:
                chosen_word_list_underscores[index] = letter
        else:
            letter_wrong += letter
            if len(letter_wrong) == 6:
                os.system("cls")
                print("Ha alcanzado el número máximo de intentos")
                break
        if "_" not in chosen_word_list_underscores:
            os.system("cls")
            print("¡Ganaste! La palabra era", chosen_word)
            break
        
        
    

if __name__ == '__main__':
    main()
    