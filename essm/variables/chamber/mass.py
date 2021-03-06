"""Chamber mass and energy balance."""

from __future__ import absolute_import

from sage.symbolic.units import units

from .._core import Variable

# Used units
kelvin = units.temperature.kelvin
meter = units.length.meter
mole = units.amount_of_substance.mole
pascal = units.pressure.pascal
second = units.time.second
watt = units.power.watt


class W_c(Variable):
    """Chamber width"""

    unit = meter


class L_c(Variable):
    """Chamber length"""

    unit = meter


class H_c(Variable):
    """Chamber height"""

    unit = meter


class V_c(Variable):
    """Chamber volume"""

    unit = meter**3


class n_c(Variable):
    """molar mass of gas in chamber"""

    unit = mole


class F_in_v(Variable):
    """Volumetric flow rate into chamber"""

    unit = meter**3 / second
    latex_name = 'F_{in,v}'


class F_in_mola(Variable):
    """Molar flow rate of dry air into chamber"""

    unit = mole / second
    latex_name = 'F_{in,mol,a}'


class F_in_molw(Variable):
    """Molar flow rate of water vapour into chamber"""

    unit = mole / second
    latex_name = 'F_{in,mol,w}'


class F_out_mola(Variable):
    """Molar flow rate of dry air out of chamber"""

    unit = mole / second
    latex_name = 'F_{out,mol,a}'


class F_out_molw(Variable):
    """Molar flow rate of water vapour out of chamber"""

    unit = mole / second
    latex_name = 'F_{out,mol,w}'


class F_out_v(Variable):
    """Volumetric flow rate out of chamber"""

    unit = meter**3 / second
    latex_name = 'F_{out,v}'


class T_d(Variable):
    """Dew point temperature of incoming air"""

    unit = kelvin


class T_in(Variable):
    """Temperature of incoming air"""

    unit = kelvin
    latex_name = 'T_{in}'


class T_out(Variable):
    """Temperature of outgoing air (= chamber T_a)"""

    unit = kelvin
    latex_name = 'T_{out}'


class T_room(Variable):
    """Lab air temperature"""

    unit = kelvin
    latex_name = 'T_{room}'


class P_w_in(Variable):
    """Vapour pressure of incoming air"""

    unit = pascal
    latex_name = 'P_{w,in}'


class P_w_out(Variable):
    """Vapour pressure of outgoing air"""

    unit = pascal
    latex_name = 'P_{w,out}'


class R_H_in(Variable):
    """Relative humidity of incoming air"""

    unit = 1 / 1
    latex_name = 'R_{H,in}'


class L_A(Variable):
    """Leaf area"""

    unit = meter**2


__all__ = (
    'W_c', 'L_c', 'H_c', 'V_c', 'n_c', 'F_in_v', 'F_in_mola', 'F_in_molw',
    'F_out_mola', 'F_out_molw', 'F_out_v', 'T_d', 'T_in', 'T_out', 'T_room',
    'P_w_in', 'P_w_out', 'R_H_in', 'L_A', )
