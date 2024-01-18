from csg_config import config
from csg_utils import *
from csg_const import *

class Req():
    def __init__(self, cycle:int=None, addr:int=None, core:int=None, driver:Driver=None, inst:Inst=None) -> None:
        # cycle addr core driver inst
        self.cycle = cycle
        self.addr = addr
        self.core = core
        self.driver = driver
        self.inst = inst

class Generator():
    def  __init__(self) -> None:
        self.drivers = [Driver.icache, Driver.dcache]
        self.supports = [[Inst.LOAD], [Inst.LOAD, Inst.STORE, Inst.STORE_ALL]]

    def full_ramdom(self):
        reqs = []
        for cycle in range(config.init_cycles, config.run_cycles):
            for core in range(0, config.cores):
                for i, driver in enumerate(self.drivers):
                    for inst in self.supports[i]:
                        req = Req(cycle, gen_random_addr(), core, driver, inst)
                        reqs.append(req)
        return reqs