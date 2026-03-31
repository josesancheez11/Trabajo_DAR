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
[!IMPORTANT]
Para evitar el error No such file or directory, asegúrate de situar la terminal en la carpeta raíz del proyecto antes de ejecutar los comandos.

🏠 Opción A: Prueba en la misma máquina (Localhost)
Es la forma más rápida de testear el protocolo. Abre dos terminales y ejecuta:

Terminal 1 (Servidor):

Bash
python server/server.py
Terminal 2 (Cliente):

Bash
python client/client.py 127.0.0.1
🌐 Opción B: Prueba en red (Dos máquinas)
Ideal para verificar la conectividad real entre distintos hosts:

En el PC Servidor: Ejecuta el script y anota tu IP local (ej. 192.168.1.XX).

Bash
python server/server.py
En el PC Cliente: Lanza el script apuntando a la IP del servidor.

Bash
python client/client.py 192.168.1.XX
## 5. Ejemplos de Uso
### 📋 Especificación de Comandos

| Comando | Sintaxis | Descripción | Ejemplo de Respuesta |
| :--- | :--- | :--- | :--- |
| **ADD** | `ID ADD <nombre> <IP> <TTL>` | Registra un dominio en la caché con un tiempo de vida. | `ID OK` |
| **QUERY** | `ID QUERY <nombre>` | Consulta la IP y el TTL restante de un nombre. | `ID OK <IP> <TTL>` |
| **NOTFOUND** | `-` | Respuesta del servidor si el dominio no existe o expiró. | `ID NOTFOUND` |
| **SALIR** | `salir` | Finaliza la sesión TCP de forma ordenada. | `Desconexión` |

## 6. Estructura del Repositorio

Para facilitar la navegación por el proyecto, los archivos se han organizado de la siguiente manera:

```text
/
├── client/
│   └── client.py          
├── server/
│   ├── server.py         
│   ├── cache.py            
│   └── protocol.py        
├── docs/
│   ├── capturas/           
│   ├── trafico_red/        
│   └── ESPECIFICACION PROTOCOLO.pdf  
└── README.md
```
## 7. Verificación del Protocolo (Análisis de Tráfico)

Para garantizar la robustez del sistema, se ha realizado un análisis exhaustivo con **Wireshark**, cuyas evidencias se encuentran en la carpeta `/docs`. Los hitos verificados son:

*   **Handshake TCP:** Confirmación del establecimiento de conexión fiable (SYN, SYN-ACK, ACK) antes de cualquier intercambio de datos de aplicación.
*   **Integridad de PDUs:** Verificación de que los comandos `ADD` y `QUERY` se transmiten íntegramente respetando el formato definido.
*   **Dinámica del TTL:** Observación en tiempo real de cómo el servidor descuenta los segundos de validez en respuestas `QUERY` sucesivas hasta la expiración del registro.
*   **Gestión de Errores:** Validación de la respuesta `NOTFOUND` ante consultas de dominios inexistentes o registros caducados.

> **Nota:** Las trazas originales en formato `.pcapng` están disponibles para su inspección técnica detallada en la ruta `docs/trafico_red/`.
