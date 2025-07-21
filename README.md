# 🕐 Sistema de Análisis de Accesos Fuera de Horario

Sistema MapReduce que identifica accesos de usuarios fuera del horario laboral (08:00 - 18:00).

## 🎯 ¿Qué hace?
Analiza registros de acceso y detecta cuándo los usuarios ingresan al sistema fuera del horario de trabajo.

## 📋 Componentes
- **`mapper.py`**: Filtra accesos fuera de horario
- **`reducer.py`**: Consolida resultados de todos los mappers

## 📊 Formato de Datos
**Entrada:** `2025-07-26 19:30:00 daniel`  
**Salida:** `usuario:daniel 2025-07-26 19:30:00`

## 🚀 Uso
```bash
python mapper.py archivo.txt    # Procesar archivo
python reducer.py               # Consolidar resultados
```

## 📝 Resultado
```
Usuario: daniel
  1. 2025-07-26 07:30:00
  2. 2025-07-26 19:30:00
Total accesos fuera de horario: 2
```

## 📁 Estructura del Proyecto
```
taller/
├── mapper.py                    # Procesador de archivos individuales
├── reducer.py                   # Consolidador de resultados
├── docker-compose.yml           # Configuración Docker
├── Dockerfile                   # Imagen del contenedor
├── split_entrada.sh             # Script para dividir archivos
├── logs.txt                     # Registro de ejecución
├── accesos_fuera_de_horario.txt # Resultado final consolidado
├── splits/                      # Carpeta con archivos divididos
│   ├── part_00.txt             # Archivo de entrada 1
│   ├── part_00.txt.out         # Resultado del mapper 1
│   ├── part_01.txt             # Archivo de entrada 2
│   ├── part_01.txt.out         # Resultado del mapper 2
│   ├── part_02.txt             # Archivo de entrada 3
│   ├── part_02.txt.out         # Resultado del mapper 3
│   ├── part_03.txt             # Archivo de entrada 4
│   └── part_03.txt.out         # Resultado del mapper 4
└── README.md                    # Este archivo
```
