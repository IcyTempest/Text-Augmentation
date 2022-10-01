from pathlib import Path


def fileio(filename, msg):
    Path("generate/"+filename + ".txt").touch()
    with open("generate/"+filename + ".txt", 'a+', encoding="utf-8") as f:
        f.write(msg + "\n")
        f.close()