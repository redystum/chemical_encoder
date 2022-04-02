from os import system

data = {
    "len1": {
        "h": 1,
        "b": 5,
        "c": 6,
        "n": 7,
        "o": 8,
        "f": 9,
        "p": 15,
        "s": 16,
        "k": 19,
        "v": 23,
        "y": 39,
        "i": 53,
        "u": 92
    },
    "len2": {
        "he": 2,
        "li": 3,
        "be": 4,
        "ne": 10,
        "na": 11,
        "mg": 12,
        "ai": 13,
        "si": 14,
        "ci": 17,
        "ar": 18,
        "ca": 20,
        "sc": 21,
        "ti": 22,
        "cr": 24,
        "mn": 25,
        "fe": 26,
        "co": 27,
        "ni": 28,
        "cu": 29,
        "zn": 30,
        "ga": 31,
        "ge": 32,
        "as": 33,
        "se": 34,
        "br": 35,
        "kr": 36,
        "rb": 37,
        "sr": 38,
        "zr": 40,
        "nb": 41,
        "mo": 42,
        "tc": 43,
        "ru": 44,
        "rh": 45,
        "pd": 46,
        "ag": 47,
        "cd": 48,
        "in": 49,
        "sn": 50,
        "sb": 51,
        "te": 52,
        "xe": 54,
        "cs": 55,
        "ba": 56,
        "la": 57,
        "ce": 58,
        "pr": 59,
        "nd": 60,
        "pm": 61,
        "sm": 62,
        "eu": 63,
        "gd": 64,
        "tb": 65,
        "dy": 66,
        "ho": 67,
        "er": 68,
        "tm": 69,
        "yb": 70,
        "lu": 71,
        "hf": 72,
        "ta": 73,
        "re": 75,
        "os": 76,
        "ir": 77,
        "pt": 78,
        "au": 79,
        "hg": 80,
        "tl": 81,
        "pb": 82,
        "bi": 83,
        "po": 84,
        "at": 85,
        "rn": 86,
        "fr": 87,
        "ra": 88,
        "ac": 89,
        "th": 90,
        "pa": 91,
        "np": 93,
        "pu": 94,
        "am": 95,
        "cm": 96,
        "bk": 97,
        "cf": 98,
        "es": 99,
        "fm": 100,
        "md": 101,
        "no": 102,
        "lr": 103,
        "rf": 104,
        "db": 105,
        "sg": 106,
        "bh": 107,
        "hs": 108,
        "mt": 109,
        "ds": 110,
        "rg": 111,
        "cn": 112,
        "nh": 113,
        "fl": 114,
        "mc": 115,
        "lv": 116,
        "ts": 117,
        "og": 118
    }
}


inp = input("""
Write a sentence to be converted chemically
=> """)

# write a function tath takes a string and devolve a array of each letter


def get_letters(string):
    letters = []
    for i in string:
        letters.append(i)
    return letters


inp = get_letters(inp.lower())

final = ""

i = 0
while i < len(inp):
    if i < len(inp) - 1:
        if f'{inp[i]}{inp[i+1]}' in data['len2']:
            final += f'{data["len2"][f"{inp[i]}{inp[i+1]}"]} '
            i += 1
        elif f'{inp[i]}' in data['len1']:
            final += f'{data["len1"][f"{inp[i]}"]} '
        elif inp[i] == " ":
            final += " "
        else:
            final += f'{inp[i]} '
    else:
        if f'{inp[i]}' in data['len1']:
            final += f'{data["len1"][f"{inp[i]}"]} '
        else:
            final += f'{inp[i]}'

    i += 1

print(final)

system("pause")
