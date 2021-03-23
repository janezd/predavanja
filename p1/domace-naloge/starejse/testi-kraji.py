svet = {
         "Evropa": {
             "Slovenija": {
                 "Gorenjska": {
                     "Kranj": {},
                     "Radovljica": {},
                     "Zali log": {},
                 },
                 "Štajerska": {
                     "Maribor": {},
                     "Celje": {}
                 },
                 "Osrednja": {
                     "Ljubljana": {
                         "Vič": {
                             "FRI": {
                                 "P1": {
                                     "tretja vrsta desno": {
                                         "peti stol z desne": {
                                             "Benjamin": {}
                                         }
                                     }
                                 }
                             }
                         },
                         "Šiška": {}
                     }
                 }
             },
             "Nemčija": {
                 "Bavarska": {
                     "Munchen": {}
                 },
                 "Berlin": {}
             },
         },
         "Amerika": {
             "ZDA": {
                 "Teksas": {
                     "Houston": {},
                     "Austin": {}
                 },
                 "Kalifornija": {
                     "San Francisco": {}
                 },
                 "Anchorage": {}
             },
             "Kanada": {}
         },
         "Azija": {
             "Osaka": {}
         }
        }

hisa = {
    "Klet": {
        "kurilnica": {
            "peč": {},
            "metla": {}
        },
        "shramba": {
            "spodnja polica": {
                "kisle kumare": {},
                "rdeča pesa": {}
            },
            "zgornja polica": {
                "škatla piškotov": {
                    "crknjena miš": {},
                    "pol piškota": {}
                }
            }
        },
    },
    "Prvo nadstropje": {
        "soba": {
            "računalnik": {},
            "jaz": {}
        },
        "otroška soba": {
            "Martin": {
                "ostali piškoti": {}
            }
        }
    }
}



import unittest

class Kraji(unittest.TestCase):
    def testiraj_prestej(self):
        self.assertEqual(prestej(svet), 33)
        self.assertEqual(prestej(hisa), 19)
        self.assertEqual(prestej({}), 0)
        self.assertEqual(prestej({"ena": {}}), 1)
        self.assertEqual(prestej({"ena": {}, "dva": {}}), 2)
        self.assertEqual(prestej({"ena": {"dva": {"tri": {}}}}), 3)

    def testiraj_kje_je_preprosti(self):
        self.assertListEqual(kje_je("ena", {"ena": {}}), ["ena"])
        self.assertListEqual(kje_je("ena", {"ena": {}, "dva": {}}), ["ena"])
        self.assertListEqual(kje_je("dva", {"ena": {}, "dva": {}}), ["dva"])
        self.assertListEqual(kje_je("dva", {"ena": {"dva": {}}}), ["ena", "dva"])
        self.assertListEqual(kje_je("tri", {"ena": {"dva": {"tri": {}}}}), ["ena", "dva", "tri"])

        self.assertIsNone(kje_je("peč", {}))
        self.assertIsNone(kje_je("peč", {"ena": {}}))
        self.assertIsNone(kje_je("peč", {"ena": {}, "dva": {}}))
        self.assertIsNone(kje_je("peč", {"ena": {"dva": {}}}))
        self.assertIsNone(kje_je("peč", {"ena": {"dva": {"tri": {}}}}))

        self.assertIsNone(kje_je("", {}))
        self.assertIsNone(kje_je("", {"ena": {}}))
        self.assertIsNone(kje_je("", {"ena": {}, "dva": {}}))
        self.assertIsNone(kje_je("", {"ena": {"dva": {}}}))
        self.assertIsNone(kje_je("", {"ena": {"dva": {"tri": {}}}}))


    def testiraj_kje_je(self):
        self.assertListEqual(kje_je("Kranj", svet),
            ["Evropa", "Slovenija", "Gorenjska", "Kranj"])

        self.assertListEqual(kje_je("Nemčija", svet), ["Evropa", "Nemčija"])

        self.assertListEqual(kje_je("Amerika", svet), ['Amerika'])

        self.assertListEqual(kje_je("P1", svet),
            ['Evropa', 'Slovenija', 'Osrednja', 'Ljubljana', 'Vič', 'FRI', 'P1'])

        self.assertIsNone(kje_je("Nara", svet))

        self.assertIsNone(kje_je("", svet))

        self.assertListEqual(kje_je("peč", hisa), ["Klet", "kurilnica", "peč"])

