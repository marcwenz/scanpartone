from configparser import ConfigParser
import json


def loadConfig(conf):
    with open("config/" + conf + ".json") as f:
        return json.load(f)


def saveConfig(saveas, conf):
    with open("config/" + saveas + ".json", "w") as f:
        json.dump(conf, f)
