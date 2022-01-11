FROM eclipse-mosquitto:1.6.10
ENV BROKER_USER=radiogis
ENV BROKER_PASSWORD=broker.radio@2019
RUN echo ${BROKER_USER}":"${BROKER_PASSWORD} > /mosquitto/passwords
RUN cat /mosquitto/passwords
RUN mosquitto_passwd -U /mosquitto/passwords
RUN sed -i 's/#allow_anonymous true/allow_anonymous false/g' /mosquitto/config/mosquitto.conf
RUN sed -i 's/#password_file/password_file \/mosquitto\/passwords/g' /mosquitto/config/mosquitto.conf 
