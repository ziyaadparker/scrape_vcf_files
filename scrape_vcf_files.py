import datetime
import re
import os

f_o = open('indels_samples.csv', 'w')
#looping through file directory
root = "indels"
path = os.path.join(root, "samples")
for path, subdirs, files in os.walk(root):
    for name in files:
        if name.endswith(".vcf"):
            vcf_file = os.path.join(path, name)

            #reads through the files
            with open(vcf_file) as f:
                for line in f.readlines():
                    if line.startswith('##fileDate'):
                        line_date = line.split('=')
                        date_string = line_date[1]
                        date_string = date_string.strip()
                    elif line.startswith('##command'):
                        line_sample = line.split('-s')

                        sample_id = line_sample[1].split(' ')
                        vcf_file = vcf_file.split('/')
                        file_name = vcf_file[1]

                        #formats the date
                        date = datetime.datetime.strptime(date_string, '%Y%m%d')
                        date.strftime("%Y-%M-%d %H:%M:%S")
                        date = date.isoformat("T") + "Z"

                output = file_name + ','  + sample_id[1] + ',' + date_string
                print (output)
                #exports output to csv file
                f_o.write(output + '\n')
