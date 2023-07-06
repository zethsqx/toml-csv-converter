import os
import toml
import csv

result = []
filename = 'output2.csv'

def print_file_names(folder_path):
    count = 0
    for root, dirs, files in os.walk(folder_path):
        if "_deprecated" in root:
            continue  # Skip the current folder if it matches the ignore string
        for file in files:
            if file in ["README.md","NOTICE.txt"]:
                continue
            else:
                ruleline = [str(count)]
                count = count + 1
                
                file_path = os.path.join(root, file)
                
##                try:
##                    data = toml.load(file_path)
##                    ruleline.append(data['rule']['name'])
##                    try:
##                        ruleline.append(str(data['metadata']['integration']))
##                    except Exception as e:
##                        ruleline.append(" ")
##                    ruleline.append(data['rule']['type'])
##                    try:
##                        ruleline.append(str(data['rule']['index']))
##                    except Exception as e:
##                        ruleline.append(" ")
##                    ruleline.append(str(data['rule']['tags']))
##                    ruleline.append(data['rule']['description'].replace("\n", ""))
##                    ruleline.append(root.replace("C:\\Users\\Test\\Documents\\detection-rules\\rules\\", ""))
##                except Exception as e:
##                    ruleline.append("An error occurred: ")
##                    ruleline.append(file_path)
                ruleline.append(file)
                line = '| '.join(ruleline)
                #print(line)
                result.append(line)
        #if count > 100:
            #break;


    with open(filename, 'a') as file:
        for line in result:
            file.write(line + '\n')
            
# Provide the folder path where your TOML files are located
folder_path = "C:\\Users\\Test\\Documents\\detection-rules\\rules"
print_file_names(folder_path)
