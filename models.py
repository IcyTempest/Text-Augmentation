import re

from enum import Enum, unique
from typing import List

@unique
class Intent(Enum):
    O = "/O"
    I = "/I-PER"


def convert(words: List[str], intent: Intent = None, segment:bool = True):
    match intent:
        case Intent.I:
            if segment:
                # Long version
                # rose = []
                # rise = []
                # for i in words:
                #     rose = i.strip()
                #     rose += " "
                #     rise.append(rose)
                #     print("|" + rose + "|")
                #     for j in rise:
                #         ree = j.replace(" ", "/B-PER ")
                #         roo = re.sub(r"/B-PER $", "/I-PER ", ree)
                #         list.append(roo)


                # Short Version
                ree = [x.strip()+" " for x in words]
                row = [re.sub(r"/B-PER $", "/I-PER ", x.replace(" ", "/B-PER ")) for x in ree]
                return row
            return words

        case Intent.O:

            if segment:
                return [x.replace(" ", intent.value + " ").replace("?", "?" + intent.value) for x in words]
            return [x.replace(" ", "") for x in words]

        case _:
            return words


class MyWords:
    def __init__(self, intentR: Intent, words: List[str]):
        newWords = convert(intent=intentR, words=words)
        print(newWords)
        self.words = newWords

    intent: Intent
    words: List[str]