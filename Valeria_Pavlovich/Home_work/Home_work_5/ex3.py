def analyze_temps(temps):
    avg = sum(temps) / len(temps)
    anomalies = 0
    for temp in temps:
        if temp > 30 or temp < -10:
            anomalies += 1
    return {'avg': avg,
            'max': max(temps),
            'min': min(temps),
            'anomalies': anomalies}
temps_input = input("Enter temperatures separated by space: ")
temps = list(map(float, temps_input.split()))
result = analyze_temps(temps)
print(result)