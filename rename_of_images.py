# -*- coding: utf-8 -*-
"""Rename of images.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fkOm1EMa0PyRxTESnDPFv3veygSgiBmp
"""

from google.colab import drive
drive.mount('/content/drive')

!pip install Pillow

"""# **Rename of images**"""

import os

def rename_images_in_directory(directory, new_name_prefix):
    for count, filename in enumerate(os.listdir(directory)):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.heic','.HEIC')):  # Change the file extension as needed
            new_name = f"{new_name_prefix}_{count + 1}.jpg"
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")

if __name__ == "__main__":
    directory = "/content/drive/MyDrive/Dataset/class1"  # Replace with the path to your image directory
    new_name_prefix = "cook_house_waste"  # Specify the new name prefix
    rename_images_in_directory(directory, new_name_prefix)
