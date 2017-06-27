import os
from NHDPlus_Extractor_Class import NHDPlusExtractor




############
# Before using make sure destination in the NHDPlusExtractor __init__ method is set to the path of your data folder
#
############

x = NHDPlusExtractor()



for vpu in sorted(x.VPU_to_RPU.keys()):

    for files in x.VPU_Files:
        print(vpu + ' ' + files)
        y = x.getvpufile(vpu, files)
        if y is not None:
            y = y.split('/')[-1]
        else:
            continue

        if os.path.exists(os.path.join(x.destination, y)):
            print(y + ' already exists moving on')
            pass

        else:
            x.downloadvpufile(vpu,files)

for rpu in sorted(x.RPU_to_VPU.keys()):

    for files in x.RPU_Files:
        print(rpu + ' ' + files)
        y = x.getrpufile(rpu, files)
        if y is not None:
            y = y.split('/')[-1]
            print(y)
        else:
            continue

        if os.path.exists(os.path.join(x.destination, y)):
            print(y + ' already exists moving on')
            pass

        else:
            x.downloadrpufile(rpu, files)

for dirpath, subdir, files in os.walk(x.destination):

    for data in files:
        x.decompress(os.path.join(dirpath, data))
