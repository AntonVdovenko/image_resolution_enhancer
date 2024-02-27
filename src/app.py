import os

import streamlit as st

from PIL import Image
from waifu2x import run


def upscale_image(input_img_path: str, output_img_path: str):
    """
    Upscales an image from the input_img_path and saves the upscaled
    image to the output_img_path.

    Parameters:
    - input_img_path: The file path of the input image.
    - output_img_path: The file path where the upscaled image will be saved.
    """
    run(input_img_path, output_img_path)


def main():
    st.title("Image Upscaling Service")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # Save the uploaded image to a temporary file
        temp_input_path = "data/temp_input.png"
        with open(temp_input_path, "wb") as f:
            f.write(uploaded_file.getvalue())

        image = Image.open(uploaded_file)
        # Clean up the temporary input file
        os.remove(temp_input_path)
        st.image(image, caption="Original Image", use_column_width=True)

        if st.button("Upscale Image"):
            # Set a permanent output file path
            output_img_path = (
                "data/" + uploaded_file.name.split(".")[0] + "_upscaled.png"
            )

            upscale_image(temp_input_path, output_img_path)

            upscaled_image = Image.open(output_img_path)
            st.image(upscaled_image, caption="Upscaled Image", use_column_width=True)


if __name__ == "__main__":
    main()
main()
