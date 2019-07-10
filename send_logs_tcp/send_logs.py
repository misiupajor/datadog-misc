#!/usr/bin/python
import socket

def datadogLogger(datacenter, api_key, payload):
    if datacenter == "eu":
        endpoint = "tcp-intake.logs.datadoghq.eu"
        endpoint_port = 1883
    else:
        endpoint = "intake.logs.datadoghq.com"
        endpoint_port = 10514

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect((endpoint, endpoint_port))

    payload = "{} {} \n".format(api_key, payload)

    soc.send(payload.encode("utf8"))
    soc.close()

    print("Message sent with following payload: {}\n".format(payload))

if __name__ == '__main__':
    datacenter = raw_input("Specify datacenter. 'eu' or 'us': ")
    api_key = raw_input("Specify valid api key: ")
    api_key = api_key.replace(" ","")
    payload = raw_input("Specify log message to send. Raw or in JSON: ")
    datadogLogger(datacenter, api_key, payload)