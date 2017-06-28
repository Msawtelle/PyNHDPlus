import dbf
from NHDPlus_Extractor_Class import NHDPlusExtractor
import os
from shapefile import Reader,Writer

### PlusFlowlinVAA files are encoded in cp1252
###



x = NHDPlusExtractor(r'C:\Users\User\Data')
a=0
z=0
y=0
for DA in x.DA_to_VPU.keys():
    # print(x.DA_to_VPU[DA])
    # print(len(x.DA_to_VPU[DA]))
    for i in range(len(x.DA_to_VPU[DA])):
        DAPATH = r'{}\NHDPlus{}'.format(x.destination,DA)
        VAAPATH = r'{}\{}{}\{}\{}'.format(DAPATH,'NHDPlus',x.DA_to_VPU[DA][i],
                                        'NHDPlusAttributes','PlusFlowlineVAA.dbf')
        mydbf = open(VAAPATH,'rb')
        sf = Reader(dbf=mydbf)
        w = Writer()
        for b in range(1,len(sf.fields)):
            sf.fields[b][0] = sf.fields[b][0].upper()
            a+=1
            print(a)
        w.fields = list(sf.fields)
        records = sf.records()
        for row in records:
            args = row
            w.record(*args)
        w.save(VAAPATH)
        mydbf.close()




        # w = Writer()
        # for b in range(1,len(sf.fields)):
        #     sf.fields[b][0] = sf.fields[b][0].upper()
        # w.fields = list(sf.fields)
        # w.save('VAAPATH')
        # mydbf.close()
        # print(w.fields)


    # for i in range(len(x.DA_to_VPU[DA])):
    #     DAPATH = '{}\\NHDPlus{}'.format(x.destination,DA)
    #     ELEVSLOPEVPATH = '{}\\{}{}\\{}\\{}'.format(DAPATH,'NHDPlus',x.DA_to_VPU[DA][i],
    #                                     'NHDPlusAttributes','elevslope.dbf')
    #
    #     table = dbf.Table(ELEVSLOPEVPATH)
    #     print(table)
    #     z+=1
    #     print(z)
    #
    # for i in range(len(x.DA_to_VPU[DA])):
    #     DAPATH = '{}\\NHDPlus{}'.format(x.destination,DA)
    #     EROMPATH = '{}\\{}{}\\{}\\{}'.format(DAPATH,'NHDPlus',x.DA_to_VPU[DA][i],
    #                                     'EROMExtension','EROM_MA0001.DBF')
    #     if os.path.isfile(EROMPATH):
    #         table = dbf.Table(EROMPATH)
    #         print(table)
    #         a+=1
    #         print(a)
