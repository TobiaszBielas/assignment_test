from os import error
import sys, json
from Handlers import trim, pad_to_multiple, add_timestamp


if __name__ == '__main__':
    try:
        json_cmd = sys.argv[1].replace("\'","\"")
        sensor = json.loads(json_cmd)
        payload = sensor["payload"]
    except:
        sys.exit("Wrong argument!")

    try:
        symbol = sys.argv[2]
        number_of_symbols = int(sys.argv[3])
    except:
        symbol = "#"
        number_of_symbols = 5

    while True:
        sensor_model = input("Enter the sensor model, or type 'exit' to close app.\n")
        sensor_copy = sensor
        if sensor_model.upper() == "WS-0001": 
            print(sensor_copy)

        elif sensor_model.upper() == "WS-0002": 
            sensor_copy["payload"] = pad_to_multiple(payload, symbol, number_of_symbols)
            print(sensor_copy)

        elif sensor_model.upper() == "WS-0003": 
            sensor_copy["payload"] = trim(payload)
            sensor_copy["payload"] = pad_to_multiple(sensor_copy["payload"], symbol, number_of_symbols)
            try:
                filename = input("Enter the name of the file to write:  ")
            except:
                filename = "WS-0003"
            try:
                results_file = open(filename + ".json", "a+")
                results_file.write(json.dumps(sensor_copy) + ",\n")
            except:
                print("Error!")
            finally:
                results_file.close()

        elif sensor_model.upper() == "WS-0004": 
            sensor_copy["payload"] = trim(payload)
            sensor_copy["payload"] = pad_to_multiple(sensor_copy["payload"], symbol, number_of_symbols)
            sensor_copy["payload"] = add_timestamp(sensor_copy["payload"])
            try:
                filename = input("Enter the name of the file to write:  ")
            except:
                filename = "WS-0004"
            try:
                results_file = open(filename + ".json", "a+")
                results_file.write(json.dumps(sensor_copy) + ",\n")
            except:
                print("Error!")
            finally:
                results_file.close()
            print(sensor_copy)

        elif sensor_model.upper() == "EXIT":
            sys.exit(0)
            
        else:
            print("Wrong sensor model!")
            
