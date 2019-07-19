class Accuracy:
    def __init__(self, cmiss, c50, c100, c300):
        # Thanks Ayato_k
        self.accuracy = str(round(float(((int(c50)*50 + int(c100)*100 + int(c300) * 300) / ((int(cmiss)+int(c50)+int(c100)+int(c300))*300))*100), 2))

    def __str__(self):
        return self.accuracy
