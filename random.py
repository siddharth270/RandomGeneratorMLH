from time import time

def time_random():
    return time() - float(str(time()).split('.')[0])


def random_number_genrator(min, max):
    return float(time_random() * (max - min) + min)

print(random_number_genrator(0,99999))



