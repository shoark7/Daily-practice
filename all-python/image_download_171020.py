"""Downaload image from a given url

    This project can be practical with some purposes.
    image_downlaod function downloads image from a given url.
    Later, I'll make a function that accepts html input to download images in it.
    Then this functino would be useful for that purpose.

    It uses requests and PIL module, which are both famous for http requests and image processing.
    Also, io and os modules are used. Check how this got used.

    Start Date: 2017/10/20
    End Date  : 2017/10/20
"""

from io import BytesIO
import os
from PIL import Image
import requests


def image_download(url, name=None, download_path='.'):
    """Download a image from a given url

        URL must be provided.
        Extension of image file in url will be used but name of it can be given.
        Download path is current directory by default, but can be given.

        ----------------------------------------------------------------
        :input:
            url: MUST. If the image of that url doesn't exist, error occurs.
            name: Original image name will be used. But can be customized with what you want.
            download_path: Current directory by default. Can be modified.
        :result:
            None. Whether downloaded successfuly or not, messages are printed.
    """

    if not os.path.exists(download_path):
        raise OSError("Given path doesn't exist")

    _, file_name = os.path.split(url)
    name_prefix, ext = os.path.splitext(file_name)

    if name:
        name_prefix = name

    image_bytes = requests.get(url).content
    image = Image.open(BytesIO(image_bytes))  # Image.open needs a file-like object

    final_file_name = download_path + '/' + name_prefix + ext

    if os.path.exists(final_file_name):  # Maybe there might be a file with the same name we want
        raise OSError('***', final_file_name, "Already exists ***")

    try:
        image.save(final_file_name)
    except:
        raise OSError("I don't know why this happens...")
    else:
        print(final_file_name, "has been downloaded successfully")
    finally:
        image.close()


if __name__ == '__main__':
    image_download('http://www.desicomments.com/wp-content/uploads/2017/07/Awesome-Picture.jpg',
                   name='funkyboy',
                   download_path='/home/sunghwanpark')
