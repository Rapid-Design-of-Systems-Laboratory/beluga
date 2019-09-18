import pytest
import subprocess
import os

AscentVehicles = [r'BFR', r'GoddardRocket', r'Titan-II-SSTO']
AtmosphericFlight = [r'HangGlider', r'HypersonicNose']

@pytest.mark.parametrize("file", AscentVehicles)
def test_AscentVehicles(file):
    fpath = os.path.dirname(__file__)
    path = os.path.realpath(fpath + r'/../../examples/AscentVehicles/' + file + '/' + file + '.py')
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
