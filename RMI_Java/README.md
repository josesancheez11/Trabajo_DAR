🌐 Práctica 2: Sistema DNS Distribuido (Java RMI)
Este módulo contiene la implementación de un servidor DNS utilizando la tecnología Java Remote Method Invocation (RMI). El objetivo principal ha sido evolucionar el protocolo de paso de mensajes manual (Sockets) de la práctica anterior hacia un modelo de invocación directa de métodos remotos.

🚀 Decisiones de Diseño
Para garantizar un sistema robusto y eficiente, se han adoptado las siguientes soluciones:

Interfaz Remota (IDNSService): Define el contrato entre cliente y servidor. El uso de métodos tipados (add y query) elimina errores de formato y simplifica la lógica del programador.

Caché Concurrente: Implementación mediante ConcurrentHashMap para permitir el acceso simultáneo de múltiples clientes sin condiciones de carrera.

Gestión de TTL (Lazy Deletion): El servidor calcula el instante de expiración en la inserción. La limpieza se realiza "bajo demanda" durante la consulta, optimizando el uso de CPU al evitar hilos de limpieza en segundo plano.

Transparencia de Red: Uso de java.rmi.server.hostname para superar las limitaciones de localhost y permitir el funcionamiento en redes locales reales (Hotspots, LAN universitaria).

🛠️ Instrucciones de Ejecución
[!IMPORTANT]
Es imprescindible que ambas máquinas (Cliente y Servidor) estén conectadas a la misma red local y que los Firewalls permitan el tráfico en el puerto 1099.

1. Compilación
Desde la terminal, compila todos los archivos fuente:

Bash
javac IDNSService.java DNSServiceImpl.java ServidorDNS.java ClienteDNS.java
2. Ejecución del Servidor
Modifica en ServidorDNS.java la IP por tu IP local:
System.setProperty("java.rmi.server.hostname", "TU_IP_AQUI");

Lanza el servicio:

Bash
java ServidorDNS
3. Ejecución del Cliente
Asegúrate de que la IP en Naming.lookup("rmi://IP_SERVIDOR/ServicioDNS") sea la correcta en ClienteDNS.java.

Inicia el cliente:

Bash
java ClienteDNS
📋 Integrantes
José Sánchez Bueno

Sergio Mozas Blanca
