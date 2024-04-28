import spacy
from spacy import displacy
from typing import List

NER = spacy.load("en_core_web_lg")

def person_detector(text: str) -> List[str]:
    result = NER(text)
    names = []
    name = ""   
    for word in result:
        if word.pos_ == "PROPN":
            name += str(word) + " "
        else:
            if name != "" and name is not None:
                name = name.strip()
                names.append(name)
                name = ""
        print(word, word.pos_)
    return names


if __name__ == "__main__":

    result = person_detector("""MISS.ZIYAN ZHOU 
MR.YUAN TAO (ผ.30)""")
    print(result)
    for word in result:
        print(word)
