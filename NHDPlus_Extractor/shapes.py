import dbf
from NHDPlus_Extractor_Class import NHDPlusExtractor
import os
from shapefile import Reader,Writer
from osgeo import ogr
### PlusFlowlinVAA files are encoded in cp1252
###



x = NHDPlusExtractor(r'C:\Users\User\Data')

b = [21376788, (2012, 7, 12), 4, 2, 2, 720048542, 720102010, 720026398, 720026398, 0.0, 720026398, 22.984, 0, 0, 1, 0, 0, 720026398, 720050315, 0, 0, 0, 0, 0.0, 100.0, '15080303000101', 0.971, 46003, 0, 0, 0, 0, 0, 0.6444, 21.0942, 13.3308, 0, 0.0488124732414, '']
print(len(b))
print([i for i in range(len(b))])
a=0
z=0


flowattributes = [['COMID', 'N', 9, 0], ['HYDROSEQ', 'N', 11, 0], ['UPHYDROSEQ','N', 11, 0],
                  ['DNHYDROSEQ','N', 11, 0], ['REACHCODE', 'C', 14, 0],['AREASQKM', 'N', 15, 6],
                  ['TOTDASQKM','N', 15, 6], ['DIVDASQKM','N', 15, 6]]
slopeattributes = ['COMID', 'MAXELEVSMO', 'MINELEVSMO','SLOPELENKM']
eromattributes = ['COMID', 'Q0001E', 'V0001E', 'SMGAGEID']

def read_dbf(source, comids=None, attributes = None,verbose=True):
    mydbf = open(source,'rb')
    sf = Reader(dbf=mydbf)
    print(sf.fields)
    w = Writer()
    w.fields = attributes
    fields = sf.fields[1:]
    fields = [item[0].upper() for item in fields]
    fieldsindex = {}

    #iterate over the dbf file accessing the records using attributes as a fields
    ##query. if attributes is none return all the records for all the fields
    if attributes is None: attributes = fields


    for attribute in attributes:
        print(attribute)
        y = [pos for pos,j in enumerate(fields) if attribute[0] == j]
        print(y)
        fieldsindex[attribute[0]] = y[0]

    for rec in enumerate(sf.records()):
        pass


    print(fieldsindex.keys())
read_dbf(r"C:\Users\User\Data\NHDPlusCO\NHDPlus15\NHDPlusAttributes\PlusFlowlineVAA.dbf",attributes=flowattributes)


# for DA in x.DA_to_VPU.keys():
#     # print(x.DA_to_VPU[DA])
#     # print(len(x.DA_to_VPU[DA]))
#     for i in range(len(x.DA_to_VPU[DA])):
#         DAPATH = r'{}\NHDPlus{}'.format(x.destination,DA)
#         VAAPATH = r'{}\{}{}\{}\{}'.format(DAPATH,'NHDPlus',x.DA_to_VPU[DA][i],
#                                         'NHDPlusAttributes','PlusFlowlineVAA.dbf')
#         mydbf = open(VAAPATH,'rb')
#         sf = Reader(dbf=mydbf)
#
#         fields  = sf.fields[1:]
#         fields = [item[0].upper() for item in fields]
#
#         for attribute in flowattributes:
#
#             y = [pos + 1 for pos,j in enumerate(fields) if attribute == j]
#             print(y, attribute)


# mydbf = open(r"C:\Users\User\Data\NHDPlusCO\NHDPlus15\NHDPlusAttributes\PlusFlowlineVAA.dbf",'rb')
# sf = Reader(dbf=mydbf)
# w = Writer()
# w.fields = sf.fields
# fields  = sf.fields[1:]
# fields = [item[0].upper()for item in fields]
# print(fields)
# for attribute in flowattributes:
#
#     y = [pos + 1 for pos,j in enumerate(fields) if attribute == j ]
#     print(y, attribute)
#
#     if y is not []:

# for attribute in flowattributes:
#     for pos, field in enumerate(sf.fields)



# print(sf.fields)
# print(len(sf.fields))
#  # for b in range(len(sf.fields)):
#  #     for attribute in flowattributes:
#  #         if attribute == sf.fields[b][0].upper():
#  #            y = sf.fields[b]
#
#
#
# for rec in enumerate(sf.records()):
#     print(rec)
# print(fields)
# mydbf.close()
# def readdbf(source, attributes=None, comids=None, verbose=True):
#     sourcedbf = open(source,'rb')
#     sf = Reader(dbf=sourcedbf)
#     for attribute in range(len(sf.fields)):
#         fields.append(sf.fields[attribute][0].upper())
#
#     for attribute in fields:
#         if attribute == 'COMID':
#             comid_index = fields.index(attribute)
#         elif attribute == 'HYDROSEQ':
#             hyd



# for DA in x.DA_to_VPU.keys():
#     # print(x.DA_to_VPU[DA])
#     # print(len(x.DA_to_VPU[DA]))
#     for i in range(len(x.DA_to_VPU[DA])):
#         DAPATH = r'{}\NHDPlus{}'.format(x.destination,DA)
#         VAAPATH = r'{}\{}{}\{}\{}'.format(DAPATH,'NHDPlus',x.DA_to_VPU[DA][i],
#                                         'NHDPlusAttributes','PlusFlowlineVAA.dbf')
#         mydbf = open(VAAPATH,'rb')
#         sf = Reader(dbf=mydbf)
#
#         for b in range(len(sf.fields)):
#             fields.append(sf.fields[b][0].upper())
#
#         a+=1
#         print(a)
#         print([x for x in fields])
#
#         for attribute in flowattributes:
#             if attribute
#         # w.fields = list(sf.fields)
#         # records = sf.records()
#         # for row in records:
#         #     args = row
#         #     w.record(*args)
#         # w.save(VAAPATH)
#         # mydbf.close()
#
#
#
#
#         # w = Writer()
#         # for b in range(1,len(sf.fields)):
#         #     sf.fields[b][0] = sf.fields[b][0].upper()
#         # w.fields = list(sf.fields)
#         # w.save('VAAPATH')
#         # mydbf.close()
#         # print(w.fields)
#
#
#     # for i in range(len(x.DA_to_VPU[DA])):
#     #     DAPATH = '{}\\NHDPlus{}'.format(x.destination,DA)
#     #     ELEVSLOPEVPATH = '{}\\{}{}\\{}\\{}'.format(DAPATH,'NHDPlus',x.DA_to_VPU[DA][i],
#     #                                     'NHDPlusAttributes','elevslope.dbf')
#     #
#     #     table = dbf.Table(ELEVSLOPEVPATH)
#     #     print(table)
#     #     z+=1
#     #     print(z)
#     #
#     # for i in range(len(x.DA_to_VPU[DA])):
#     #     DAPATH = '{}\\NHDPlus{}'.format(x.destination,DA)
#     #     EROMPATH = '{}\\{}{}\\{}\\{}'.format(DAPATH,'NHDPlus',x.DA_to_VPU[DA][i],
#     #                                     'EROMExtension','EROM_MA0001.DBF')
#     #     if os.path.isfile(EROMPATH):
#     #         table = dbf.Table(EROMPATH)
#     #         print(table)
#     #         a+=1
#     #         print(a)
