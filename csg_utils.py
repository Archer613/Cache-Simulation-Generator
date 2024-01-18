from csg_config import config
import random

# shift right and shift left the same bits, which means zeroing out the lower 6 bits and keeping the higher bits intact
def reduce_offset(addr):
    return (addr >> config.data_bits) << config.data_bits

def gen_random_addr():
    addr = random.randint(0, config.addr_max)
    addr = reduce_offset(addr)
    return addr