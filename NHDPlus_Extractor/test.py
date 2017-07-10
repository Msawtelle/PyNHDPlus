from NHDPlus_Extractor_Class import NHDPlusExtractor
from shapefile import Reader



# y = Reader(r"C:\Users\User\Data\NHDPlusCI\NHDPlus21\NHDSnapshot\Hydrography\NHDFlowline")



x = NHDPlusExtractor(r'C:\Users\Mitchell\Downloads')

flowattributes = [['COMID', 'N', 9, 0], ['HYDROSEQ', 'N', 11, 0], ['UPHYDROSEQ','N', 11, 0],
                  ['DNHYDROSEQ','N', 11, 0], ['REACHCODE', 'C', 14, 0],['AREASQKM', 'N', 15, 6],
                  ['TOTDASQKM','N', 15, 6], ['DIVDASQKM','N', 15, 6]]
x.read_dbf(r"C:\Users\Mitchell\Downloads\NHDPlusMS\NHDPlus11\NHDPlusAttributes\PlusFlowlineVAA.dbf",attributes=flowattributes,comids=[7621376,24557283])

# print([ for x in y.fields if x[0] == 'REACHCODE'])
# for x in y.fields:
#     if x[0] == 'REACHCODE':
#         print(x[0]+ str(y.fields.index(x)))
#     else:
#         print(x[0] + 'is not equal to REACHCODE')
