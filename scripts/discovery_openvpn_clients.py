#!/usr/local/bin/python35

# Read file and return an array of the file or portion if specified, like an array with which line like a value
def read_file_part_specific(begin=None, end=None, status_file="/var/log/openvpn-status.log"):
    file = open(status_file, 'r')
    lines = file.readlines()
    for line in lines:
        index = lines.index(line)
        lines[index] = line.replace("\n", "")
    if (begin is not None and end is not None):
        begin_index = lines.index(begin)
        end_index = lines.index(end)
        return lines[begin_index:end_index]
    elif (begin is not None and end is None):
        begin_index = lines.index(begin)
        return lines[begin_index:]
    else:
        return lines


# Convert array passed into a json in a format that Zabbix server accepts.
# Support legacy format for Server in version prior than 4.2
def convert_array_to_json_zabbix_server_v4_0(array_file):
    # Imports:
    import json
    # Declare an array to construct an array of from the array argument:
    array_dic = []
    # Iterate to construct an array of Dictionaries from the array argument:
    for x in range(2, len(array_file)):
        # Extracting values, putting in single arrays and cleaning values:
        array_single = array_file[x].split(",")
        # Mount Dictionary and Add Dictionary in list
        array_dic.append({"{#CNAME}": array_single[1], "{#IPVIRTUAL}": array_single[0]})
    # Return Dic with Arrays of Dicts values:
    dict_array = {"data": array_dic}
    return json.dumps(dict_array)


def convert_array_to_json_zabbix_server_v4_2(array_file):
    # Imports:
    import json
    # Declare an array to construct an array of from the array argument:
    array_dic = []
    # Iterate to construct an array of Dictionaries from the array argument:
    for x in range(2, len(array_file)):
        # Extracting values, putting in single arrays and cleaning values:
        array_single = array_file[x].split(",")
        # Mount Dictionary and Add Dictionary in list
        array_dic.append({"{#CNAME}": array_single[1], "{#IPVIRTUAL}": array_single[0]})
    # Return Dic with Arrays of Dicts values:
    return json.dumps(array_dic)


# Execute if standalone program
if __name__ == '__main__':
    import sys
    argsLen = len(sys.argv)
    if argsLen < 3:
        print("Missing parameter")
    elif argsLen == 3:
        print(convert_array_to_json_zabbix_server_v4_2(read_file_part_specific(sys.argv[1], sys.argv[2])))
    elif argsLen == 4:
        if sys.argv[3] == "4.0":
            print(convert_array_to_json_zabbix_server_v4_0(read_file_part_specific(sys.argv[1], sys.argv[2])))
        elif sys.argv[3] == "4.2":
            print(convert_array_to_json_zabbix_server_v4_2(read_file_part_specific(sys.argv[1], sys.argv[2])))
        else:
            print(convert_array_to_json_zabbix_server_v4_2(read_file_part_specific(sys.argv[1], sys.argv[2], sys.argv[3])))
    elif argsLen == 5:
        if sys.argv[3] == "4.0":
            print(convert_array_to_json_zabbix_server_v4_0(read_file_part_specific(sys.argv[1], sys.argv[2], sys.argv[4])))
        else:
            print(convert_array_to_json_zabbix_server_v4_2(read_file_part_specific(sys.argv[1], sys.argv[2], sys.argv[4])))
