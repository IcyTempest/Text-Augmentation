from models import MyWords, Intent
from file import fileio


def sentences(filename, word1, word2, word3, word4):
    tmp = "\n word1:" + str(word1) + "\n " + "word2:" + str(word2) + "\n " + "word3:" + str(
        word3) + "\n " + "word4:" + str(word4) + "\n " + "_______________________________________________"
    fileio(filename, tmp)
    for i in range(len(word1)):
        for j in range(len(word2)):
            for k in range(len(word3)):
                for m in range(len(word4)):
                    x = "តើ/O " + word1[i - 1] + word2[j - 1] + word3[k - 1] + word4[m - 1]
                    print(x)
                    fileio(filename, x)


def intent():
    filename = 'rose'
    # If dak word normally, remove intent
    words1: MyWords = MyWords(intentR=Intent.I,
                              words=[" Manuth ", "ម៉ាន៉ុត", " Rithiya ", "រិទ្ធិយ៉ា", " Chhunheang ", "ឈុនហ៊ាង",
                                     " Kimhong ", "គីមហុង", " Nary ",
                                     "ណារី", " Nao ", "ណោ"])

    # Add space at the end of the sentence too, im too lazy to account for this XD
    words2: MyWords = MyWords(intentR=Intent.O,
                              words=["មាន ដឹង សាលា មាន ", "ដឹង ថា សាលា មាន "])

    words3: MyWords = MyWords(intentR=Intent.I,
                              words=[' Facebook page ', "ហ្វេសបុកភេច", " social media page ", "សូសលមីឌិរភេច", " page ",
                                     "ភេច",
                                     " instagram page ", "អុីនស្តាក្រាម ភេច", " Twitter ", "ថ្វីតធឺរ", " TikTok ",
                                     "តិកតុក"])

    words4: MyWords = MyWords(intentR=Intent.O,
                              words=["អត់?", "ទេ?"])

    sentences(filename, word1=words1.words, word2=words2.words, word3=words3.words, word4=words4.words)


if __name__ == '__main__':
    intent()
