def graus_celsius(c):
    return c * 1.8 +32

c = float(input("digite a temperatura em graus celsius"))
fahrenheit = graus_celsius(c)
print(f"a temperatura em fahrenheit é {fahrenheit:.2f}°F")