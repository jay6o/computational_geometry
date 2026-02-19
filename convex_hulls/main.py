import gc
from graham_scan import graham_scan
from monotone_chain import monotone_chain
from tests import EmpiricalBoth

if __name__ == "__main__":
    
    test = EmpiricalBoth()
    methods = dir(test)
    for i in methods:
        for i in ["test_3", "test_5", "test_50", "test_500", "test_5k", "test_50k", "test_500k", "test_1m", "test_2m", "test_3m", "test_4m", "test_5m", "test_6m", "test_7m", "test_8m", "test_9m", "test_10m"]:
            curr_test = getattr(test, i)
            curr_test(graham_scan, monotone_chain)
            gc.collect()
