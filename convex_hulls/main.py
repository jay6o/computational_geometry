import gc
from graham_scan import graham_scan
from monotone_chain import monotone_chain
from tests import EmpiricalBoth

if __name__ == "__main__":
    
    test = EmpiricalBoth()
    methods = dir(test)
    for i in methods:
        if i[0:5] == "test_":
            curr_test = getattr(test, i)
            curr_test(graham_scan, monotone_chain)
            gc.collect()
