![Imagen de cabecera](https://nattia.com/wp-content/uploads/2023/11/que-es-docker.webp)
# Proyecto Educativo: Comunicación entre Contenedores en Docker

## Descripción
Este repositorio tiene una finalidad educativa. Contiene dos aplicaciones en Python que demuestran la comunicación entre contenedores Docker utilizando sockets TCP. El objetivo es aprender a configurar, desplegar y probar contenedores Docker que interactúan en una red.

---

## Características
- Aplicación servidor que escucha en el puerto `2025` y muestra los mensajes recibidos.
- Aplicación cliente que envía mensajes al servidor según los datos ingresados por el usuario.
- Despliegue sencillo con contenedores Docker.
- Configuración de red automática usando la red `bridge` predeterminada de Docker.
- Ejemplo adaptado para propósitos educativos.

---

## Cómo Empezar

### Descargar el Repositorio
1. **Clona este repositorio usando git**:
    ```
   git clone https://github.com/rpiealb297/docker-network-example
   ```
2. **Accede al directorio del proyecto**:
   ```
   cd docker-network-example
   ```

### Instalación de Docker
1. **Instalar Docker**:
   - Descarga Docker Desktop desde su página oficial: [Docker](https://www.docker.com/).
   - Sigue las instrucciones para tu sistema operativo (Windows, macOS, Linux).
2. **Verificar la instalación**:
   Ejecuta en tu terminal:
   ```bash
   docker --version
   ```
   Deberías ver la versión de Docker instalada.

---

## Cómo Configurarlo

### Modificar los Scripts de Python
- **`servidor.py`**:
  - Si el servidor debe escuchar en un puerto diferente, edita la variable `PORT`.
  - Si deseas agregar funcionalidades, como autenticación o validación de datos, puedes modificar el bucle que procesa los mensajes en el servidor.

- **`cliente.py`**:
  - Cambia la variable `HOST` al nombre del contenedor del servidor (en el entorno Docker).
  - Si quieres usar un puerto diferente, modifica la variable `PORT`.
  - Puedes adaptar la lógica del cliente para enviar mensajes de manera automatizada o leer de un archivo.

### Desplegar los Contenedores
1. Construye las imágenes Docker para ambos servicios:
   ```bash
   docker build -t servidor -f Dockerfile-servidor .
   docker build -t cliente -f Dockerfile-cliente .
   ```
2. Ejecuta el contenedor del servidor:
   ```bash
   docker run --rm --name servidor servidor
   ```
3. Ejecuta el contenedor del cliente:
   ```bash
   docker run --rm --name cliente --link servidor -it cliente
   ```

---

## Cómo Ejecutar la App

### Servidor
1. El servidor se ejecuta automáticamente al levantar su contenedor.
2. Mostrará el mensaje recibidos en la consola.

### Cliente
1. El cliente permite al usuario escribir un mensaje desde la consola.
2. El mensaje es recibido en el servidor y termina la aplicación.

---

## Pruebas
1. **Levanta el servidor**:
   ```bash
   docker run --rm --name servidor servidor
   ```
2. **Levanta el cliente** en otra terminal:
   ```bash
   docker run --rm --name cliente --link servidor -it cliente
   ```
3. Escribe mensajes en el cliente y verifica que aparecen en el servidor.

---

