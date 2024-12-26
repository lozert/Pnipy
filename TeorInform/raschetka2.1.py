import numpy as np
from entropy import H, HNderM


n = 5

PXY = np.array([[n/260,       1/14,       1/14],
       [2/7 - n/240, 0,          2/7 - n/250],
       [n/240,       2/7-n/260,  n/250]])

PX = np.sum(PXY, axis=1)
PY = np.sum(PXY, axis=0)
print(f"PX = {PX}")
print(f"PY = {PY}\n")

print(f"H(PX) = {H(PX)}")
print(f"H(PY) = {H(PY)}")

PXderY = np.zeros((len(PX), len(PY)))
for j in range(len(PY)):
    for i in range(len(PX)):
        PXderY[i][j] = PXY[i][j]/PY[j]

print("\nP(X/Y)")
print(PXderY)

PYderX = np.zeros((len(PX), len(PY)))

for i in range(len(PX)):
    for j in range(len(PY)):
        PYderX[i][j] = PXY[i][j]/PX[i]

print("\nP(Y/X)=")
print(PYderX)

print(f"\nH(X/Y) = {HNderM(PXY, PXderY)}")
print(f"H(Y/X) = {HNderM(PXY, PYderX)}")


print(f"\nH(X/y1) = {H(PXderY.T[0])}")
print(f"H(X/y2) = {H(PXderY.T[1])}")

print(f"\nH(X; Y) = {HNderM(PXY, PXY)}")