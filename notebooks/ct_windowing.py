import numpy as np


def apply_ct_window(volume, center=500, width=3000):
    """
    Apply intensity windowing to a 3D CT volume.

    Parameters
    ----------
    volume : numpy.ndarray
        3D CT volume.
    center : float
        Window center.
    width : float
        Window width.

    Returns
    -------
    numpy.ndarray
        Windowed volume normalized to [0, 1].
    """

    lower = center - width / 2
    upper = center + width / 2

    windowed = np.clip(volume, lower, upper)
    windowed = (windowed - lower) / (upper - lower)

    return windowed
