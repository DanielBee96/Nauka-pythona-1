def daj_rabat(klient_vip, kwota):
   
    if klient_vip == True or kwota > 1000:
        return "Rabat 10%"
    else:
        return "Brak rabatu"

# TESTY
print("Test 1:", daj_rabat(True, 200))
print("Test 2:", daj_rabat(False, 1500))
print("Test 3:", daj_rabat(False, 500)) 

# True and False , Dwa argumenty !