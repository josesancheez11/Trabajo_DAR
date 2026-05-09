import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.NotBoundException;
import java.net.MalformedURLException;
import java.util.Scanner;

public class ClienteDNS {
    public static void main(String[] args) {
        // Permitir pasar la IP por argumento para cumplir con "Ejecución distribuida"
        String host = (args.length > 0) ? args[0] : "localhost";
        String url = "rmi://" + host + "/ServicioDNS";

        try {
            System.out.println("Conectando a: " + url + "...");
            IDNSService dns = (IDNSService) Naming.lookup(url);
            
            Scanner sc = new Scanner(System.in);
            String opcion = "";

            while (!opcion.equals("salir")) {
                System.out.println("\n--- CLIENTE DNS RMI ---");
                System.out.println("Opciones: query | add | salir");
                System.out.print("> ");
                opcion = sc.nextLine().toLowerCase();

                try {
                    if (opcion.equals("query")) {
                        System.out.print("Nombre a resolver: ");
                        String nombre = sc.nextLine();
                        System.out.println("Resultado: " + dns.query(nombre));

                    } else if (opcion.equals("add")) {
                        System.out.print("Nombre (ej. google.com): ");
                        String nombre = sc.nextLine();
                        System.out.print("IP: ");
                        String ip = sc.nextLine();
                        System.out.print("TTL (segundos): ");
                        // Validación de entrada para evitar que el cliente muera por error de formato
                        int ttl = Integer.parseInt(sc.nextLine());
                        
                        dns.add(nombre, ip, ttl);
                        System.out.println("Registro añadido correctamente.");
                    }
                } catch (RemoteException re) {
                    System.err.println("Error en la llamada remota: " + re.getMessage());
                    break; // Si se pierde la conexión, salimos del bucle
                } catch (NumberFormatException nfe) {
                    System.err.println("Error: El TTL debe ser un número entero.");
                }
            }
        } catch (NotBoundException e) {
            System.err.println("Error: El servicio no está registrado en el servidor.");
        } catch (MalformedURLException e) {
            System.err.println("Error: URL de RMI inválida.");
        } catch (Exception e) {
            System.err.println("Error inesperado: " + e.getMessage());
        }
    }
}
