# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    Sel = 1100
    Inp12 = 10

   # input driving
    dut.sel.value = Sel
    dut.inp12.value = Inp12

    await Timer(2, units='ns')

    assert dut.out.value == Inp12, f"Mux result is incorrect: {dut.out.value} != 10"

