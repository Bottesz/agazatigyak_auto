def elso_feladat():
    print("I/A: ")
    auto_neve:str = input("\t Autó neve : ")
    gyartasi_datum:int = int(input("\t Gyártási év: "))
    print("I/B: ")
    if gyartasi_datum == 2022:
        print("\t Ez az autó frissen gyártott autó")
    elif gyartasi_datum < 2000:
        print("\t Ez egy öreg autó")
    else:
        print("\t Ez az autó átlagos korú")
    
