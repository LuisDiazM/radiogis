# Proyecto de radioastronomía

El presente proyecto contiene la plataforma creada por radiogis para centralizar diferentes proyectos de investigación.

La plataforma involucra tecnologías como python, postgres, broker mqtt mosquitto, gunicorn, y docker compose para orquestar el servicio.


Para correr la plataforma de manera local se requiere instalar docker y docker-compose.

## Instalación de docker
Puede seguir la documentación oficial de docker [enlace oficial](https://docs.docker.com/engine/install/ubuntu/), o también ejecutar los siguientes comandos en ubuntu:

```
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
sudo apt-get install docker-ce docker-ce-cli containerd.io
```
## Instalación de docker-compose
Puede seguir la documentación oficial para la instalación [enlace](https://docs.docker.com/compose/install/) o ejecutar los siguientes pasos para linux:

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose
```

Verificar la instalación:

``docker-compose --version``

# Ejecutar localmente la plataforma

Una vez instalado docker y docker-compose, para correr la plataforma se requiere ejecutar el siguiente comando:

``docker-compose up`` y esperar unos 3 min ya que hay unos scripts de configuración que tienen retardos, una vez pasados los tres minutos puede abrir el navegador y entrar a [enlace](http://localhost:8000).

Para ingresar a la plataforma se crearon las siguientes credenciales de prueba:

- username: mario
- password: mario