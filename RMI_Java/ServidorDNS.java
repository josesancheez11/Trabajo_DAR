import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class ServidorDNS {
    public static void main(String[] args) {
        try {
            System.setProperty("java.rmi.server.hostname", "172.23.203.161");

            LocateRegistry.createRegistry(1099);

            DNSServiceImpl objetoRemoto = new DNSServiceImpl();

            Naming.rebind("ServicioDNS", objetoRemoto);

            System.out.println("Servidor DNS RMI funcionando correctamente...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}