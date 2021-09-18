import time


def trim(payload):
    if payload[0] == " ":
        payload = payload[1:]
    
    if payload[-1] == " ":
        payload = payload[:-1]
    
    return payload

def pad_to_multiple(payload, symbol, number_of_symbols):
    symbol *= number_of_symbols
    return payload + symbol

def add_timestamp(payload):
    timestamp = int(time.time())
    return payload + '_' + str(timestamp)