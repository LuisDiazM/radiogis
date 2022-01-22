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

``docker-compose up`` y esperar unos 3 min ya que hay unos scripts de configuración que tienen retardos, una vez pasados los tres minutos puede abrir el navegador y entrar a [enlace](http://localhost:80).

Para ingresar a la plataforma se crearon las siguientes credenciales de prueba:

- username: admin
- password: admin

# Configuración de Casiri para poder usar por primera vez

Casiri requiere de unas configuraciones iniciales para poder capturar datos, a continuación se enumerarán los pasos a seguir:

1. Registrar los estados, para ello debe ingresar al siguiente [link](http://127.0.0.1/radioastronomia/subsistema/estados/camara-estacion) y dar click en el botón, "Registrar estados"
2. Registrar la Resolución de ancho de banda del dispositivo, para ello se puede basar en las especificaciones del E310 o del LimeSDR, por ejemplo: para el E310 puede registrar 16000000, 8000000, 4000000, 2000000, 1000000 y escoger FFT 1024 y 2048. La de 4096 es una toma más fina pero puede bloquear el dispositivo. Para este registro puede ingresar al siguiente [link](http://127.0.0.1/radioastronomia/crear/RBW)
3. Registrar la antena con la cual se tomarán datos, la plataforma de manera interna hace las correcciones en frecuencia de la antena o el cable, para que la medición sea más precisa se recomienda caracterizar con un VNA el VSWR del cable con la antena que se van a tomar los datos, el VNA exporta un archivo CSV que podemos cargar en la plataforma.

En caso de no tener caracterizada la antena y el cable que se conectará, se puede usar una caracterización fantasma que agrega pérdidas casi nulas, esta caracterización está dentro del rango 1MHz ~ 2.9GHz, la pueden encontrar en la carpeta [config/VNAcero.csv](/backend/config/VNAcero.csv), para registrar la antena ingresar al siguiente [link](http://127.0.0.1/radioastronomia/crear/antenas) allí pedirá datos del nombre de la antena, rango de frecuencias, una foto de la antena y el archivo csv de la caracterización.

4. Una vez realizados los pasos 1 ~ 3 procedemos a registrar la zona de campaña, para ello es recomendable tomar una foto al lugar como para tener una referencia, para registrar la zona de campaña se ingresa al siguiente [link](http://127.0.0.1/radioastronomia/crear/region)

Si todo sale bien es posible que podamos empezar a [tomar datos RFI](http://127.0.0.1/radioastronomia/control-manual) desde la plataforma mediante el control manual o control automático, lo anterior es posible si se tienen los periféricos conectados.