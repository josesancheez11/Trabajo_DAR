# 🌐 Práctica 2: Sistema DNS Distribuido (Java RMI)

Este módulo contiene la implementación de un servidor DNS utilizando la tecnología **Java Remote Method Invocation (RMI)**. El objetivo principal ha sido evolucionar el protocolo de paso de mensajes manual (Sockets) de la práctica anterior hacia un modelo de **invocación directa de métodos remotos**.

---

## 🚀 Decisiones de Diseño

Para garantizar un sistema robusto y eficiente, se han adoptado las siguientes soluciones:

* **Interfaz Remota (`IDNSService`)**: Define el contrato entre cliente y servidor.
* **Caché Concurrente**: Implementación mediante `ConcurrentHashMap` para evitar condiciones de carrera.
* **Gestión de TTL (Lazy Deletion)**: El servidor calcula la expiración al insertar y limpia el registro solo bajo demanda.
* **Transparencia de Red**: Configuración manual de la IP mediante `java.rmi.server.hostname`.

---

## 🛠️ Instrucciones de Ejecución

> [!IMPORTANT]
> Es imprescindible que ambas máquinas estén en la **misma red local** y que los Firewalls permitan el tráfico en el puerto **1099**.

### Pasos para la terminal:
```bash
# 1. Compilación de todos los archivos fuente
# Desde la carpeta raíz del proyecto:
javac *.java

# 2. Ejecución del Servidor
# Para que el servidor sea accesible desde otras máquinas, ejecuta el comando indicando tu IP local (Sustituye 192.168.X.X por tu IP real):
java -Djava.rmi.server.hostname=192.168.X.X ServidorDNS

# 3. Ejecución del Cliente
# Ejecuta el cliente apuntando a la IP donde se encuentra el servidor:
java ClienteDNS 192.168.X.X
