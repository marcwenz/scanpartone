import twain
from time import time


def getTypeDict():
    caps = {}
    with open("CAP_TO_TYPE.txt", "r") as f:
        for l in f.readlines():
            l = l.strip().split(",")
            if l[0] not in caps.keys() and len(l) > 0:
                caps[int(l[0])] = int(l[1])
    return caps


class ScanManager:

    def __init__(self, sc=None):
        self.sm = twain.SourceManager(0)
        if not sc:
            sc = self.sm.GetSourceList()[0]
        self.scanner = self.sm.OpenSource(bytes(sc, 'utf-8'))
        self.typelookup = getTypeDict()

    def get_available():
        return twain.SourceManager(0).GetSourceList()

    def acquire_images(self, ui=True, modal=True):
        self.ims = []
        self.scanner.acquire_file(
            lambda _: self.populateIms(), show_ui=ui, modal=modal)
        return self.ims

    def populateIms(self):
        p = "scans/{}.tif".format(str(time()).replace(".", ""))
        self.ims.append(p)
        return p

    def set_property(self, property, value):
        self.scanner.SetCapability(
            property, self.typelookup[property], value)

    def get_property(self, property):
        return self.scanner.GetCapabilityCurrent(property)

    def loadConfig(self, config):
        for prop, val in config.items():
            try:
                print(f"{prop=}")
                print("type: {}".format(type(prop)))
                print(f"{val=}")
                print("type: {}".format(type(val)))
                self.set_property(prop, val)
            except:
                print("error.")
                n = self.get_property(prop)
                print(n)
                config[prop] = n[-1]
        return config


if __name__ == "__main__":
    sm = ScanManager(ScanManager.get_available()[0])
    # sm.acquire_images(False, True)
    sm.set_property()
