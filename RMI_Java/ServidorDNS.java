import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class ServidorDNS {
    public static void main(String[] args) {
        try {
            // OPCIONAL: Configurar la IP programáticamente si se pasa por argumento
            // System.setProperty("java.rmi.server.hostname", "192.168.1.XX");

            // Crear el registro RMI en el puerto 1099
            LocateRegistry.createRegistry(1099);

            DNSServiceImpl service = new DNSServiceImpl();
            Naming.rebind("ServicioDNS", service);

            System.out.println("Servidor DNS RMI listo y esperando conexiones...");
        } catch (Exception e) {
            System.err.println("Error en el servidor: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
