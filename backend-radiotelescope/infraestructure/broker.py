import os
import paho.mqtt.publish as publish
import string


class MQTTBrokerImp:

    def __init__(self) -> None:
        pass

    def publishMQTT(topic: string, pyload: string) -> None:
        auth = {"username": os.getenv(
            "BROKER_USER"), "password": os.getenv("BROKER_PASSWORD")}
        publish.single(topic=topic, pyload=pyload, hostname=os.getenv("BROKER_HOST"),
                       port=os.getenv("BROKER_PORT"), auth=auth)
