# **ImageCrypt: Portable Stenography**

## **Table of Contents**

- [**ImageCrypt: Portable Stenography**](#imagecrypt-portable-stenography)
  - [**Table of Contents**](#table-of-contents)
  - [**Overview**](#overview)
  - [**Features**](#features)
  - [**Installation**](#installation)
    - [**Pre-built executable file**](#pre-built-executable-file)
  - [**Usage**](#usage)
    - [**Encode a Message**](#encode-a-message)
    - [**Decode a Message**](#decode-a-message)
  - [**Project Structure**](#project-structure)
  - [**License**](#license)
  - [**Credits**](#credits)

## **Overview**

ImageCrypt is a lightweight stenography GUI app based on Python with a focus on hiding a passphrase on the imported image.

## **Features**

- **Encode Messages**: Hide text messages within image files
- **Decode Messages**: Retrieve hidden text messages from image files
- **Simple GUI**: User-friendly interface for ease of use

## **Installation**

### **Pre-built executable file**

1. Download the latest version of the executable from the [Releases](https://github.com/kagifret/imagecrypt/releases) page
2. Run the executable on your system

## **Usage**

### **Encode a Message**

1. Select "Encode" setting
2. Choose the image file where you want to hide the message
3. Enter your message and password in the provided text boxes
4. Save the new image with the hidden message

### **Decode a Message**

1. Select "Decode" from the main menu
2. Choose the image file with the hidden message
3. Enter the password used during the encoding process for deciphering
4. View the decoded message displayed

## **Project Structure**

Here’s an overview of the project’s directory structure:
```
imagecrypt/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── main.py              # Entry point
├── modules/             # Helper modules
│   ├── controller.py
│   ├── encryptionhandler.py
│   ├── gui.py
│   ├── imagehandler.py
│   └── stenography.py
```

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## **Credits**

- Developed by [Ilya](https://github.com/kagifret) and [Krishna](https://github.com/StygianSummer)
- This project was built using the following libraries:
  - [backports.tarfile](https://pypi.org/project/backports.tarfile/) - Backport of the `tarfile` module for Python 3.9 and earlier
  - [crayons](https://pypi.org/project/crayons/) - Colored string formatting for Python
  - [cryptography](https://pypi.org/project/cryptography/) - Cryptographic recipes and primitives
  - [importlib-metadata](https://pypi.org/project/importlib-metadata/) - Read metadata from Python packages
  - [importlib-resources](https://pypi.org/project/importlib-resources/) - Read resources from Python packages
  - [jaraco.text](https://pypi.org/project/jaraco.text/) - Utilities for text processing
  - [opencv-python](https://pypi.org/project/opencv-python/) - Python bindings for OpenCV
  - [piexif](https://pypi.org/project/piexif/) - EXIF metadata manipulation library
  - [Pillow](https://python-pillow.org/) - Python Imaging Library (PIL Fork)
  - [pip-chill](https://pypi.org/project/pip-chill/) - Freeze dependencies to create lightweight requirements files
  - [platformdirs](https://pypi.org/project/platformdirs/) - Platform-specific directories for caching, configuration, etc
  - [pyinstaller](https://pypi.org/project/pyinstaller/) - Bundles Python applications into stand-alone executables
  - [tomli](https://pypi.org/project/tomli/) - A Python library for parsing TOML files