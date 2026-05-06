paisa = int(input("Enter paisa: "))

rupees = paisa // 100
p = paisa % 100

print(rupees, "Rupees and", p, "Paisa")

if rupees % 5 == 0:
    print("Only 5 & 10 Rupee Notes Possible: Yes")
else:
    print("Only 5 & 10 Rupee Notes Possible: No")
