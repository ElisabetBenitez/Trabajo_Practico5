import psutil
import datetime

def obtener_informacion_sistema():
    # Obtener la hora del sistema
    hora_actual = datetime.datetime.now()
    print("Hora del sistema:", hora_actual)

    # Obtener estado de la memoria RAM
    memoria = psutil.virtual_memory()
    print("Estado de la memoria RAM:")
    print("  Total:", memoria.total, "bytes")
    print("  Disponible:", memoria.available, "bytes")
    print("  Usada:", memoria.used, "bytes")
    print("  Porcentaje de uso:", memoria.percent, "%")

    # Obtener almacenamiento disponible en la partición "/"
    particion_root = psutil.disk_usage('/')
    print("Almacenamiento disponible en la partición '/':")
    print("  Total:", particion_root.total, "bytes")
    print("  Usado:", particion_root.used, "bytes")
    print("  Libre:", particion_root.free, "bytes")
    print("  Porcentaje de uso:", particion_root.percent, "%")

if __name__ == "__main__":
    obtener_informacion_sistema()