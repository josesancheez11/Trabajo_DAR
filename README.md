# Caso de Uso 11: Protocolo de Resolución de Nombres

## 1. Descripción del Proyecto
Este proyecto implementa un protocolo de aplicación cliente-servidor diseñado para resolver nombres simbólicos en direcciones IP. El servidor gestiona una base de datos de registros en caché, controlando el ciclo de vida de cada entrada mediante tiempos de validez (TTL).

## 2. Arquitectura General
* **Protocolo de Transporte:** Se utiliza **TCP**, garantizando que los mensajes de consulta y respuesta lleguen sin errores y en orden.
* **Gestión de Concurrencia:** El servidor utiliza la librería `threading` de Python para gestionar múltiples clientes simultáneamente. Cada conexión entrante se deriva a un hilo independiente.
* **Mecanismo de Caché:** El servidor mantiene un diccionario interno donde almacena las asociaciones Nombre-IP y el TTL restante. Una vez el TTL expira, el registro se marca como inválido.

## 3. Requisitos de Ejecución
* **Lenguaje:** Python 3.10 o superior
* **Sistema Operativo:** Windows (probado en entorno local y red local).
* **Librerías:** Únicamente librerías estándar de Python (`socket`, `threading`, `time`). No requiere instalaciones externas.

## 4. Instrucciones de Lanzamiento
Para probar el protocolo en dos máquinas distintas:

1.  **En el ordenador Servidor:**
    Obtener la IP local (ej. 192.168.1.XX) y ejecutar:
    python servidor.py
    
2.  **En el ordenador Cliente:**
    Ejecutar el script apuntando a la IP del servidor
    python cliente.py 192.168.1.XX
    

## 5. Ejemplos de Uso
### 📋 Especificación de Comandos

| Comando | Sintaxis | Descripción | Ejemplo de Respuesta |
| :--- | :--- | :--- | :--- |
| **ADD** | `ID ADD <nombre> <IP> <TTL>` | Registra un dominio en la caché con un tiempo de vida. | `ID OK` |
| **QUERY** | `ID QUERY <nombre>` | Consulta la IP y el TTL restante de un nombre. | `ID OK <IP> <TTL>` |
| **NOTFOUND** | `-` | Respuesta del servidor si el dominio no existe o expiró. | `ID NOTFOUND` |
| **SALIR** | `salir` | Finaliza la sesión TCP de forma ordenada. | `Desconexión` |
