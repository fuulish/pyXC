#!/usr/bin/env python

import pyxc
from pyxc import XC
from cube import Cube

Exc_ref = -4.22993799824178
Eh_ref = 18.42001204556387

edens = Cube('PBE-ELECTRON_DENSITY-1_0.cube')
tdens = Cube('PBE-TOTAL_DENSITY-1_0.cube')
hpot = Cube('PBE-v_hartree-1_0.cube')

Eh = (hpot.data * tdens.data).sum() * tdens.dV/2.
xc = XC(edens, func_id=[101, 130])
exc = xc.exc
exc = exc.reshape(edens.data.shape)

Exc = (exc * edens.data).sum() * edens.dV

print Exc_ref, Exc
print Eh_ref, Eh
