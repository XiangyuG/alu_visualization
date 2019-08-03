import re
import sys

# Read file into string
f = open("/Users/Xiangyu/Downloads/stateful_fw_canonicalizer_equivalent_0_pred_raw_stateless_alu_4_5_verify_iter_12.sk","r")
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
