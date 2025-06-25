def analyze_temps(temps):
    return {
        'avg': round(sum(temps) / len(temps), 1),
        'max': max(temps),
        'min': min(temps),
        'anomalies': sum(1 for t in temps if t > 30 or t < -10)
    }
print(analyze_temps([22.1, 18.5, 31.2, -5.4]))
# → {'avg': 16.6, 'max': 31.2, 'min': -5.4, 'anomalies': 2}
