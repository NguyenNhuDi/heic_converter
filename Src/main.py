from PIL import Image
import pyheif
from glob import glob
import os

def cvt_to_jpg(heic_file, output_file, output_format="JPEG"):
    # Decode HEIC file
    heif_file = pyheif.read(heic_file)

    # Convert to a Pillow Image
    image = Image.frombytes(
        heif_file.mode, 
        heif_file.size, 
        heif_file.data, 
        "raw", 
        heif_file.mode, 
        heif_file.stride,
    )

    # Save in the desired format (JPEG or PNG)
    image.save(output_file, format=output_format)


def main():
    main_dir = '/'.join(os.path.abspath(__file__).split('/')[:-2])

    in_dir = f'{main_dir}/Input'
    out_dir = f'{main_dir}/Output'


    images = glob(f'{in_dir}/*.heic')

    for f in images:
        name = os.path.basename(f)
        cvt_to_jpg(f,f'{out_dir}/{name}.jpg')

    # h_files = glob(f'{}')

if __name__ == '__main__':
    main()