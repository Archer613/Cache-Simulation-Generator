from csg_generator import Generator
import debugpy

if __name__ == '__main__':
    print('Hello, here is CacheStimulusGenerator(CSG)')
    
    # debug
    # debugpy.listen(5678)
    # debugpy.wait_for_client() 
    
    generator = Generator()

    reqs = generator.full_ramdom()
    
    for req in reqs:
        print(f"cycle[{req.cycle}] addr[{hex(req.addr)}] core[{req.core}] driver[{req.driver}] inst[{req.driver}]")
    
    
    