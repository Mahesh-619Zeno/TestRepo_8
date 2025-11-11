temps = [0, 10, 20, 30, 40, 50]
fahrenheit = []

for t in temps:
    f = (t * 9/5) + 32
    fahrenheit.append(f)

with open("temperature_report.txt", "w") as f:
    f.write("Celsius | Fahrenheit\n")
    for i in range(len(temps)):
        f.write(f"{temps[i]}       | {fahrenheit[i]:.1f}\n")

print("Temperature report generated in 'temperature_report.txt'")
