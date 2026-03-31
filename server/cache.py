import time

# Diccionario global que almacena los registros
cache = {}

def agregar_registro(nombre, ip, ttl):
    cache[nombre] = {
        "ip": ip,
        "ttl_original": ttl,
        "timestamp_creacion": time.time()
    }

def calcular_ttl_restante(registro):
    tiempo_actual = time.time()
    tiempo_transcurrido = tiempo_actual - registro["timestamp_creacion"]
    ttl_restante = registro["ttl_original"] - tiempo_transcurrido
    return int(ttl_restante)

def resolver_dominio(nombre):
    if nombre not in cache:
        return None, "NOTFOUND"

    registro = cache[nombre]
    ttl_restante = calcular_ttl_restante(registro)

    if ttl_restante <= 0:
        del cache[nombre]
        return None, "NOTFOUND"

    return (registro["ip"], ttl_restante), "OK"

def limpiar_cache():
    ahora = time.time()
    dominios_a_borrar = []

    for nombre, registro in cache.items():
        ttl_restante = registro["ttl_original"] - (ahora - registro["timestamp_creacion"])
        if ttl_restante <= 0:
            dominios_a_borrar.append(nombre)

    for nombre in dominios_a_borrar:
        del cache[nombre]   
