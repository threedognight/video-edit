__author__ = 'loki'
from bitstring import ConstBitStream, ReadError
import os
from filetimes import filetime_to_dt, dt_to_filetime, utc
s = ConstBitStream(filename='test3.avi')
statinfo = os.stat('test3.avi')
print statinfo.st_size
print ("Current bytepos %X" % s.bytepos)
# Search to Start of Frame 0 code on byte boundary
foundMoviOffset = s.find('0x6D6F7669', bytealigned=True)
if foundMoviOffset:
    moviOffset = foundMoviOffset[0] / 8
    print("Found movi signature at byte offset %X" % moviOffset)
else:
    print "Signature movi not found"
print ("Current bytepos %X" % s.bytepos)
foundIdx1Offset = s.find('0x69647831', bytealigned=True)
if foundIdx1Offset:
    idx1Offset = foundIdx1Offset[0] / 8
    print("Found idx1 signature at byte offset %X" % idx1Offset)
else:
    print "Signature idx1 not found"
print ("Current bytepos %X" % s.bytepos)
found01dcOffset = s.findall('0x30316463', bytealigned=True)
for i in found01dcOffset:
    i = (i /8) + 8
    print("%X" % i)
    s.bytepos = i
    print s.bytepos
    timeStamp = s.read(64).bin
    print timeStamp

    print ("Time is %d" % timeStamp)
    # print filetime_to_dt(timeStamp)
    # s.bytepos = i + 4
    # print s.bytepos
    # timelow = s.read(32).Q
    # t = float(timehigh)*2**32 + timelow
    # print (t*1e-7 - 11644473600)
# try:
#     while True:
#         found01dbOffset2 = s.readto('0x30316462')
#         _01dbOffsetList.append((s.bytepos))
#         _01dbOffsetArray.append((s.bytepos))
#         print ("!!Current bytepos %X" % s.bytepos)
# except ReadError:
#     print "Oops! The file end here )"
# for i in _01dbOffsetArray:
#     print("%X" % i)