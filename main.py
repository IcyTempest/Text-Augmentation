from typing import List

from models import Intent, convert
from file import fileio


def sentences(filename, word1, word2, word3, word4, word5, segment: bool = False):
    tmp = "\n word1:" + str(word1) + "\n " + "word2:" + str(word2) + "\n " + "word3:" + str(
        word3) + "\n " + "word4:" + str(word4) + "\n " + "word5:" + str(
        word5) + "\n " + "_______________________________________________"
    fileio(filename, tmp)

    for i in range(len(word1)):
        for j in range(len(word2)):
            for k in range(len(word3)):
                for m in range(len(word4)):
                    for r in range(len(word5)):
                        if segment:
                            x = "តើ/O " + word1[i - 1] + word2[j - 1] + word3[k - 1] + word4[m - 1] + word5[r - 1]
                            print(x)
                            fileio(filename, x)
                        else:
                            x = "តើ" + word1[i - 1] + word2[j - 1] + word3[k - 1] + word4[m - 1] + word5[r - 1]
                            print(x)
                            fileio(filename, x)


# def SocialMediaExist():
#     filename = 'newPage'
#     # If dak word normally, modify segment to false
#     # If wants to segment word, add space to each word,
#     # for Intent.I, adding space for entity is optional
#     segment: bool = True
#
#     words1 = convert(
#         intent=Intent.Person,
#         segment=segment,
#         words=[" Manuth ", "ម៉ាន៉ុត", " Rithiya ", "រិទ្ធិយ៉ា", " Chhunheang ", "ឈុនហ៊ាង",
#                " Kimhong ", "គីមហុង", " Nary ",
#                "ណារី", " Nao ", "ណោ"])
#
#     words2 = convert(
#         intent=Intent.O,
#         segment=segment,
#         words=["មាន ដឹង សាលា មាន ", "ដឹង ថា សាលា មាន "])
#
#     words3 = convert(
#         intent=Intent.Organization,
#         segment=segment,
#         words=[' Facebook page ', "ហ្វេសបុកភេច", " social media page ", "សូសលមីឌិរភេច", " page ",
#                "ភេច",
#                " instagram page ", "អុីនស្តាក្រាម ភេច", " Twitter ", "ថ្វីតធឺរ", " TikTok ",
#                "តិកតុក"])
#
#     words4 = convert(
#         intent=Intent.O,
#         segment=segment,
#         words=["អត់?", "ទេ?"])
#
#     sentences(filename, word1=words1, word2=words2, word3=words3, word4=words4, segment=segment)
#
#
# def announceScholarship():
#     filename = 'announceScholarship'
#     # If dak word normally, modify segment to false
#     # If wants to segment word, add space to each word,
#     # for Intent.I, adding space for entity is optional
#     segment: bool = False
#
#     words1 = convert(
#         intent=Intent.I,
#         segment=segment,
#         words=[" Darot ", "ដារូ៉ត", " Jojo ", "ចូចូ", " Lita ", "លីតា",
#                " Duoung ", "ដួង", " Linda ",
#                "លីនដា", " Sokleap ", "សុខលាភ"])
#
#     words2 = convert(
#         intent=Intent.O,
#         segment=segment,
#         words=["ដឹង ថា សាលា បាន ប្រកាស ", "មាន ដឹង សាលា មាន ", ])
#
#     # words3 = convert(
#     #     intent=Intent.I,
#     #     segment=segment,
#     #     words=[' Facebook page ', "ហ្វេសបុកភេច", " social media page ", "សូសលមីឌិរភេច", " page ",
#     #            "ភេច",
#     #            " instagram page ", "អុីនស្តាក្រាម ភេច", " Twitter ", "ថ្វីតធឺរ", " TikTok ",
#     #            "តិកតុក"])
#     words3 = convert(
#         intent=Intent.I,
#         segment=segment,
#         words=["Scholarship Event", "អាហារូបករណ៍ event", "អាហារូបករណ៍ អុីវែន"])
#
#     words4 = convert(
#         intent=Intent.O,
#         segment=segment,
#         words=["នៅ?", "ទេ?"])
#
#     sentences(filename, word1=words1, word2=words2, word3=words3, word4=words4, segment=segment)

def findTotalStudent():
    filename = 'FindTotalStudentsV2'
    segment: bool = True

    words1 = convert(
        intent=Intent.Person,
        segment=segment,
        words=[" Darot ", "ដារូ៉ត", " Jojo ", "ចូចូ", " Lita ", "លីតា",
               " Duoung ", "ដួង", " Linda ",
               "លីនដា", " Sokleap ", "សុខលាភ"])

    words2 = convert(
        intent=Intent.O,
        segment=segment,
        words=["ដឹង ថា  ", "មាន ដឹង សាលា មាន និស្សិត ", "ដឹង ថា សាលា មាន សិស្ស ", "មាន ដឹង សាលា មាន និស្សិត សរុប",
               "មាន ដឹង សាលា មាន និស្សិត ", "មាន ដឹង ថា សាកលវិទ្យាល័យ មាន សិស្ស សរុប ",
               "មាន ដឹង ថា សាកលវិទ្យាល័យ មាន សិស្ស ",
               "មាន ដឹង ថា សាកលវិទ្យាល័យ មាន និស្សិត សរុប", "មាន ដឹង ថា សាកលវិទ្យាល័យ មាន និស្សិត "])

    words3 = convert(
        intent=Intent.Building,
        segment=segment,
        words=[" CADT ", "សុីអេឌុី", "សាលា CADT ", "សាកលវិទ្យាល័យ CADT ", "សាកលវិទ្យាល័យ សុីអេឌុី", "វិទ្យាល័យ CADT ",
               "វិទ្យាល័យ សុីអេឌុី"])

    words4 = convert(
        intent=Intent.O,
        segment=segment,
        words=["មាន សិស្ស សរុប "])

    words5 = convert(
        intent=Intent.O,
        segment=segment,
        words=["ប៉ុន្មាន?", "ប៉ុន្មាន អ្នក?", "ម៉ាន?", "ម៉ាន អត់?", "ម៉ាន ទេ?",
               "ម៉ាន អ្នក?"])

    sentences(filename, word1=words1, word2=words2, word3=words3, word4=words4, segment=segment, word5=words5)


if __name__ == '__main__':
    findTotalStudent()
