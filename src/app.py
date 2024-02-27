import os

import streamlit as st

from PIL import Image
from waifu2x import run


def upscale_image(input_img_path: str, output_img_path: str) -> None:
    """
    Upscales an image from the input_img_path and saves the upscaled
    image to the output_img_path.

    Parameters
    ----------
    input_img_path : str
        input image path string
    output_img_path : str
        output upscaled image path string
    """
    run(input_img_path, output_img_path)


def main():
    st.title("Image Upscaling Service")

    uploaded_files = st.file_uploader(
        "Choose images...", type=["jpg", "jpeg", "png"], accept_multiple_files=True
    )
    if uploaded_files:
        for uploaded_file in uploaded_files:
            temp_input_path = f"data/temp_{uploaded_file.name}"
            with open(temp_input_path, "wb") as f:
                f.write(uploaded_file.getvalue())

            output_img_path = f"data/{uploaded_file.name.split('.')[0]}_upscaled.png"
            upscale_image(temp_input_path, output_img_path)

            upscaled_image = Image.open(output_img_path)
            st.image(
                upscaled_image,
                caption=f"Upscaled Image: {uploaded_file.name}",
                use_column_width=True,
            )

            os.remove(temp_input_path)  # Clean up the temporary input file


if __name__ == "__main__":
    main()
