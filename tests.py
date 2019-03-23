# from datasources import tests

import datasources
print(dir(datasources))

# from Landsat8 import Landsat8
#
#
# class Landsat8TestCases(tests.BaseTestCases):
#
#     def _setUp(self):
#         self.datasource = Landsat8
#         self.spatial = {
#                         "type": "Polygon",
#                         "coordinates": [
#                           [
#                             [
#                               -96.84173583984374,
#                               32.713355353177555
#                             ],
#                             [
#                               -96.63848876953125,
#                               32.713355353177555
#                             ],
#                             [
#                               -96.63848876953125,
#                               32.88189375925038
#                             ],
#                             [
#                               -96.84173583984374,
#                               32.88189375925038
#                             ],
#                             [
#                               -96.84173583984374,
#                               32.713355353177555
#                             ]
#                           ]
#                         ]
#                       }
#         self.temporal = ("2017-01-01", "2017-12-31")
#         self.properties = {"landsat:processing_level": {"eq": "L1TP"}}
#         self.limit = 20
