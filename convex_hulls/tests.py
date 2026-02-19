import time
from generator import Generator

class EmpiricalBoth:
    def __init__(self):
        self.gen = Generator()

    def test_3(self, algo1, algo2):
        points = self.gen.generate(3)
        plane = []
        for p in points:
            plane.append(p.copy())
        start = time.perf_counter()
        algo1(plane)
        end = time.perf_counter()
        print(f"{algo1.__name__} n=3: {end-start}")

        # Test 2
        plane = []
        for p in points:
            plane.append(p.copy())

        start = time.perf_counter()
        algo2(plane)
        end = time.perf_counter()
        print(f"{algo2.__name__} n=3: {end-start}")

    def test_5(self, algo1, algo2):
        points = self.gen.generate(5)
        plane = []
        for p in points:
            plane.append(p.copy())
        start = time.perf_counter()
        end = time.perf_counter()
        print(f"{algo1.__name__} n=5: {end-start}")

        # Test 2
        plane = []
        for p in points:
            plane.append(p.copy())

        start = time.perf_counter()
        end = time.perf_counter()
        print(f"{algo2.__name__} n=5: {end-start}")

    def test_50(self, algo1, algo2):
        points = self.gen.generate(50)
        plane = []
        for p in points:
            plane.append(p.copy())
        start = time.perf_counter()
        algo1(plane)
        end = time.perf_counter()
        print(f"{algo1.__name__} n=50: {end-start}")

        # Test 2
        plane = []
        for p in points:
            plane.append(p.copy())

        start = time.perf_counter()
        algo2(plane)
        end = time.perf_counter()
        print(f"{algo2.__name__} n=50: {end-start}")

    def test_500(self, algo1, algo2):
        points = self.gen.generate(500)
        plane = []
        for p in points:
            plane.append(p.copy())
        start = time.perf_counter()
        algo1(plane)
        end = time.perf_counter()
        print(f"{algo1.__name__} n=500: {end-start}")

        # Test 2
        plane = []
        for p in points:
            plane.append(p.copy())

        start = time.perf_counter()
        algo2(plane)
        end = time.perf_counter()
        print(f"{algo2.__name__} n=500: {end-start}")

    def test_5k(self, algo1, algo2):
        points = self.gen.generate(5000)
        plane = []
        for p in points:
            plane.append(p.copy())
        start = time.perf_counter()
        algo1(plane)
        end = time.perf_counter()
        print(f"{algo1.__name__} n=5k: {end-start}")

        # Test 2
        plane = []
        for p in points:
            plane.append(p.copy())

        start = time.perf_counter()
        algo2(plane)
        end = time.perf_counter()
        print(f"{algo2.__name__} n=5k: {end-start}")

    def test_50k(self, algo1, algo2):
        points = self.gen.generate(50000)
        plane = []
        for p in points:
            plane.append(p.copy())
        start = time.perf_counter()
        algo1(plane)
        end = time.perf_counter()
        print(f"{algo1.__name__} n=50k: {end-start}")

        # Test 2
        plane = []
        for p in points:
            plane.append(p.copy())

        start = time.perf_counter()
        algo2(plane)
        end = time.perf_counter()
        print(f"{algo2.__name__} n=50k: {end-start}")

    def test_500k(self, algo1, algo2):
        points = self.gen.generate(500000)
        plane = []
        for p in points:
            plane.append(p.copy())
        start = time.perf_counter()
        algo1(plane)
        end = time.perf_counter()
        print(f"{algo1.__name__} n=500k: {end-start}")

        # Test 2
        plane = []
        for p in points:
            plane.append(p.copy())

        start = time.perf_counter()
        algo2(plane)
        end = time.perf_counter()
        print(f"{algo2.__name__} n=500k: {end-start}")

    def test_1m(self, algo1, algo2):
        points = self.gen.generate(1000000)
        plane = []
        for p in points:
            plane.append(p.copy())
        start = time.perf_counter()
        algo1(plane)
        end = time.perf_counter()
        print(f"{algo1.__name__} n=1M: {end-start}")

        # Test 2
        plane = []
        for p in points:
            plane.append(p.copy())

        start = time.perf_counter()
        algo2(plane)
        end = time.perf_counter()
        print(f"{algo2.__name__} n=1M: {end-start}")

    def test_2m(self, algo1, algo2):
        points = self.gen.generate(2000000)
        plane = []
        for p in points:
            plane.append(p.copy())
        start = time.perf_counter()
        algo1(plane)
        end = time.perf_counter()
        print(f"{algo1.__name__} n=2M: {end-start}")

        # Test 2
        plane = []
        for p in points:
            plane.append(p.copy())

        start = time.perf_counter()
        algo2(plane)
        end = time.perf_counter()
        print(f"{algo2.__name__} n=2M: {end-start}")

    def test_3m(self, algo1, algo2):
        points = self.gen.generate(3000000)
        plane = []
        for p in points:
            plane.append(p.copy())
        start = time.perf_counter()
        algo1(plane)
        end = time.perf_counter()
        print(f"{algo1.__name__} n=3M: {end-start}")

        # Test 2
        plane = []
        for p in points:
            plane.append(p.copy())

        start = time.perf_counter()
        algo2(plane)
        end = time.perf_counter()
        print(f"{algo2.__name__} n=3M: {end-start}")

    def test_4m(self, algo1, algo2):
        points = self.gen.generate(4000000)
        plane = []
        for p in points:
            plane.append(p.copy())
        start = time.perf_counter()
        algo1(plane)
        end = time.perf_counter()
        print(f"{algo1.__name__} n=4M: {end-start}")

        # Test 2
        plane = []
        for p in points:
            plane.append(p.copy())

        start = time.perf_counter()
        algo2(plane)
        end = time.perf_counter()
        print(f"{algo2.__name__} n=4M: {end-start}")

    def test_5m(self, algo1, algo2):
        points = self.gen.generate(5000000)
        plane = []
        for p in points:
            plane.append(p.copy())
        start = time.perf_counter()
        algo1(plane)
        end = time.perf_counter()
        print(f"{algo1.__name__} n=5M: {end-start}")

        # Test 2
        plane = []
        for p in points:
            plane.append(p.copy())

        start = time.perf_counter()
        algo2(plane)
        end = time.perf_counter()
        print(f"{algo2.__name__} n=5M: {end-start}")

    def test_6m(self, algo1, algo2):
        points = self.gen.generate(6000000)
        plane = []
        for p in points:
            plane.append(p.copy())
        start = time.perf_counter()
        algo1(plane)
        end = time.perf_counter()
        print(f"{algo1.__name__} n=6M: {end-start}")

        # Test 2
        plane = []
        for p in points:
            plane.append(p.copy())

        start = time.perf_counter()
        algo2(plane)
        end = time.perf_counter()
        print(f"{algo2.__name__} n=6M: {end-start}")

    def test_7m(self, algo1, algo2):
        points = self.gen.generate(7000000)
        plane = []
        for p in points:
            plane.append(p.copy())
        start = time.perf_counter()
        algo1(plane)
        end = time.perf_counter()
        print(f"{algo1.__name__} n=7M: {end-start}")

        # Test 2
        plane = []
        for p in points:
            plane.append(p.copy())

        start = time.perf_counter()
        algo2(plane)
        end = time.perf_counter()
        print(f"{algo2.__name__} n=7M: {end-start}")

    def test_8m(self, algo1, algo2):
        points = self.gen.generate(8_000_000)
        plane = []
        for p in points:
            plane.append(p.copy())
        start = time.perf_counter()
        algo1(plane)
        end = time.perf_counter()
        print(f"{algo1.__name__} n=8M: {end-start}")

        # Test 2
        plane = []
        for p in points:
            plane.append(p.copy())

        start = time.perf_counter()
        algo2(plane)
        end = time.perf_counter()
        print(f"{algo2.__name__} n=8M: {end-start}")

    
    def test_9m(self, algo1, algo2):
        points = self.gen.generate(9000000)
        plane = []
        for p in points:
            plane.append(p.copy())
        start = time.perf_counter()
        algo1(plane)
        end = time.perf_counter()
        print(f"{algo1.__name__} n=9M: {end-start}")

        # Test 2
        plane = []
        for p in points:
            plane.append(p.copy())

        start = time.perf_counter()
        algo2(plane)
        end = time.perf_counter()
        print(f"{algo2.__name__} n=9M: {end-start}")

    def test_10m(self, algo1, algo2):
        points = self.gen.generate(10_000_000)
        plane = []
        for p in points:
            plane.append(p.copy())
        start = time.perf_counter()
        algo1(plane)
        end = time.perf_counter()
        print(f"{algo1.__name__} n=10M: {end-start}")

        # Test 2
        plane = []
        for p in points:
            plane.append(p.copy())

        start = time.perf_counter()
        algo2(plane)
        end = time.perf_counter()
        print(f"{algo2.__name__} n=10M: {end-start}")

    #def test_50m(self, algo1, algo2):
    #    points = self.gen.generate(50000000)
    #    plane = []
    #    for p in points:
    #        plane.append(p.copy())
    #    start = time.perf_counter()
    #    algo1(plane)
    #    end = time.perf_counter()
    #    print(f"{algo1.__name__} n=50M: {end-start}")

    #    # Test 2
    #    plane = []
    #    for p in points:
    #        plane.append(p.copy())

    #    start = time.perf_counter()
    #    algo2(plane)
    #    end = time.perf_counter()
    #    print(f"{algo2.__name__} n=50M: {end-start}")

    #def test_500m(self, algo1, algo2):
    #    points = self.gen.generate(500000000)
    #    plane = []
    #    for p in points:
    #        plane.append(p.copy())
    #    start = time.perf_counter()
    #    algo1(plane)
    #    end = time.perf_counter()
    #    print(f"{algo1.__name__} n=500M: {end-start}")

    #    # Test 2
    #    plane = []
    #    for p in points:
    #        plane.append(p.copy())

    #    start = time.perf_counter()
    #    algo2(plane)
    #    end = time.perf_counter()
    #    print(f"{algo2.__name__} n=500M: {end-start}")

    #def test_5b(self, algo1, algo2):
    #    points = self.gen.generate(5000000000)
    #    plane = []
    #    for p in points:
    #        plane.append(p.copy())
    #    start = time.perf_counter()
    #    algo1(plane)
    #    end = time.perf_counter()
    #    print(f"{algo1.__name__} n=5B: {end-start}")

    #    # Test 2
    #    plane = []
    #    for p in points:
    #        plane.append(p.copy())

    #    start = time.perf_counter()
    #    algo2(plane)
    #    end = time.perf_counter()
    #    print(f"{algo2.__name__} n=5B: {end-start}")
