name = "Surya"
print(name)
try:
    print(int(name))

except ValueError as e:
    print("Error:", e)

p, r, t = map(float, input("Enter principal, rate of interest and time:").split())
SI = (p * r * t) / 100
print("simple interest is:", SI)