import math
var_1 = ""
print("git works")
def einai_palindromi(var_1):
    return var_1 == var_1[::-1]


print("Grapse \"stop i STOP\" gia na termatiseis to script!\n")
while var_1 != "stop" and var_1 != "STOP":
    var_1 = input("Grapse ti leksi: ")
    if len(var_1) <= 1:
        print("To mikos einai poli mikro")
    elif einai_palindromi(var_1):
        print("Nai, einai palindromi\n")
        var_2 = len(var_1)
        var_2 = var_2 / 2
        var_2 = int(math.floor(var_2))
        print("H leksi exei " + str(var_2) + " xaraktires")
        var_3 = var_1[0:len(var_1) // 2]
        var_4 = var_1[len(var_1) // 2 if len(var_1) % 2 == 0 else ((len(var_1) // 2) + 1):]
        print("Ta duo misa tis leksis : " + var_3 + "-" + var_4 + "\n")
    else:
        print("Oxi, den einai palindromi\n")
