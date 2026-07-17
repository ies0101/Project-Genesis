import json
from pathlib import Path

word_correction_file = Path("kang/brain/word_corrections.json")



def load_word_corrections():
    data = word_correction_file.read_text(encoding="utf=8")
    return json.loads(data)


def add_word_correction(wrong, correct):
    corrections = load_word_corrections()

    correction = {
        "wrong" : wrong,
        "correct" : correct
    }

    corrections.append(correction)

    word_correction_file.write_text(
        json.dumps(corrections, ensure_ascii=False, indent=4),
        encoding="utf=8"
    )

def find_word_correction(word):
    corrections = load_word_corrections()

    for correction in corrections:
        if correction["wrong"] == word:
            return correction["correct"]
        
    return None

def apply_word_corrections(text):
    words = text.split()

    new_words = []

    for word in words:
        corrected = find_word_correction(word)

        if corrected:
            new_words.append(corrected)
            
        else:
            new_words.append(word)
    
    return " ".join(new_words)