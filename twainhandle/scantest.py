from pyzbar.pyzbar import decode
from pyzbar.wrapper import ZBarSymbol
from PIL import Image
from os import listdir
from time import time


def getFiles(path):
    return listdir(path)


def pil(im):
    return decode(im, [ZBarSymbol.QRCODE])


def tp(im, t):
    if t:
        return im.transpose(t)
    return im


if __name__ == "__main__":
    start = time()
    path = "C:\\Users\\marcw\Documents\\Panasonic\\"
    ff = getFiles(path)
    files = [Image.open(path + f) for f in ff]
    count = 0
    correct = []
    print("loading time: {:.2g}".format(time() - start))
    start = time()

    for f, s in zip(files, ff):
        c = False
        for rot in [None, Image.FLIP_TOP_BOTTOM, Image.ROTATE_90, Image.ROTATE_180, Image.ROTATE_270]:
            res = pil(tp(f, rot))
            if len(res) > 0:
                c = True
                correct.append(res)
                break
        if not c:
            print(s)
        count += 1

    print("decoding:{:.2g}s".format(time() - start))
    print("Total:", count)
    print("Correct:", len(correct) / count)
