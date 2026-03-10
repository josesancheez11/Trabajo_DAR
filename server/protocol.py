from cache import agregar_registro, resolver_dominio

def procesar_mensaje(mensaje):
    partes = mensaje.strip().split()

    if len(partes) < 2:
        return "ERROR malformed_request"

    query_id = partes[0]
    comando = partes[1]

    if comando == "QUERY":
        if len(partes) != 3:
            return f"{query_id} ERROR malformed_query"

        nombre = partes[2]
        resultado, estado = resolver_dominio(nombre)

        if estado == "NOTFOUND":
            return f"{query_id} NOTFOUND"

        ip, ttl = resultado
        return f"{query_id} OK {ip} TTL={ttl}"

    elif comando == "ADD":
        if len(partes) != 5:
            return f"{query_id} ERROR malformed_add"

        nombre = partes[2]
        ip = partes[3]
        ttl = int(partes[4])

        agregar_registro(nombre, ip, ttl)

        return f"{query_id} OK"

    else:
        return f"{query_id} ERROR unknown_command"
