import re

from enum import Enum, unique
from typing import List


@unique
class Intent(Enum):
    O = "/O"
    Person = "PER"
    Room = "ROOM"
    Building = "BUILD"
    Floor = "FLOOR"
    Ordinal = "ORD"
    Cardinal = "CAR"
    Date = "DATE"
    Time = "TIME"
    Money = "MONEY"
    Event = "EVE"
    Announcement = "ANN"
    CountryCity = "GPE"
    Location = "LOC"
    Organization = "ORG"


def convert(words: List[str], intent: Intent = None, segment: bool = True):
    match intent:
        case Intent.O:

            if segment:
                return [x.replace(" ", intent.value + " ").replace("?", "?" + intent.value) for x in words]
            return [x.replace(" ", "") for x in words]

        case _:
            if segment:
                # # Long version
                # rose = []
                # rise = []
                # for i in words:
                #     rose = i.strip()
                #     rose += " "
                #     rise.append(rose)
                #     print("|" + rose + "|")
                #     for j in rise:
                #         ree = j.replace(" ", "/B-PER ")
                #         if ree.count(" ")>2:
                #             roo = re.sub(r"/B-PER $", "/I-PER ", ree)
                #             list.append(roo)

                # Short Version
                intent = intent.value
                ree = [x.strip() + " " for x in words]
                row = [re.sub(r"/B-{} $".format(intent), "/I-{} ".format(intent),
                              x.replace(" ", "/B-{} ".format(intent))) if x.count(" ") >= 2 else x.replace(" ",
                                                                                                          "/B-{} ".format(
                                                                                                              intent))
                       for x in ree]
                return row
            return words
