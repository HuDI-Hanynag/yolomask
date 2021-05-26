class PCInformation(object):
    def mask(self):
        f = open('yolomask.txt', 'r')
        text = f.read()
        a = text[-1]
        maskpeople=int(a)
        f.close
        return maskpeople









