import time
from matplotlib import pyplot as plt


def bar(*args):
    for obj in args:
        if type(obj) != str:
            t = count(obj)
            plt.bar(t[1], t[0], label=t[1])
            plt.legend()
        if type(obj) == str:
            obj = load(str(obj))
            plt.bar(obj[1], obj[0], label=obj[1])
            plt.legend()
    plt.show()


def count(function):
    startTime = time.time()
    function()
    return time.time() - startTime, str(function.__name__)


def save(function, filename):
    counted = count(function)
    with open(filename, "w") as wrt:
        wrt.write(counted[1] + "\n")
        wrt.write(str(counted[0]))
        wrt.close()


def load(filename):
    with open(filename, "r") as rd:
        text = rd.readlines()
        rd.close()
        return float(text[1]), text[0].replace("\n", "")
