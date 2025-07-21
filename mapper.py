import sys 
from collections import defaultdict

filename = sys.argv[1]
with open(filename, 'r') as f:
    lines = f.read().strip().split('\n')

# Diccionario para almacenar las fechas de acceso fuera de horario por usuario
horas_fuera = defaultdict(list)

for line in lines:
    parts = line.split()
    if len(parts) >= 3:
        date_str = parts[0]
        time_str = parts[1]
        user = parts[2]
        
        # Extraer solo la hora (formato HH:MM:SS)
        hour = int(time_str.split(':')[0])
        
        # Verificar si está fuera del horario laboral (08:00 a 18:00)
        if hour < 8 or hour >= 18:
            horas_fuera[user].append(f"{date_str} {time_str}")

with open(f"{filename}.out", 'w') as out:
    for user, dates in horas_fuera.items():
        for date_time in dates:
            out.write(f"{user} {date_time}\n")