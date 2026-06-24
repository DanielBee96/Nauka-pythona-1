# Sesja 4 - funkcje def
def ocen_test(wynik):
    if wynik >= 90:
        print("Ocena: 5. Szacun!")
    elif wynik >= 70:
        print("Ocena: 4. Dobrze Ci idzie.")
    else:
        print("Ocena: 3. Trzeba docisnąć.")

print("Sprawdzam wyniki:")
ocen_test(95)  # pierwszy uczeń
ocen_test(82)  # drugi uczeń
ocen_test(60)  # trzeci uczeń