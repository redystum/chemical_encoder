from os import system
import sys
import json

def e():
    system("pause")
    sys.exit(0)

try:
    f = open("./Periodic_Table.json", "r")
    f.close()
except:
    print("The periodic table is necessary for this program to run, do you want to create it?")
    inp = input("y/n => ").lower()
    y = ['yes', 'y']

    if inp in y:
        import convert
    else:
        sys.exit(0)



try:
    f = open('Periodic_Table.json', 'r')
    data = json.load(f)
    f.close()
except:
    print("Periodic Table not found")
    e()

if len(data) != 2:
    print("The current periodic table is corrupted, please delete it and run the program again by choosing \"y\" in the create table menu")
    e()

else:
    if len(data['len1']) + len(data['len2']) != 118:
        print("The current periodic table is corrupted, please delete it and run the program again by choosing \"y\" in the create table menu")
        e()

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
names = ""
names_list = ""

i = 0
try:
    while i < len(inp):
        if i < len(inp) - 1:
            if f'{inp[i]}{inp[i+1]}' in data['len2']:
                final += f'{data["len2"][f"{inp[i]}{inp[i+1]}"]["number"]} '
                names += f'{data["len2"][f"{inp[i]}{inp[i+1]}"]["name"]} '
                names_list += f'{data["len2"][f"{inp[i]}{inp[i+1]}"]["number"]} = {data["len2"][f"{inp[i]}{inp[i+1]}"]["name"]}\n'
                i += 1
            elif f'{inp[i]}' in data['len1']:
                final += f'{data["len1"][f"{inp[i]}"]["number"]} '
                names += f'{data["len1"][f"{inp[i]}"]["name"]} '
                names_list += f'{data["len1"][f"{inp[i]}"]["number"]} = {data["len1"][f"{inp[i]}"]["name"]}\n'
            else:
                final += f'{inp[i]} '
        else:
            if f'{inp[i]}' in data['len1']:
                final += f'{data["len1"][f"{inp[i]}"]["number"]}'
                names += f'{data["len1"][f"{inp[i]}"]["name"]}'
                names_list += f'{data["len1"][f"{inp[i]}"]["number"]} = {data["len1"][f"{inp[i]}"]["name"]}'

        i += 1

except:
    print("Error loading Periodic Table")
    e()

print("\n" + final + "\n")
print(names + "\n")
print(names_list + "\n")    

system("pause")