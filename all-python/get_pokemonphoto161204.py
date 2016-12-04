"""
In Korea, there is a site called 'Namu wiki'(Namu is 'tree' in Korean) and it's a korean
 dedicated wikipedia.

https://namu.wiki/w/%ED%8F%AC%EC%BC%93%EB%AA%AC%EC%8A%A4%ED%84%B0/%EB%AA%A9%EB%A1%9D/1%EC%84%B8%EB%8C%80#fn-A

In this url, it contains a pokemon dictionary of generation 1 pokemons.
Now I think I have a project to use this dictionary to visualize them in my site.
First of all, I'll get all pokemons' photos for my fun.

It's my slump time and I need a chance to overcome it.
Anyway let's get started.

Start date = 2016/12/04
End date = 201?/??/??
"""

import requests
from bs4 import BeautifulSoup
import os
from io import BytesIO
from PIL import Image

# pokemon has 7 generation so you can choose what generation to use
FRONT_URL = 'https://namu.wiki/w/%ED%8F%AC%EC%BC%93%EB%AA%AC%EC%8A%A4%ED%84%B0/%EB%AA%A9%EB%A1%9D/'
AFTER_URL = '%EC%84%B8%EB%8C%80'

IMAGE_LOCATION = '/home/sunghwanpark/사진/pokemons'
# This is my local location so you can customize.


def get_pokemon_photos_from_namuwiki(generation=7, *, image_location=IMAGE_LOCATION):
    """
    Download pokemon photos of your wanted generation from Namuwiki.
    :param generation: pokemon generation from 1 to 7. You can choose.
    :param image_location: Location to save images. It must be a keyword argument.
    :return: Whether or not saving photos succeeded.
    """
    os.chdir(image_location)
    full_url = FRONT_URL + str(generation) + AFTER_URL
    html_text = requests.get(full_url).text
    soup = BeautifulSoup(html_text, 'html.parser')

    table_body = soup.find_all('table', class_='wiki-table')[1]
    # It has two wiki-table tables, and our need is second one.

    all_tr = table_body.find_all('tr')
    # print(all_tr)


    count = 0
    # image making process.
    for tr in all_tr[1:]: # First tr is a heading tr, so we don't need it.
        if tr.find(class_='wiki-fn-content'):
            continue

        # This image is a reworked pokemon image in generation 7.
        # But we need only generation 1 pokemon. So we skip this.

        image_url = "https:" + tr.find('img', class_='wiki-image').get('data-original')
        image_bytes = BytesIO(requests.get(image_url).content)
        # As you know, you should make image into BytesIO,
        # because Image.open method needs file-like objects with 'read' method.

        pokemon_image = Image.open(image_bytes)
        pokemon_image_format = pokemon_image.format
        pokemon_image_name   = tr('td')[2].p.string

        pokemon_image.save(pokemon_image_name, format=pokemon_image_format)
        # pokemon_image.show()
        # If you're a brave guy, you can open 151 pokemon images :)

        pokemon_image.close()
        image_bytes.close()

        count += 1
        print('{} / {} is finished'.format(count, 151))

get_pokemon_photos_from_namuwiki(generation=1)
