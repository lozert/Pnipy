import numpy as np
import time

start = time.time()
rnd = np.random.rand(150_000_000)
end = time.time()

print(f"Время генерации {end-start}")
print(len(rnd))