from ligotools import util
from ligotools import readligo as rl
import numpy as np
import matplotlib.mlab as mlab
from scipy.interpolate import interp1d

strain_H1, time_H1, chan_dict_H1 = rl.loaddata('data/H-H1_LOSC_4_V2-1126259446-32.hdf5', 'H1')


def test_util_whiten():
    fs = 4096    NFFT = 4*fs
    Pxx_H1, freqs = mlab.psd(strain_H1, Fs = fs, NFFT = NFFT)
    # We will use interpolations of the ASDs computed above for whitening:
    psd_H1 = interp1d(freqs, Pxx_H1)

    time = time_H1
    # the time sample interval (uniformly sampled!)
    dt = time[1] - time[0]
    result_whiten = util.whiten(strain, psd_H1, dt)
    assert result_whiten is not None

def test_util_wav():
    assert util.reqshift(strain_H1,fshift=100,sample_rate=4096) is not None