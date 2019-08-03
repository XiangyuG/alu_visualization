import re
import sys
import argparse

def main(argv):
    if (len(argv) != 2):
        print("Usage: python3 " + argv[0] + " <file_name>")
        sys.exit(1)
    file_name = str(argv[1])
    # Read file into string
    f = open(file_name,"r")
    file_string = f.read()
    search_result = re.findall('int' +' (\w+) ' + '= (\d)', file_string)
    print(len(search_result))
    # search result will store the hole_name and hole_value
    for i in range(len(search_result)):
        # we do not need to deal with input_0_0
        if (search_result[i][0].find("input_") != -1):
            continue
        # pos is the pos of the hole_
        pos = file_string.find(search_result[i][0])
        while (pos != -1):
            pos = file_string.find(search_result[i][0],pos + 1)
            if (file_string[pos + len(search_result[i][0])] != '_'):
                # Because we cannot do assignment directly to string
                list_file_string = list(file_string)
                list_file_string[pos : pos + len(search_result[i][0])] = search_result[i][1]
                file_string = ''.join(list_file_string)
    
    file = open("/tmp/test.sk", "w")
    file.write(file_string)
    file.close()

if __name__ == "__main__":
    main(sys.argv)
