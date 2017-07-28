import numpy as np


def surface_area_exact(r1, r2):
    gamma = np.arccos(r2 / r1)
    return 2 * np.pi * (np.square(r1) + (np.square(r2) / np.sin(gamma)) * np.log(np.cos(gamma) / (1 - np.sin(gamma))))


def surface_area_approx(r1, r2):
    return 4 * np.pi * np.square((r1 + r2) / 2)


if __name__ == "__main__":
    print(surface_area_approx(6378.137, 6356.752), surface_area_exact(6378.137, 6356.752))


