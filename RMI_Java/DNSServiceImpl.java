import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.concurrent.ConcurrentHashMap;

public class DNSServiceImpl extends UnicastRemoteObject implements IDNSService {
    
    private ConcurrentHashMap<String, Registro> cache;

    class Registro {
        String ip;
        long expiracion;

        Registro(String ip, int ttl) {
            this.ip = ip;
            this.expiracion = System.currentTimeMillis() + (ttl * 1000L);
        }
    }

    public DNSServiceImpl() throws RemoteException {
        super();
        this.cache = new ConcurrentHashMap<>();
    }

    @Override
    public String query(String nombre) throws RemoteException {
        Registro reg = cache.get(nombre);

        if (reg == null) return "NOTFOUND";

        if (System.currentTimeMillis() > reg.expiracion) {
            cache.remove(nombre);
            return "NOTFOUND (Expired)";
        }

        long ttlRestante = (reg.expiracion - System.currentTimeMillis()) / 1000;
        return "IP: " + reg.ip + " | TTL Restante: " + ttlRestante + "s";
    }

    @Override
    public void add(String nombre, String ip, int ttl) throws RemoteException {
        cache.put(nombre, new Registro(ip, ttl));
        System.out.println("Añadido: " + nombre + " -> " + ip + " (TTL: " + ttl + ")");
    }
}