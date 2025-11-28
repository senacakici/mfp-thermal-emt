import numpy as np

def k_series(k_fibre, k_air, porosity):
    """
    Series model (lower bound).
    1/k_eff = (1-ε)/k_fibre + ε/k_air
    """
    eps = porosity
    return 1 / ((1 - eps) / k_fibre + eps / k_air)


def k_parallel(k_fibre, k_air, porosity):
    """
    Parallel model (upper bound).
    k_eff = (1-ε)*k_fibre + ε*k_air
    """
    eps = porosity
    return (1 - eps) * k_fibre + eps * k_air


def k_geometric(k_fibre, k_air, porosity):
    """
    Geometric-mean EMT model.
    k_eff = k_fibre^(1-ε) * k_air^ε
    """
    eps = porosity
    return (k_fibre ** (1 - eps)) * (k_air ** eps)


def keff_with_barrier(k_core, L_core, k_barrier, L_barrier):
    """
    1D through-thickness model with a core layer + polymer barrier in series.

    R_total = L_core/k_core + L_barrier/k_barrier
    k_eff = (L_core + L_barrier) / R_total
    """
    R_core = L_core / k_core
    R_barrier = L_barrier / k_barrier
    R_total = R_core + R_barrier
    L_total = L_core + L_barrier
    return L_total / R_total

