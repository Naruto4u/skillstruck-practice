F1 = int(input("1"))
F2 = int(input("2"))
F3 = int(input("3"))
F4 = int(input("4"))
F5 = int(input("5"))

def WHY(FT1,FT2,FT3,FT4,FT5):
    smallest = FT1
    if FT2 < FT1:
        smallest = FT2
    if FT3 < FT2:
        smallest = FT3
    if FT4 < FT3:
        smallest = FT4
    if FT5 < FT4:
        smallest = FT5
    print(smallest)
WHY(F1,F2,F3,F4,F5)
