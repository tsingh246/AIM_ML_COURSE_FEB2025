import os
from IPython.display import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import rcParams
import face_recognition


def load_images(known_images_dir):
    known_encodings = []
    known_images = []

    for file in os.listdir(known_images_dir):
        #fsdecode function decode the file into 
       # print(file)
        filename = os.fsdecode(file)
        #print(filename)
       # print(os.path.join(known_images_dir, filename))
        image = face_recognition.load_image_file(os.path.join(known_images_dir, filename))
        #print("image  ",image)

        enc = face_recognition.face_encodings(image)
       # print("enc   ",enc)
        if len(enc) > 0:
            known_encodings.append(enc[0])
            known_images.append(filename)

    return (known_encodings, known_images)


#print(load_images("C:\Learning\images\input"))




def calculate_face_distance(known_encodings, unknown_img_path, cutoff=0.5, num_results=4):
    image_to_test = face_recognition.load_image_file(unknown_img_path)
    #print(image_to_test)
    image_to_test_encoding = face_recognition.face_encodings(image_to_test)[0]

    face_distances = face_recognition.face_distance(known_encodings, image_to_test_encoding)
    
    return (unknown_img_path, known_images[face_distances.argmin()])

known_encodings, known_images = load_images("C:\Learning\images\input")
original_image = r"C:\Learning\images\req.jpg"
print("before")
Image(filename=original_image)
print("after")
matching_image = calculate_face_distance(known_encodings, original_image)
#%matplotlib inline
print("after",matching_image)
# read images
img_1 = mpimg.imread(original_image)
img_2 = mpimg.imread("C:\\Learning\\images\\input\\" + matching_image[1])

# display images
fig, ax = plt.subplots(1,2)
ax[0].imshow(img_1);
ax[1].imshow(img_2);

print('Hey, you look like ' + os.path.splitext(matching_image[1])[0] + '!')


