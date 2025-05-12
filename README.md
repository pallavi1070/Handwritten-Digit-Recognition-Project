
# Handwritten Digit Recognition Project

## Introduction

This is a Handwritten Digit Recognition Project developed using Python and a Convolutional Neural Network (CNN) model. It provides an interactive graphical interface for users to draw digits, and it predicts the drawn digit in real-time using a pre-trained CNN model.

## Features

* Real-time digit recognition using a pre-trained CNN model.
* Interactive drawing interface using Pygame.
* Automatic image processing and prediction display.
* Easy-to-use graphical interface.

## How It Works

1. Users draw a digit on the screen using the mouse.
2. Once drawing is complete, the application processes the drawing as an image.
3. The image is resized, preprocessed, and passed to the CNN model.
4. The model predicts the digit, and the prediction is displayed on the screen.

## Prerequisites

* Python installed on your system.
* Required Python libraries: `pygame`, `keras`, `opencv-python`, and `numpy`.
* The pre-trained model file (`bestmodel.h5`) should be in the same directory.
* Font file (`FreeSansBold.ttf`) should be in the same directory.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/handwritten-digit-recognition.git
   cd handwritten-digit-recognition
   ```
2. Install the required libraries:

   ```bash
   pip install pygame keras opencv-python numpy
   ```

## Usage

* Run the application:

  ```bash
  python app.py
  ```
* Draw a digit using the mouse.
* The predicted digit will appear on the screen.
* Press 'n' to clear the screen and draw again.

## Error Handling

* If the drawing is incomplete or not clear, the model may not provide an accurate prediction.
* If the model file (`bestmodel.h5`) is missing, the application will not run.

## License

This project is licensed under the MIT License. Feel free to modify and use it as needed.

## Acknowledgements

* The pre-trained CNN model was built using Keras.
* Pygame for graphical interface.
* OpenCV for image processing.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

