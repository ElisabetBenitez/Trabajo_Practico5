!/bin/bash

# Función para el contador en Python
counter() {
    local limit=$1
    local pid=$$
    local i=1
    while [ $i -le $limit ]; do
        echo "Contador $pid: $i"
        sleep 1
        ((i++))
    done
}

# Función para ejecutar el contador en Python en segundo plano
run_counter() {
    local limit=$1
    counter $limit &
    echo "PID del contador: $!"
}

# Obtener el número hasta el que se contará
echo -n "Ingrese el número máximo para contar: "
read number

# Ejecutar los contadores en Python con un bucle for
echo "Ejecutando contadores..."
for _ in {1..3}; do
    run_counter $number
done

echo "Todos los contadores están corriendo en segundo plano."