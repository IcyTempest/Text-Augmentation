from models import MyWords, Intent, convert
from file import fileio


def sentences(filename, word1, word2, word3, word4, segment: bool = False):
    tmp = "\n word1:" + str(word1) + "\n " + "word2:" + str(word2) + "\n " + "word3:" + str(
        word3) + "\n " + "word4:" + str(word4) + "\n " + "_______________________________________________"
    fileio(filename, tmp)
    for i in range(len(word1)):
        for j in range(len(word2)):
            for k in range(len(word3)):
                for m in range(len(word4)):
                    if segment:
                        x = "តើ/O " + word1[i - 1] + word2[j - 1] + word3[k - 1] + word4[m - 1]
                        print(x)
                        fileio(filename, x)
                    else:
                        x = "តើ" + word1[i - 1] + word2[j - 1] + word3[k - 1] + word4[m - 1]
                        print(x)
                        fileio(filename, x)


def intent():
    filename = 'newPage'
    # If dak word normally, modify segment to false
    # If wants to segment word, add space to each word,
    # for Intent.I, adding space for entity is optional
    segment: bool = False

    words1 = convert(
        intent=Intent.I,
        segment=segment,
        words=[" Manuth ", "ម៉ាន៉ុត", " Rithiya ", "រិទ្ធិយ៉ា", " Chhunheang ", "ឈុនហ៊ាង",
               " Kimhong ", "គីមហុង", " Nary ",
               "ណារី", " Nao ", "ណោ"])

    words2 = convert(
        intent=Intent.O,
        segment=segment,
        words=["មាន ដឹង សាលា មាន ", "ដឹង ថា សាលា មាន "])

    words3 = convert(
        intent=Intent.I,
        segment=segment,
        words=[' Facebook page ', "ហ្វេសបុកភេច", " social media page ", "សូសលមីឌិរភេច", " page ",
               "ភេច",
               " instagram page ", "អុីនស្តាក្រាម ភេច", " Twitter ", "ថ្វីតធឺរ", " TikTok ",
               "តិកតុក"])

    words4 = convert(
        intent=Intent.O,
        segment=segment,
        words=["អត់?", "ទេ?"])

    sentences(filename, word1=words1, word2=words2, word3=words3, word4=words4, segment=segment)


if __name__ == '__main__':
    intent()
