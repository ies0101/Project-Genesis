# Project Genesis
#AI NAME: Kang
#Creator: IES
#Version: 0.5



from kang.brain.memory_interpreter import interpret_memory
from kang.core.identity import NAME, VERSION, CREATOR, BIRTH_DATE
from kang.memory.memory_manager import (
    get_creator_name, 
    save_creator_name, 
    add_creator_memory,
    get_creator_memories
)
from kang.brain.correction_manager import add_correction, find_similar_corrections
from kang.brain.word_correction_manager import apply_word_corrections, add_word_correction




print("Merhaba")
print("Ben", NAME)
print("Şu anki sürümüm:", VERSION)
print("Yaratıcım:", CREATOR)
print("Doğum tarihim:", BIRTH_DATE)

creator_name = get_creator_name()

if creator_name:
    print("\nTekrar hoşgeldin", creator_name+"!")

else:
    print("\nAdın nedir?")
    creator_name = input().strip()

    save_creator_name(creator_name)

    print("\nTanıştığıma memnun oldum", creator_name + "!")
    print("Adını hafızama kaydettim.")
    
add_creator_memory("Eren bana kang adını verdi.")

get_creator_memories = get_creator_memories()
print("\nSeninle ilgili hatırladıklarım:")

for memory in get_creator_memories:
    print("-", memory)


print("\nBana kendin hakkında bir şey öğret:")
new_memory = input().strip()

if new_memory:
    previous_correction = find_similar_corrections(new_memory)

    if previous_correction:
        interpreted_memory = previous_correction["corrected"]

        print("\nBu cümleyi daha önce yanlış anlamıştım.")
        print("Geçmişte bana öğrettiğin düzeltmeyi kullandım.")
        
    else:
        interpreted_memory = interpret_memory(new_memory, creator_name)
    
    print("\nŞöyle anladım:")
    interpreted_memory = apply_word_corrections(interpreted_memory)
    print(interpreted_memory)

    print("\nDoğru anladım mı?")
    answer = input().strip().lower()

    if answer == "evet":
        add_creator_memory(interpreted_memory)
        print("\nBunu hatırlayacağım.")

    else:
        print("\nYanlış anladım.")
        print("Düzeltme türü nedir?")
        print("1- Kelime veya yazım hatası")
        print("2- Cümlenin anlamı yanlış")

        correction_type = input().strip()

        if correction_type == "1":
            print("\nYanlış yazdığım kelime nedir?")
            wrong_word = input().strip()

            print("Doğrusu nedir?")
            correct_word = input().strip()

            if wrong_word and correct_word:
                add_word_correction(wrong_word, correct_word)
                print("\nKelime düzeltmesini öğrendim.")

        elif correction_type == "2":
            print("\nCümlenin doğrusunu öğret:")
            corrected_memory = input().strip()

            if corrected_memory:
                add_correction(
                    new_memory,
                    interpret_memory,
                    corrected_memory
                )

                add_creator_memory(corrected_memory)

                print("\nAnlam hatamı ve düzeltmeni kaydettim.")
        
        else:
            print("\nGeçersiz seçim yaptın.")