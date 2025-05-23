# -*- coding: utf-8 -*-
"""image-augmentation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GA2e84tzYnvGqY92x7tEdkrWyhCXcww0
"""

from matplotlib import pyplot as plt
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator,load_img,img_to_array

img_path='/content/drive/MyDrive/lion-elephant-classification (1)/testing (1)/cat/images (1).jpg'
img=load_img(img_path)

img_array=img_to_array(img)

img_array=img_array.reshape((1,)+img_array.shape)

datagen=ImageDataGenerator(rescale=1./255,
                           rotation_range=20,
                           width_shift_range=0.2,
                           height_shift_range=0.2,
                           shear_range=0.2,
                           zoom_range=0.2,
                           horizontal_flip=True,
                           fill_mode='nearest')

augmented_images=datagen.flow(img_array,batch_size=1)

def visualize_augmented_images(generator,num_images):
  fig,axes = plt.subplots(1, num_images, figsize=(20, 20))
  for i in range(num_images):
    batch=next(generator)
    aug_image=batch[0]
    axes[i].imshow(aug_image)

    axes[i].axis('off')
  plt.show()

visualize_augmented_images(augmented_images,10)

import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
img_path = '/content/drive/MyDrive/lion-elephant-classification (1)/testing (1)/cat/images (3).jpg'  # update path if needed
original_img = load_img(img_path, target_size=(224, 224))
img_array = img_to_array(original_img)
img_array = np.expand_dims(img_array, axis=0)
datagen = ImageDataGenerator(horizontal_flip=True, fill_mode='nearest')
augmented_images = datagen.flow(img_array, batch_size=1)
augmented_img = next(augmented_images)[0].astype('uint8')
fig, axes = plt.subplots(2, 1, figsize=(4, 8))
axes[0].imshow(original_img)
axes[0].set_title("Original Image")
axes[0].axis('off')
axes[1].imshow(augmented_img)
axes[1].set_title("Augmented Image")
axes[1].axis('off')
plt.tight_layout()
plt.show()

