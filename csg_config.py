import os
import configparser
import math
import random
from typing import Optional

class Config:
    def __init__(self, config_path = None) -> None:
        if config_path != None: # for files in other path who wants to get configure
            os.environ['CUSTOM_CONFIG_PATH'] = config_path
            self.config_file = os.environ.get('CUSTOM_CONFIG_PATH')
        else:
            self.config_file = os.environ.get("CONFIG_FILE", "config.ini")
        
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file)

        # --------------------------- basic_info ----------------------------------- #
        self.cores                  = self.config.getint('basic_info', 'cores'  )
        self.addr_bits              = self.config.getint('basic_info', 'addr_bits')
        self.addr_max               = math.pow(2, self.addr_bits)-1
        self.data_bytes             = self.config.getint('basic_info', 'data_bytes')
        self.data_bits              = int(math.log2(self.data_bytes))

        # l1_d
        self.d_sets                 = self.config.getint('basic_info', 'd_sets')
        self.d_ways                 = self.config.getint('basic_info', 'd_ways')
        # l1_i
        self.i_has_coh              = self.config.getboolean('basic_info', 'i_has_coh')
        self.i_sets                 = self.config.getint('basic_info', 'i_sets')
        self.i_ways                 = self.config.getint('basic_info', 'i_ways')
        # l2
        self.l2_sets                = self.config.getint('basic_info', 'l2_sets')
        self.l2_ways                = self.config.getint('basic_info', 'l2_ways')
        self.l2_banks               = self.config.getint('basic_info', 'l2_banks')
        # l3
        self.l3_sets                = self.config.getint('basic_info', 'l3_sets')
        self.l3_ways                = self.config.getint('basic_info', 'l3_ways')
        self.l3_banks               = self.config.getint('basic_info', 'l3_banks')

        # --------------------------- gen_info ----------------------------------- #
        self.seed                   = self.config.getint('gen_info', 'seed')
        self.init_cycles            = self.config.getint('gen_info', 'init_cycles')
        self.run_cycles             = self.config.getint('gen_info', 'run_cycles')
        assert self.init_cycles < self.run_cycles
        self.mode                   = self.config.get('gen_info', 'mode')
        assert self.mode in ['full_random', 'sim_behavior', 'limit_parameters', 'coh_test'], f"Invalid mode => {self.mode}"

        # random seed init
        random.seed(self.seed)

config = Config()
