def getTypeDict():
    caps = {}
    with open("CAP_TO_TYPE.txt", "r") as f:
        for l in f.readlines():
            l = l.strip().split()
            if l[0] not in caps.keys():
                caps[int(l[0])] = int(l[1])
    return caps
