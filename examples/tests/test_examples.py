import pytest
import subprocess
import os

AscentVehicles = [r'BFR', r'GoddardRocket', r'Titan-II-SSTO']
Astrodynamics = [r'Detumble']
AtmosphericFlight = [r'HangGlider', r'HypersonicNose', r'SpaceShuttle']
Classic = [r'AlyChan', r'Brachistochrone', r'BrysonDenham', r'HangingChain', r'MoonLander', r'ZermelosProblem']
ElectricityAndMagnetism = [r'OneLoopCircuit']
Oscillators = [r'FinancialOscillator', r'MallsOscillator', r'Rayleigh']


@pytest.mark.parametrize("file", AscentVehicles)
def test_ascent_vehicles(file):
    fpath = os.path.dirname(__file__)
    path = os.path.realpath(fpath + r'/../../examples/AscentVehicles/' + file + '/' + file + '.py')
    assert subprocess.call(['python', path]) == 0


@pytest.mark.parametrize("file", Astrodynamics)
def test_astrodynamics(file):
    fpath = os.path.dirname(__file__)
    path = os.path.realpath(fpath + r'/../../examples/Astrodynamics/' + file + '/' + file + '.py')
    assert subprocess.call(['python', path]) == 0


def test_astrodynamics_ht():
    fpath = os.path.dirname(__file__)
    path = os.path.realpath(fpath + r'/../../examples/Astrodynamics/OrbitRaising/HighThrust.py')
    assert subprocess.call(['python', path]) == 0


def test_astrodynamics_lt():
    fpath = os.path.dirname(__file__)
    path = os.path.realpath(fpath + r'/../../examples/Astrodynamics/OrbitRaising/LowThrust.py')
    assert subprocess.call(['python', path]) == 0


@pytest.mark.parametrize("file", AtmosphericFlight)
def test_atmospheric_flight(file):
    fpath = os.path.dirname(__file__)
    path = os.path.realpath(fpath + r'/../../examples/AtmosphericFlight/' + file + '/' + file + '.py')
    assert subprocess.call(['python', path]) == 0

def test_hypersonic_fam():
    fpath = os.path.dirname(__file__)
    path = os.path.realpath(fpath + r'/../../examples/AtmosphericFlight/Hypersonic3DOF/hypersonic3DOFfamily.py')
    assert subprocess.call(['python', path]) == 0


@pytest.mark.parametrize("file", Classic)
def test_classic(file):
    fpath = os.path.dirname(__file__)
    path = os.path.realpath(fpath + r'/../../examples/Classic/' + file + '/' + file + '.py')
    assert subprocess.call(['python', path]) == 0


@pytest.mark.parametrize("file", ElectricityAndMagnetism)
def test_electricity_and_magnetism(file):
    fpath = os.path.dirname(__file__)
    path = os.path.realpath(fpath + r'/../../examples/ElectricityAndMagnetism/' + file + '/' + file + '.py')
    assert subprocess.call(['python', path]) == 0


@pytest.mark.parametrize("file", Oscillators)
def test_oscillators(file):
    fpath = os.path.dirname(__file__)
    path = os.path.realpath(fpath + r'/../../examples/Oscillators/' + file + '/' + file + '.py')
    assert subprocess.call(['python', path]) == 0
