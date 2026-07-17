import json
from pathlib import Path

correction_file = Path("kang/brain/corrections.json")

def load_corrections():
    data = correction_file.read_text(encoding="utf=8")

    corrections = json.loads(data)

    return corrections

def add_correction(heard, interpreted, corrected):
    corrections = load_corrections()

    correction= {
        "heard" : heard,
        "interpreted" : interpreted,
        "corrected" : corrected
    }

    corrections.append(correction)

    correction_file.write_text(
        json.dumps(corrections, ensure_ascii=False, indent=4),
        encoding="utf=8"
    )

def find_similar_corrections(heard):
    corrections = load_corrections()

    for correction in corrections:
        if correction["heard"] == heard:
            return correction
    
    return None