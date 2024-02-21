"""Kalkulators ar 4 darbībām"""

def saskaitisana(a, b):
    return a + b

def alnemsana(a, b):
    return a - b

def dalisana (a, b):
    try:
        return round(a / b, 7)
    except ZeroDivisionError:
        return "Dalīt ar 0 nedrīkst"
    
def kapinasana (a, b):
    return round(a ** b, 7)

def reizinasana(a, b):
    return round(a * b, 7)

def main():
    skaitlis1 = float(input("Pirmis skaitlis "))
    skaitlis2 = float(input("Otrs skaitlis "))
    print(""" 
        1. Saskaitīšana
        2. Atņemsana
        3. Dalīšana
        4. Reizināšana
        5. Kāpināšana
    """)
    darbiba = int(input("izvēlies darbību "))
    if darbiba == 1:
        print(saskaitisana(skaitlis1, skaitlis2))
    elif darbiba == 2:
        print(alnemsana(skaitlis1, skaitlis2))
    elif darbiba == 3:
        print(dalisana(skaitlis1, skaitlis2))
    elif darbiba == 4:
        print(reizinasana(skaitlis1, skaitlis2))
    elif darbiba == 5:
        print(kapinasana(skaitlis1, skaitlis2))
    else:
        print("Hello world!")

if __name__ == "__main__":
    main()