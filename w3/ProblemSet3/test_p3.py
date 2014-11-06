import unittest
import random
from ps3b import Patient, SimpleVirus, ResistantVirus, NoChildException


class SimpleVirusTest(unittest.TestCase):

    def setUp(self):
        pass

    def testConstruct(self):
        for _ in range(100):
            SimpleVirus(random.random(), random.random())

    def testgetMaxBirthProb(self):
        r = [i * 0.01 for i in range(100)]
        for i in r:
            tmp = SimpleVirus(i, 0)
            self.assertEquals(tmp.getMaxBirthProb(), i)

    def testgetClearProb(self):
        r = [i * 0.01 for i in range(100)]
        for i in r:
            tmp = SimpleVirus(1, i)
            self.assertEquals(tmp.getClearProb(), i)

    def testdoesClear(self):
        v1 = SimpleVirus(1.0, 0.0)
        self.assertEquals(v1.doesClear(), False)
        v1 = SimpleVirus(1.0, 1.0)
        self.assertEquals(v1.doesClear(), True)


class PatientTest(unittest.TestCase):

    def setUp(self):
        self.virusesList = []
        for _ in range(5):
            self.virusesList.append(
                SimpleVirus(random.random(), random.random()))

    def testConstruct(self):
        for _ in range(100):
            Patient(self.virusesList, random.random())

    def testgetTotalPop(self):
        P1 = Patient(self.virusesList, 7)
        self.assertEquals(P1.getTotalPop(), 5)

    def testAlwaysReproduces(self):
        """
        Create a Patient with virus that is never cleared and always reproduces
        """
        virus = SimpleVirus(1.0, 0.0)
        patient = Patient([virus], 100)
        for _ in range(50):
            patient.update()
        self.assertEquals(patient.getTotalPop(), 100)
        # patient.getTotalPop() expected to be == 100

    def testAlwaysCleared(self):
        """
        Create a Patient with virus that is always cleared and always reproduces
        """
        virus = SimpleVirus(1.0, 1.0)
        patient = Patient([virus], 100)
        for _ in range(50):
            patient.update()
        self.assertEquals(patient.getTotalPop(), 0)
        # patient.getTotalPop() expected to be == 100


class TestResistantVirus(unittest.TestCase):

    def setUp(self):
        pass

    def testReproduces(self):
        """
        Create a ResistantVirus that is never cleared and always reproduces.
        """
        virus = ResistantVirus(1.0, 0.0, {}, 0.0)
        print('virus = ResistantVirus(1.0, 0.0, {}, 0.0)')
        print(
            'Testing update() and doesClear(); virus should not be cleared and should always reproduce.')
        for _ in range(15):
            try:
                virus = virus.reproduce(10, {})
            except NoChildException:
                pass
            self.assertEquals(virus.doesClear(), False)

        print('Test completed.')

    def testNoClearedNoReproduces(self):
        """
        Create a ResistantVirus that is never cleared and never reproduces.
        """
        virus = ResistantVirus(0.0, 0.0, {}, 0.0)
        print('virus = ResistantVirus(0.0, 0.0, {}, 0.0)')
        print(
            'Testing update() and doesClear(); virus should not be cleared and should never reproduce.')
        for _ in range(50):
            self.assertRaises(NoChildException, virus.reproduce, 10, {})
            self.assertEquals(virus.doesClear(), False)

        print('Test completed.')
if __name__ == "__main__":
    unittest.main()
