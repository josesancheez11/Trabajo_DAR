import java.rmi.Remote;
import java.rmi.RemoteException;

public interface IDNSService extends Remote {
    String query(String nombre) throws RemoteException;

    void add(String nombre, String ip, int ttl) throws RemoteException;
}