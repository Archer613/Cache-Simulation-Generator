from enum import Enum, unique, auto

class Inst(Enum):
    LOAD = 0
    STORE = 1
    STORE_ALL = 2 # overwrite block
    LOAD_RESP = 3
    STORE_RESP = 4

class Driver(Enum):
    icache = 0
    dcache = 1
    