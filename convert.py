string = """1__Hydrogen__H
2__Helium__He
3__Lithium__Li
4__Beryllium__Be
5__Boron__B
6__Carbon__C
7__Nitrogen__N
8__Oxygen__O
9__Fluorine__F
10__Neon__Ne
11__Sodium__Na
12__Magnesium__Mg
13__Aluminum__Al
14__Silicon__Si
15__Phosphorus__P
16__Sulfur__S
17__Chlorine__Cl
18__Argon__Ar
19__Potassium__K
20__Calcium__Ca
21__Scandium__Sc
22__Titanium__Ti
23__Vanadium__V
24__Chromium__Cr
25__Manganese__Mn
26__Iron__Fe
27__Cobalt__Co
28__Nickel__Ni
29__Copper__Cu
30__Zinc__Zn
31__Gallium__Ga
32__Germanium__Ge
33__Arsenic__As
34__Selenium__Se
35__Bromine__Br
36__Krypton__Kr
37__Rubidium__Rb
38__Strontium__Sr
39__Yttrium__Y
40__Zirconium__Zr
41__Niobium__Nb
42__Molybdenum__Mo
43__Technetium__Tc
44__Ruthenium__Ru
45__Rhodium__Rh
46__Palladium__Pd
47__Silver__Ag
48__Cadmium__Cd
49__Indium__In
50__Tin__Sn
51__Antimony__Sb
52__Tellurium__Te
53__Iodine__I
54__Xenon__Xe
55__Cesium__Cs
56__Barium__Ba
57__Lanthanum__La
58__Cerium__Ce
59__Praseodymium__Pr
60__Neodymium__Nd
61__Promethium__Pm
62__Samarium__Sm
63__Europium__Eu
64__Gadolinium__Gd
65__Terbium__Tb
66__Dysprosium__Dy
67__Holmium__Ho
68__Erbium__Er
69__Thulium__Tm
70__Ytterbium__Yb
71__Lutetium__Lu
72__Hafnium__Hf
73__Tantalum__Ta
74__Tungsten__W
75__Rhenium__Re
76__Osmium__Os
77__Iridium__Ir
78__Platinum__Pt
79__Gold__Au
80__Mercury__Hg
81__Thallium__Tl
82__Lead__Pb
83__Bismuth__Bi
84__Polonium__Po
85__Astatine__At
86__Radon__Rn
87__Francium__Fr
88__Radium__Ra
89__Actinium__Ac
90__Thorium__Th
91__Protactinium__Pa
92__Uranium__U
93__Neptunium__Np
94__Plutonium__Pu
95__Americium__Am
96__Curium__Cm
97__Berkelium__Bk
98__Californium__Cf
99__Einsteinium__Es
100__Fermium__Fm
101__Mendelevium__Md
102__Nobelium__No
103__Lawrencium__Lr
104__Rutherfordium__Rf
105__Dubnium__Db
106__Seaborgium__Sg
107__Bohrium__Bh
108__Hassium__Hs
109__Meitnerium__Mt
110__Darmstadtium__Ds
111__Roentgenium__Rg
112__Copernicium__Cn
113__Nihonium__Nh
114__Flerovium__Fl
115__Moscovium__Mc
116__Livermorium__Lv
117__Tennessine__Ts
118__Oganesson__Og"""

data = {}
data['len1'] = {}
data['len2'] = {}

s = string.split('\n')

for i in range(0, len(s)):
    s[i] = s[i].split('__')    

for i in range(0, len(s)):
    if len(s[i][2]) == 1:
        
        data["len1"][f"{s[i][2].lower()}"] = {}
        data["len1"][f"{s[i][2].lower()}"]['number'] = s[i][0]
        data["len1"][f"{s[i][2].lower()}"]['name'] = s[i][1]

    else:
        data["len2"][f"{s[i][2].lower()}"] = {}
        data["len2"][f"{s[i][2].lower()}"]['number'] = s[i][0]
        data["len2"][f"{s[i][2].lower()}"]['name'] = s[i][1]


import json

f = open('Periodic_Table.json', 'w')

json.dump(data, f, indent=4)

f.close()