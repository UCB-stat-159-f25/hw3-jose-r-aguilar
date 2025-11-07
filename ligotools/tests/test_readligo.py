from ligotools import readligo

def test_ligo_read():
    assert readligo.loaddata("data/H-H1_LOSC_4_V2-1126259446-32.hdf5", 'H1') is not None

def test_ligo_read_2():
    assert readligo.loaddata("data/L-L1_LOSC_4_V2-1126259446-32.hdf5", 'L1') is not None

