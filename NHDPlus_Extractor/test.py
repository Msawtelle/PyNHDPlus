from NHDPlus_Extractor_Class import NHDPlusExtractor
from shapefile import Reader



y = Reader(r"C:\Users\User\Data\NHDPlusCI\NHDPlus21\NHDSnapshot\Hydrography\NHDFlowline")
print(y.fields)


x = NHDPlusExtractor(r'C:\Users\User\Data')
x.extract_HUC8('21','21010002','C:\\Users\\User\\Data')
# print([ for x in y.fields if x[0] == 'REACHCODE'])
# for x in y.fields:
#     if x[0] == 'REACHCODE':
#         print(x[0]+ str(y.fields.index(x)))
#     else:
#         print(x[0] + 'is not equal to REACHCODE')
