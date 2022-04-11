from decimal import Decimal, ROUND_HALF_UP
from math import ceil, floor

# usando decimal:
def round_well(num):
    return Decimal(num).quantize(0, ROUND_HALF_UP)

# usando math:
def otra_forma(n):
    if n - floor(n) < 0.5:
        return floor(n)
    else:
        return ceil(n)
