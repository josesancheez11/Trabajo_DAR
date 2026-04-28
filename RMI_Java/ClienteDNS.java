import java.rmi.Naming;
import java.util.Scanner;

public class ClienteDNS {
    public static void main(String[] args) {
        try {
            IDNSService dns = (IDNSService) Naming.lookup("rmi://localhost/ServicioDNS");

            Scanner sc = new Scanner(System.in);
            String opcion = "";

            while (!opcion.equals("salir")) {
                System.out.println("\n--- CLIENTE DNS RMI ---");
                System.out.println("Escribe: 'query', 'add' o 'salir'");
                opcion = sc.nextLine().toLowerCase();

                if (opcion.equals("query")) {
                    System.out.print("Nombre a resolver: ");
                    String nombre = sc.nextLine();
                    String respuesta = dns.query(nombre); // Llamada remota
                    System.out.println("Resultado: " + respuesta);

                } else if (opcion.equals("add")) {
                    System.out.print("Nombre: ");
                    String nombre = sc.nextLine();
                    System.out.print("IP: ");
                    String ip = sc.nextLine();
                    System.out.print("TTL (segundos): ");
                    int ttl = Integer.parseInt(sc.nextLine());
                    
                    dns.add(nombre, ip, ttl); // Llamada remota
                    System.out.println("Registro enviado al servidor.");
                }
            }
        } catch (Exception e) {
            System.err.println("Error en el cliente: " + e.getMessage());
        }
    }
}