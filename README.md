# OpenCV Workshop

A comprehensive workshop on computer vision using OpenCV and Convolutional Neural Networks (CNNs) for emotion detection.

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/cheetahraghav/opencv_worshop.git
   cd opencv_worshop
   ```

2. Environment setup (Optional):
   ```
   # Create and activate a virtual environment
   python -m venv cv_env
   
   # On Windows
   cv_env\Scripts\activate
   
   # On macOS/Linux
   source cv_env/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Workshop Content

### Module 1: OpenCV Basics

This module covers the fundamentals of computer vision with OpenCV:

- **Image Reading and Display**: Learn how to load images from disk and visualize them using OpenCV functions
- **Video Capture**: Techniques for capturing and processing video streams from webcams or video files
- **Basic Image Processing**: Master essential operations including:
  - Resizing and scaling
  - Image cropping
  - Color space conversions (RGB, BGR, HSV, Grayscale)
  - Drawing on images (lines, rectangles, circles)
  - Image filtering and transformations

### Module 2: Emotion Detection with CNN

This advanced module explores emotion detection using Convolutional Neural Networks:

- **Dataset Preparation**:
  - Working with facial expression datasets
  - Data preprocessing and augmentation
  - Train/validation/test splitting

- **CNN Architecture**:
  - Understanding CNN components (convolutional layers, pooling, fully connected layers)
  - Model design considerations for emotion recognition
  - Implementation using modern frameworks

- **Training and Evaluation**:
  - Training procedures and hyperparameter tuning
  - Model evaluation metrics
  - Performance optimization techniques

- **Real-time Emotion Detection**:
  - Integrating the trained model with OpenCV
  - Processing video streams for facial detection
  - Real-time emotion classification and visualization

## Additional Resources

- [CNN Visualization Tool](https://adamharley.com/nn_vis/cnn/2d.html) - Interactive visualization of CNNs
- [CNN Introduction](https://gamma.app/docs/Copy-of-Introduction-to-Convolutional-Neural-Networks-h4bzbh2auk496jw?mode=doc) - Comprehensive guide to CNN concepts

## Requirements

- Python 3.6+
- OpenCV
- NumPy

