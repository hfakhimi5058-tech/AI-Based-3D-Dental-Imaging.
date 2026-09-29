import numpy as np


def get_volume_statistics(volume):
    """
    Calculate basic intensity statistics for a 3D CT volume.

    Parameters
    ----------
    volume : numpy.ndarray
        3D CT volume.

    Returns
    -------
    dict
        Basic intensity statistics.
    """

    return {
        "shape": volume.shape,
        "min": float(np.min(volume)),
        "max": float(np.max(volume)),
        "mean": float(np.mean(volume)),
        "median": float(np.median(volume)),
    }


def get_physical_size(image):
    """
    Calculate the physical dimensions of a medical image.

    Parameters
    ----------
    image : SimpleITK.Image
        Medical image.

    Returns
    -------
    numpy.ndarray
        Physical dimensions in millimeters.
    """

    size = np.array(image.GetSize())
    spacing = np.array(image.GetSpacing())

    return size * spacing
