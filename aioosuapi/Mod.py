class Mod:
    def __init__(self, bits):
        if not bits:
            bits = 0
        number = int(bits)
        # Thanks Ayato_k
        mod_list = ["NF", "EZ", "TD", "HD", "HR",
                    "SD", "DT", "RX", "HT", "NC",
                    "FL", "AutoPlay", "SO", "AP", "PF",
                    "4K", "5K", "6K", "7K", "8K",
                    "FI", "RanD", "Cinema", "TP", "9K",
                    "10K", "1K", "3K", "2K", "V2", "LM"]
        if number <= 0:
            mod_str = "None"
        else:
            bin_list = [int(x) for x in bin(number)[2:]]
            i = 0
            mod_str = ""
            for y in reversed(bin_list):
                if y == 1:
                    mod_str += mod_list[i]
                i += 1
        self.mod = mod_str

    def __str__(self):
        return self.mod
