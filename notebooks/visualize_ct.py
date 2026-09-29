import matplotlib.pyplot as plt


def show_ct_slice(volume, slice_index=None, center=500, width=3000):
    """
    Display an axial slice from a 3D CT volume.

    Parameters
    ----------
    volume : numpy.ndarray
        3D CT volume.
    slice_index : int, optional
        Axial slice index. Defaults to the middle slice.
    center : float
        Window center.
    width : float
        Window width.
    """

    if slice_index is None:
        slice_index = volume.shape[0] // 2

    lower = center - width / 2
    upper = center + width / 2

    plt.figure(figsize=(8, 8))

    plt.imshow(
        volume[slice_index],
        cmap="gray",
        vmin=lower,
        vmax=upper
    )

    plt.title(f"CT Axial Slice — Z={slice_index}")
    plt.axis("off")
    plt.show()
