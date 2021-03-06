from simulation.speedLimits import *
from simulation.trafficGenerators import * 

maxFps= 40
size = width, heigth = 1280, 720
# in miliseconds
updateFrame = 500

seed = None

lanes = 3
length = 300

maxSpeed = 2

speedLimits = [ SpeedLimit(range=((150,0),(300,0)), limit=3, ticks=0), SpeedLimit(range=((220, 2), (300,2)), limit=3, ticks=0) ]
trafficGenerator = SimpleTrafficGenerator(1)
slowDownProbability, laneChangeProbability = 0.4, 0.2
