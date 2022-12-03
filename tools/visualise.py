import numpy as np

import collections
import csv
import cv2
import os

from pathlib import Path
from io import TextIOWrapper


def visualise_SN(file: str):
    """
    Visualising soccer-net single video with or without tracking boxes

    Parameters
    ----------
    file - path to a parent file with video's parameters
    
    Returns
    -------
    None.

    """
    file = Path(file)
    
    # lists storing images paths and annotation files paths
    images_paths = []
    annotation_files = []
    
    # paths for det (annotation files)
    for dirpath, _, filenames in os.walk(file):
        for f in [os.path.join(dirpath, file) for file in filenames]:
            if "det\det.txt" in f:
                annotation_files.append(f)
       
    # initiate dictionary containing tracking frames for each image
    image_annotations = collections.defaultdict(list)

    # filling dictionary with image path names and box coordinates
    for af in annotation_files:
        st1, st2, sample, _, _ = af.split("\\")[-5:]
        imgpath = "%s\\%s\\%s\\img1\\%06d.jpg"
        with open(af, newline = "") as csvfile:
            csv_reader = csv.reader(csvfile, delimiter = ",")
            for row in csv_reader:
                frame, _, x, y, w, h = [int(x) for x in row[:6]] 
                ifn = imgpath%(st1, st2, sample, frame)
                ifnpath = os.path.join(file, "\\".join([i for i in ifn.split("\\") if i not in str(file).split("\\")]))
                image_annotations[ifnpath].append((x,y,w,h))
                
    # showing images with boxes
    for img_path in image_annotations.keys():
        f = open(Path(img_path), "rb")
        f = f.read()
        image = np.asarray(bytearray(f))
        image = cv2.imdecode(image, 1)
        for box in image_annotations[img_path]:
            x, y, w, h = box
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
        image = cv2.resize(image, (960, 540))
        cv2.imshow("output", image)
        cv2.waitKey(50)
