name = "Surya"
print(name)
try:
    print(int(name))

except ValueError as e:
    print("Error:", e)