# 🚀 Práctica 3: Implementación de Servicio DNS RESTful

Este proyecto documenta la migración de un sistema distribuido basado en **Java RMI** a una arquitectura **RESTful** moderna utilizando **Python** y el framework **FastAPI**.

---

## 📌 Descripción del Proyecto
El objetivo principal ha sido transformar una lógica de comunicación basada en invocaciones remotas (RPC) a un paradigma basado en **recursos (REST)**, garantizando la interoperabilidad total mediante **HTTP/1.1** y el intercambio de datos estructurados en **JSON**.

### 🛠️ Características Técnicas
* **Arquitectura:** Stateless (sin estado), siguiendo los principios REST.
* **Protocolo:** HTTP/1.1 sobre TCP.
* **Validación:** Uso de modelos **Pydantic** para garantizar la integridad de los recursos DNS (`nombre`, `ip`, `ttl`).
* **Documentación:** Generación automática de especificaciones mediante **OpenAPI (Swagger/ReDoc)**.

---

## 📂 Estructura del Repositorio
- `main.py`: Punto de entrada de la API y definición de los endpoints.
- `schemas.py`: Definición de los modelos de datos para la validación.
- `informe/`: Contiene el informe técnico en formato **PDF** y las evidencias de tráfico (**capturas Wireshark**).

---

## 🚀 Guía de Inicio y Ejecución

### 1. Requisitos Previos
* **Python 3.10+** instalado.
* `pip` (gestor de paquetes de Python).

### 2. Instalación y Ejecución
Clona el repositorio, prepara el entorno y pon en marcha el servidor:

```bash
# 1. Clonar el repositorio
git clone <url-de-tu-repo>
cd dns-rest-api

# 2. Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Linux/macOS
# O en Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install fastapi uvicorn

# 4. Iniciar el servidor
uvicorn main:app --reload
