"""
-*- coding: utf-8 -*-
========================
Random raster image creation with color information side by side
========================
Contributor: Chirag Rathod (Srce Cde)
========================
"""

import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt


def generate_random_image(
    width: int, height: int, img_type: str = "G"
) -> npt.NDArray[np.uint8]:
    """
    width: width of the image to be generted
    height: height of the image to be generted
    img_type: "G" (Default) or "C" - G stands for grayscale | C stands for color (RGB)
    """
    if img_type not in ["G", "C"]:
        raise Exception("Invalid value for image type!")
    if img_type == "G":
        return np.random.randint(
            low=0, high=256, size=(height, width, 1), dtype=np.uint8
        )
    if img_type == "C":
        return np.random.randint(
            low=0, high=256, size=(height, width, 3), dtype=np.uint8
        )


def plot_image_side_by_side(image: npt.NDArray[np.uint8]) -> None:
    plt.subplot(1, 2, 1)
    if image.shape[-1] == 1:
        plt.imshow(image, cmap="gray", vmin=0, vmax=255)
    else:
        plt.imshow(image)
    plt.axis("off")

    plt.subplot(1, 2, 2)
    if image.shape[-1] == 1:
        plt.imshow(image, cmap="gray", vmin=0, vmax=255)
    else:
        plt.imshow(image)

    for x in range(0, image.shape[1]):
        for y in range(0, image.shape[0]):
            intensity = image[y, x]
            if image.shape[-1] == 1:
                plt.text(
                    x,
                    y,
                    str(intensity[0]),
                    color="green",
                    fontsize=8,
                    fontweight=1000,
                    ha="center",
                    va="center",
                )
            else:
                plt.text(
                    x,
                    y,
                    f"{str(intensity[0])}\n{str(intensity[1])}\n{str(intensity[2])}",
                    color="black",
                    fontsize=8,
                    fontweight=1000,
                    ha="center",
                    va="center",
                )
    plt.axis("off")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    r_image = generate_random_image(8, 8, img_type="C")
    plot_image_side_by_side(r_image)

    r_image = generate_random_image(8, 8, img_type="G")
    plot_image_side_by_side(r_image)
