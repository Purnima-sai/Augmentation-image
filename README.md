# Image Augmentation

Image Augmentation is a toolkit designed to enhance your machine learning and computer vision pipelines by providing a collection of easy-to-use image transformation functions. These augmentations help improve the robustness and generalization of models by artificially expanding your dataset with realistic variations.

## Features

- **Basic Transformations**: Rotation, flipping, cropping, resizing, color jitter, and more.
- **Advanced Augmentations**: Random noise, blur, sharpening, cutout, elastic transformations, and more.
- **Custom Pipelines**: Easily compose multiple augmentations for complex workflows.
- **Configurable**: Fine-tune parameters for each augmentation to fit your dataset.
- **Plug & Play**: Integration with popular deep learning frameworks (e.g., PyTorch, TensorFlow).

## Installation

```bash
git clone https://github.com/<your-username>/image-augmentation.git
cd image-augmentation
pip install -r requirements.txt
```

## Usage

```python
from image_augmentation import augmentor

# Load your image
image = load_image('path/to/image.jpg')

# Apply augmentation
augmented_image = augmentor.random_flip(image)
augmented_image = augmentor.rotate(image, angle=30)
```

You can also build a pipeline:

```python
pipeline = augmentor.Compose([
    augmentor.RandomFlip(),
    augmentor.Rotate(angle_range=(-15, 15)),
    augmentor.ColorJitter(brightness=0.2, contrast=0.2)
])

augmented_image = pipeline(image)
```

## Supported Augmentations

- Random Flip (horizontal, vertical)
- Rotation
- Random Crop
- Resize
- Color Jitter (brightness, contrast, saturation, hue)
- Gaussian Blur
- Noise Injection
- Cutout
- Elastic Transform
- And more!

## Contributing

Contributions are welcome! Please open issues and submit pull requests for new augmentations, bug fixes, or documentation improvements.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/foo`)
3. Commit your changes (`git commit -am 'Add some foo'`)
4. Push to the branch (`git push origin feature/foo`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License.

## Acknowledgments

- Inspired by popular libraries like [imgaug](https://github.com/aleju/imgaug), [Albumentations](https://github.com/albumentations-team/albumentations), and [torchvision.transforms](https://pytorch.org/vision/stable/transforms.html).
