Práctica 2: Sistema DNS Distribuido con Java RMI
Este módulo contiene la implementación de un servidor DNS utilizando la tecnología Java Remote Method Invocation (RMI), sustituyendo el protocolo de paso de mensajes manual (Sockets) por la invocación directa de métodos remotos.

🚀 Decisiones de Diseño
Interfaz Remota: Definida en IDNSService, establece el contrato entre cliente y servidor con métodos tipados (add y query).

Caché Concurrente: Se utiliza un ConcurrentHashMap para soportar múltiples peticiones simultáneas de forma segura.

Gestión de TTL: Implementamos un borrado de tipo Lazy Deletion. El servidor calcula la expiración al insertar y solo elimina el registro si, al ser consultado, comprueba que el tiempo actual ha superado el límite.

Transparencia de Red: Configuración manual de java.rmi.server.hostname para permitir la comunicación en redes locales reales (fuera de localhost).

🛠️ Instrucciones de Ejecución
Nota: Es necesario que ambas máquinas estén en la misma red local.

1. Compilación
Compila todos los archivos fuente desde la terminal:

Bash
javac IDNSService.java DNSServiceImpl.java ServidorDNS.java ClienteDNS.java
2. Ejecución del Servidor
Abre ServidorDNS.java y asegúrate de que la IP en System.setProperty("java.rmi.server.hostname", "TU_IP_AQUI") sea la correcta.

Lanza el servidor:

Bash
java ServidorDNS
3. Ejecución del Cliente
Abre ClienteDNS.java y verifica que la IP en el método Naming.lookup coincida con la del servidor.

Lanza el cliente:

Bash
java ClienteDNS
📋 Integrantes
José Sánchez Bueno
Sergio Mozas Blanca
