cnp = input("Introdu CNP:")
flag = True

while(len(cnp) != 13):
    cnp = input("Introdu 13 cifre!")

luna = cnp[3:5]
if (int(luna) > 13 or int(luna) < 1):
    print("Luna invalida")
    flag = False

ziua = cnp[5:7]
if (int(ziua) > 31 or int(ziua) < 1 or (int(ziua) > 29 and int(luna) == 2)):
    print("Zi invalida")
    flag = False

judet = cnp[7:9]
if (int(judet) < 1 or int(judet) > 52 or (int(judet) in [47, 48, 49, 50])):
    print("Judet invalid")
    flag = False

validator = "279146358279"
sum = 0

cnp = list(cnp)
for i in range(0, len(cnp) - 1):
    sum += int(int(cnp[i]) * int(validator[i]))

control_digit = sum % 11
if control_digit == 10:
    control_digit = 1

if control_digit != int(cnp[-1]):
    print("Validator gresit")
    flag = False


if flag:
    print("Valid cnp!")
else:
    print("Invalid cnp!")

