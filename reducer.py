import os 
from collections import defaultdict

# Diccionario para almacenar todas las fechas de acceso por usuario
user_accesses = defaultdict(list)

for file in os.listdir("splits"):
    if file.endswith(".out"):
        with open(f"splits/{file}", 'r') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 3:  # usuario fecha hora
                    user = parts[0]
                    date_time = " ".join(parts[1:])  # fecha y hora completa
                    user_accesses[user].append(date_time)

# Mostrar todos los accesos por usuario
for user, dates in user_accesses.items():
    print(f"Usuario: {user}")
    for i, date_time in enumerate(dates):
        print(f"  {i + 1}: {date_time}")
    print(f"Total accesos fuera de horario: {len(dates)}")
    print("-" * 40)

# Guardar el resultado en un archivo
with open("accesos_fuera_de_horario.txt", 'w') as out:
    for user, dates in user_accesses.items():
        out.write(f"Usuario: {user}\n")
        for i, date_time in enumerate(dates):
            out.write(f"  {i + 1}: {date_time}\n")
        out.write(f"Total accesos fuera de horario: {len(dates)}\n")
        out.write("-" * 40 + "\n")