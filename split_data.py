import argparse
import csv
import os

import numpy as np
from PIL import Image
from tqdm import tqdm


def save_csv(data, path, fieldnames=['id', 'gender', 'articleType', 'baseColour']):
    with open(path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(dict(zip(fieldnames, row)))


#if __name__ == '__main__':
 #   parser = argparse.ArgumentParser(description='Split data for the dataset')
 #   parser.add_argument('/home/vrushali/Image Reco/fashion-product-images-small', type=str, required=True, help="/home/vrushali/Image Reco/fashion-product-images-small")
  #  parser.add_argument('/home/vrushali/Image Reco', type=str, required=True, help="/home/vrushali/Image Reco")

  #  args = parser.parse_args()
def split_data():
    input_folder = "/home/vrushali/Image Reco/fashion-products"
    output_folder = "/home/vrushali/Image Reco"
    annotation = os.path.join(input_folder, 'style.csv')

    # open annotation file
    all_data = []
    with open(annotation) as csv_file:
        # parse it as CSV
        reader = csv.DictReader(csv_file)
        # tqdm shows pretty progress bar
        # each row in the CSV file corresponds to the image
        for row in tqdm(reader, total=reader.line_num):
            # we need image ID to build the path to the image file
            img_id = row['id']
            # we're going to use only 3 attributes
            gender = row['gender']
            articleType = row['articleType']
            baseColour = row['baseColour']
            img_name = os.path.join(input_folder, 'images', str(img_id) + '.jpg')
            # check if file is in place
            if os.path.exists(img_name):
                # check if the image has 80*60 pixels with 3 channels
                img = Image.open(img_name)
                if img.size == (1040, 1080) and img.mode == "RGB":
                    all_data.append([img_name, gender, articleType, baseColour])

    # set the seed of the random numbers generator, so we can reproduce the results later
    #np.random.seed(7)
    # construct a Numpy array from the list
    all_data = np.asarray(all_data)
    # Take 40000 samples in random order
    #inds = np.random.choice(25, 25, replace=False)
    # split the data into train/val and save them as csv files
    save_csv(all_data[24][: 25], os.path.join(output_folder, 'trainn.csv'))
    #save_csv(all_data[inds][20:25], os.path.join(output_folder, 'vall.csv'))
split_data()