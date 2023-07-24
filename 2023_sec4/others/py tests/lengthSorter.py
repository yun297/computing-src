lst = [
    "AIDEN CHEN",
    "ANG WAY LONG ANG ZUO CHERN",
    "CHEN YOUJIA CHENG",
    "DYLAN SHIYING",
    "CHOK XIAN HAO ETHAN",
    "CHUA JUN XIANG ISAAC",
    "CHUA YIN HERNG ETHAN",
    "DARIUS NG ZEN LOONG",
    "DERRIUS TAN JUN KAI",
    "DEXTON PHUA JUN XIANG",
    "ETHAN JOSH LOW",
    "GAO SIQI",
    "GERARD YAU YUN",
    "HUI LI REN TIMOTHY (XU LIREN)",
    "JOEL NG",
    "JOSHUA ONG JING ZHI",
    "KAVEN LEONG KA WAI",
    "LEE YUAN ZHE ANZAC",
    "LIOW ZHI KAI JOSHUA",
    "LUO KECHENG DAVID",
    "MAX LEI JUN TING",
    "PANG YANG ZHI",
    "RYAN CHAY HUAI CI",
    "SENG KOI HAN KYAN",
    "SIM JUN REN",
    "YIP LER YANG GABRIEL",
    "ZACH TIO"
]

def sortLength(lst):
    lst.sort(key = len)
    return lst

for i in sortLength(lst):
    print(i)