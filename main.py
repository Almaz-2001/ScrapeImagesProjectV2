import requests
import re
from bs4 import BeautifulSoup
import os
import urllib.request


def scrape_images(url):
    # Get the HTML content of the website
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the image tags in the HTML
    images = soup.find_all('img')

    # Create a folder to store the images
    if not os.path.exists('images'):
        os.makedirs('images')

    # Loop through the images and download each one
    for image in images:
        src = image.get('src')
        src = re.sub(r'\?.*', '', src)  # Remove any parameters from the URL
        filename = src.split('/')[-1]
        file_path = os.path.join('images', filename)

        # Check if the image is of a person wearing a particular fabric
        if 'person' in src and 'fabric' in src:
            # Save the image in the "person in a particular garment" folder
            if not os.path.exists('person_in_garment'):
                os.makedirs('person_in_garment')
            urllib.request.urlretrieve(src, os.path.join('person_in_garment', filename))
        elif 'fabric' in src:
            # Save the image in the "fabrics (not worn by the person)" folder
            if not os.path.exists('fabrics'):
                os.makedirs('fabrics')
            urllib.request.urlretrieve(src, os.path.join('fabrics', filename))


# Call the function to scrape the images
scrape_images(
    'https://www.ralphlauren.nl/en/men/clothing/hoodies-sweatshirts/10204?webcat=men%7Cclothing%7Cmen-clothing-hoodies-sweatshirts')

# Convert all the scrapped images into .jpg format
for folder_name in ['person_in_garment', 'fabrics']:
    for filename in os.listdir(folder_name):
        if filename.endswith('.png'):
            old_file_path = os.path.join(folder_name, filename)
            new_file_path = os.path.join(folder_name, filename[:-4] + '.jpg')
            os.rename(old_file_path, new_file_path)

