import time

bils = [-8038.51083012] * 500_000_000
start = time.perf_counter()
for i in bils:
    sum = i + 1481.840124
end = time.perf_counter()

print(f"{end-start}")
