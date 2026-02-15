from generator import Generator
from graham_scan import graham_scan


if __name__ == "__main__":
    gen = Generator()
    plane1 = gen.generate(10000)

    # GRAHAM SCAN + EMPIRICAL ANALYSIS
    graham_scan(plane1)
    # ALGO2 + EMPIRICAL ANALYSIS
