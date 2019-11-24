class Accuracy:
    def __init__(self, c_miss, c50, c100, c300):
        # Thanks Ayato_k
        top = int(c50)*50 + int(c100)*100 + int(c300) * 300
        bottom = (int(c_miss)+int(c50)+int(c100)+int(c300))*300
        self.accuracy = str(round(float((top / bottom)*100), 2))

    def __str__(self):
        return self.accuracy
