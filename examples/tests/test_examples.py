import pytest
import subprocess
import os

AscentVehicles = [r'BFR', r'GoddardRocket', r'Titan-II-SSTO']
Astrodynamics = [r'Detumble']
AtmosphericFlight = [r'HangGlider', r'Hypersonic3DOFfamily', r'HypersonicNose', r'SpaceShuttle']
Classic = [r'AlyChan', r'Brachistochrone', r'BrysonDenham', r'MoonLander', r'ZermelosProblem']
ElectricityAndMagnetism = [r'OneLoopCircuit']
Oscillators = [r'FinancialOscillator', r'MallsOscillator', r'Rayleigh']


@pytest.mark.parametrize("file", AscentVehicles)
def test_AscentVehicles(file):
    fpath = os.path.dirname(__file__)
    path = os.path.realpath(fpath + r'/../../examples/AscentVehicles/' + file + '/' + file + '.py')
    assert subprocess.call(['python', path]) == 0

@pytest.mark.parametrize("file", Astrodynamics)
def test_Astrodynamics(file):
    fpath = os.path.dirname(__file__)
    path = os.path.realpath(fpath + r'/../../examples/Astrodynamics/' + file + '/' + file + '.py')
    assert subprocess.call(['python', path]) == 0

def test_AstrodynamicsHT():
    fpath = os.path.dirname(__file__)
    path = os.path.realpath(fpath + r'/../../examples/Astrodynamics/OrbitRaising/HighThrust.py')
    assert subprocess.call(['python', path]) == 0


def test_AstrodynamicsLT():
    fpath = os.path.dirname(__file__)
    path = os.path.realpath(fpath + r'/../../examples/Astrodynamics/OrbitRaising/LowThrust.py')
    assert subprocess.call(['python', path]) == 0


@pytest.mark.parametrize("file", AtmosphericFlight)
def test_AtmosphericFlight(file):
    fpath = os.path.dirname(__file__)
    path = os.path.realpath(fpath + r'/../../examples/AtmosphericFlight/' + file + '/' + file + '.py')
    assert subprocess.call(['python', path]) == 0


@pytest.mark.parametrize("file", Classic)
def test_Classic(file):
    fpath = os.path.dirname(__file__)
    path = os.path.realpath(fpath + r'/../../examples/Classic/' + file + '/' + file + '.py')
    assert subprocess.call(['python', path]) == 0


@pytest.mark.parametrize("file", ElectricityAndMagnetism)
def test_ElectricityAndMagnetism(file):
    fpath = os.path.dirname(__file__)
    path = os.path.realpath(fpath + r'/../../examples/ElectricityAndMagnetism/' + file + '/' + file + '.py')
    assert subprocess.call(['python', path]) == 0


@pytest.mark.parametrize("file", Oscillators)
def test_Oscillators(file):
    fpath = os.path.dirname(__file__)
    path = os.path.realpath(fpath + r'/../../examples/Oscillators/' + file + '/' + file + '.py')
    assert subprocess.call(['python', path]) == 0
