import re
from datetime import datetime

# Bloque de registros proporcionado
raw_log = """
09:32:42 | Freq: 459.25 MHz | Base: 997 uT | Fluc: 997 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:32:48 | Freq: 826.25 MHz | Base: 598 uT | Fluc: 598 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:32:54 | Freq: 303.25 MHz | Base: 199 uT | Fluc: 199 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:33:00 | Freq: 179.25 MHz | Base: 797 uT | Fluc: 797 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:33:06 | Freq: 509.25 MHz | Base: 397 uT | Fluc: 397 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:33:12 | Freq: 422.25 MHz | Base: 996 uT | Fluc: 996 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:33:18 | Freq: 900.25 MHz | Base: 600 uT | Fluc: 600 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:33:24 | Freq: 414.25 MHz | Base: 202 uT | Fluc: 202 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:33:30 | Freq: 105.25 MHz | Base: 795 uT | Fluc: 795 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:33:36 | Freq: 509.25 MHz | Base: 397 uT | Fluc: 397 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:33:48 | Freq: 84.25 MHz | Base: 602 uT | Fluc: 602 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:33:54 | Freq: 673.25 MHz | Base: 209 uT | Fluc: 209 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:34:00 | Freq: 623.25 MHz | Base: 809 uT | Fluc: 809 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:34:06 | Freq: 174.25 MHz | Base: 412 uT | Fluc: 412 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:34:18 | Freq: 491.25 MHz | Base: 613 uT | Fluc: 613 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:34:24 | Freq: 79.25 MHz | Base: 217 uT | Fluc: 217 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:34:30 | Freq: 882.25 MHz | Base: 816 uT | Fluc: 816 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:34:36 | Freq: 359.25 MHz | Base: 417 uT | Fluc: 417 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:34:48 | Freq: 639.25 MHz | Base: 617 uT | Fluc: 617 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:34:54 | Freq: 932.25 MHz | Base: 216 uT | Fluc: 216 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:35:00 | Freq: 103.25 MHz | Base: 819 uT | Fluc: 819 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:35:06 | Freq: 470.25 MHz | Base: 420 uT | Fluc: 420 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:35:17 | Freq: 791.25 MHz | Base: 573 uT | Fluc: 573 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:35:23 | Freq: 272.25 MHz | Base: 126 uT | Fluc: 126 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:35:28 | Freq: 226.25 MHz | Base: 678 uT | Fluc: 678 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:35:34 | Freq: 893.25 MHz | Base: 239 uT | Fluc: 239 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:35:40 | Freq: 68.25 MHz | Base: 794 uT | Fluc: 794 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:35:46 | Freq: 176.25 MHz | Base: 388 uT | Fluc: 388 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:35:52 | Freq: 348.25 MHz | Base: 994 uT | Fluc: 994 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:35:58 | Freq: 863.25 MHz | Base: 599 uT | Fluc: 599 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:36:04 | Freq: 377.25 MHz | Base: 201 uT | Fluc: 201 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:36:10 | Freq: 327.25 MHz | Base: 801 uT | Fluc: 801 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:36:16 | Freq: 620.25 MHz | Base: 400 uT | Fluc: 400 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:36:22 | Freq: 942.25 MHz | Base: 986 uT | Fluc: 986 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:36:28 | Freq: 345.25 MHz | Base: 585 uT | Fluc: 585 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:36:34 | Freq: 564.25 MHz | Base: 182 uT | Fluc: 182 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:36:40 | Freq: 699.25 MHz | Base: 787 uT | Fluc: 787 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:36:46 | Freq: 139.25 MHz | Base: 387 uT | Fluc: 387 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:36:51 | Freq: 163.25 MHz | Base: 989 uT | Fluc: 989 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:36:57 | Freq: 423.25 MHz | Base: 539 uT | Fluc: 539 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:37:03 | Freq: 126.25 MHz | Base: 098 uT | Fluc: 98 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:37:09 | Freq: 483.25 MHz | Base: 709 uT | Fluc: 709 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:37:15 | Freq: 628.25 MHz | Base: 304 uT | Fluc: 304 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:37:21 | Freq: 430.25 MHz | Base: 900 uT | Fluc: 900 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:37:27 | Freq: 797.25 MHz | Base: 501 uT | Fluc: 501 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:37:33 | Freq: 385.25 MHz | Base: 105 uT | Fluc: 105 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:37:39 | Freq: 594.25 MHz | Base: 712 uT | Fluc: 712 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:37:45 | Freq: 182.25 MHz | Base: 316 uT | Fluc: 316 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:37:51 | Freq: 465.25 MHz | Base: 925 uT | Fluc: 925 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
29/09/2026 09:37:57 | Freq: 943.25 MHz | Base: 529 uT | Fluc: 529 | Tipo: Anomalía Errática (Posible Manifestación Humana / Consciencia)
"""

pattern = re.compile(
    r'(?:(\d{2}/\d{2}/\d{4})\s+)?(\d{2}:\d{2}:\d{2})\s+\|\s+Freq:\s+([\d.]+)\s+MHz\s+\|\s+Base:\s+(\d+)\s+uT\s+\|\s+Fluc:\s+(\d+)'
)

parsed_data = []
for line in raw_log.strip().split('\n'):
    if not line.strip():
        continue
    match = pattern.search(line)
    if match:
        date_str, time_str, freq, base, fluc = match.groups()
        parsed_data.append({
            'date': date_str if date_str else '29/09/2026',
            'time': time_str,
            'freq': float(freq),
            'base': int(base),
            'fluc': int(fluc)
        })

print(f"[+] Total de registros parseados exitosamente: {len(parsed_data)}\n")

if parsed_data:
    freqs = [x['freq'] for x in parsed_data]
    bases = [x['base'] for x in parsed_data]
    
    print("--- ESTADÍSTICAS DEL REGISTRO ---")
    print(f"Frecuencia Mínima: {min(freqs)} MHz | Máxima: {max(freqs)} MHz | Promedio: {sum(freqs)/len(freqs):.2f} MHz")
    print(f"Campo Base Mínimo: {min(bases)} uT | Máximo: {max(bases)} uT | Promedio: {sum(bases)/len(bases):.2f} uT")
    
    # Comprobación de paridad Base == Fluc
    parity_check = all(x['base'] == x['fluc'] for x in parsed_data)
    print(f"¿Coinciden siempre Base y Fluc?: {parity_check}")

    # Análisis de intervalos de tiempo
    print("\n--- ANÁLISIS DE INTERVALOS DE TIEMPO ---")
    timestamps = [datetime.strptime(f"{x['date']} {x['time']}", "%d/%m/%Y %H:%M:%S") for x in parsed_data]
    deltas = [(timestamps[i+1] - timestamps[i]).seconds for i in range(len(timestamps)-1)]
    
    from collections import Counter
    delta_counts = Counter(deltas)
    print("Frecuencia de saltos en segundos entre registros:")
    for d, count in delta_counts.items():
        print(f"  - Salto de {d} segundos: {count} veces")
