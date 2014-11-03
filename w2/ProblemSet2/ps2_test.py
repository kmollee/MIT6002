import unittest
import random
from ps2 import Position, RectangularRoom, Robot


class PositionTest(unittest.TestCase):

    def setUp(self):
        pass

    def testConstruct(self):
        a = Position(1, 2)

    def testGetCoordinate(self):
        a = Position(1, 2)
        self.assertEquals(a.getX(), 1)
        self.assertEquals(a.getY(), 2)

    def testNewPosition(self):
        a = Position(0, 0)
        newA = a.getNewPosition(37, 5)
        self.assertEquals(abs(newA.getX() - 3) < 0.01, True)
        self.assertEquals(abs(newA.getY() - 4) < 0.01, True)


class RectangularRoomTest(unittest.TestCase):

    def setUp(self):
        pass

    def testConstruct(self):
        R = RectangularRoom(2, 1)
        self.assertEquals(R.tiles, [[1], [1]])
        R = RectangularRoom(1, 1)
        self.assertEquals(R.tiles, [[1]])

    def testgetNumTiles(self):
        self.assertEquals(RectangularRoom(6, 2).getNumTiles(), 12)
        self.assertEquals(RectangularRoom(5, 5).getNumTiles(), 25)
        self.assertEquals(RectangularRoom(6, 6).getNumTiles(), 36)
        self.assertEquals(RectangularRoom(2, 2).getNumTiles(), 4)
        self.assertEquals(RectangularRoom(3, 4).getNumTiles(), 12)

    def testIsTileCleaned(self):
        room = RectangularRoom(2, 2)
        self.assertEquals(room.isTileCleaned(0, 0), False)
        self.assertEquals(room.isTileCleaned(0, 1), False)
        self.assertEquals(room.isTileCleaned(1, 0), False)
        self.assertEquals(room.isTileCleaned(1, 1), False)

    def testCleanTileAtPosition(self):
        room = RectangularRoom(2, 2)
        room.cleanTileAtPosition(Position(0.5, 0))
        room.cleanTileAtPosition(Position(1, 1.5))
        self.assertEquals(room.isTileCleaned(0, 0), True)
        self.assertEquals(room.isTileCleaned(1, 1), True)
        self.assertEquals(room.isTileCleaned(1, 0), False)
        self.assertEquals(room.isTileCleaned(0, 1), False)

    def testGetNumCleanedTiles(self):
        room = RectangularRoom(2, 2)
        self.assertEquals(room.getNumCleanedTiles(), 0)
        room.cleanTileAtPosition(Position(0.5, 0))
        room.cleanTileAtPosition(Position(1, 1.5))
        self.assertEquals(room.isTileCleaned(0, 0), True)
        self.assertEquals(room.isTileCleaned(1, 1), True)
        self.assertEquals(room.isTileCleaned(1, 0), False)
        self.assertEquals(room.isTileCleaned(0, 1), False)
        self.assertEquals(room.getNumCleanedTiles(), 2)
        room.cleanTileAtPosition(Position(0, 1))
        self.assertEquals(room.getNumCleanedTiles(), 3)

    def testIsPositionInRoom(self):
        room = RectangularRoom(2, 2)
        for i in range(30):
            randX = random.uniform(0.0, 2.0)
            randY = random.uniform(0.0, 2.0)
            self.assertEquals(
                room.isPositionInRoom(Position(randX, randY)), True)
        for i in range(30):
            randX = random.uniform(2.0, 3.0)
            randY = random.uniform(2.0, 3.0)
            self.assertEquals(
                room.isPositionInRoom(Position(randX, randY)), False)


class RobotTest(unittest.TestCase):

    def setUp(self):
        self.room = RectangularRoom(5, 5)

    def testConstruct(self):
        R1 = Robot(self.room, 1)
        R2 = Robot(self.room, 2)
        R3 = Robot(self.room, 3)

    def testgetRobotPosition(self):
        R1 = Robot(self.room, 1)
        R2 = Robot(self.room, 1)
        R3 = Robot(self.room, 1)
        for R in [R1, R2, R3]:
            P = R.getRobotPosition()
            self.assertTrue(isinstance(P, Position))
            self.assertTrue(0 <= P.getX() < 5)
            self.assertTrue(0 <= P.getY() < 5)

    def testsetRobotPosition(self):
        R1 = Robot(RectangularRoom(5, 8), 1.0)
        R1.getRobotPosition()
        for i in range(10):
            x = random.uniform(0.0, 10.0)
            y = random.uniform(0.0, 10.0)
            if self.room.isPositionInRoom(Position(x, y)):
                R1.setRobotPosition(Position(x, y))
                self.assertEquals(
                    (R1.getRobotPosition().x, R1.getRobotPosition().y), (x, y))

    def testsetRobotDirection(self):
        robot = Robot(RectangularRoom(5, 8), 1.0)
        robot.getRobotDirection()
        for i in range(10):
            angle = random.uniform(0.0, 360.0)
            robot.setRobotDirection(angle)
            self.assertEquals(robot.getRobotDirection(), angle)

    def testupdatePositionAndClean(self):
        robot = Robot(RectangularRoom(5, 5), 4.0)
        for i in range(10):
            self.assertRaises(
                NotImplementedError, robot.updatePositionAndClean)

if __name__ == "__main__":
    unittest.main()
