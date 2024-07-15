f = open("motto.txt","w")

f.write("Fiat Lux!")

f.close()

f = open("motto.txt", "r")

print(f.read())

f = open("motto.txt", "a")

f.write("\nLet there be light!")

f.close()

f = open("motto.txt", "r")
print(f.read())

