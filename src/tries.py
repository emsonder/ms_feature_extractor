
import numpy, operator
from scipy import signal
from matplotlib import pyplot as plt
from pyteomics import mzxml
import time
from src import ms_operator, matlab_caller

spectra = list(
    mzxml.read('/Users/andreidm/ETH/projects/ms_feature_extractor/data/CsI_NaI_best_conc_mzXML/CsI_NaI_neg_08.mzXML'))

mid_spectrum = spectra[43]  # nice point on chromatogram

peaks = matlab_caller.call_peak_picking(scriptpath='/Users/andreidm/ETH/projects/fiaminer_peak_picking.m',
                                        filepath='/Users/andreidm/ETH/projects/ms_feature_extractor/data/CsI_NaI_best_conc_mzXML/CsI_NaI_neg_08.mzXML')

mz_values = [peak[0] for peak in peaks]
intensities = [peak[1] for peak in peaks]

plt.plot(mid_spectrum['m/z array'], mid_spectrum['intensity array'], lw=1)
plt.plot(mz_values, intensities, 'rx', lw=1)

plt.show()


