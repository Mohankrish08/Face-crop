# Face-crop

The Face Crop Tool is a Python-based repository designed to extract facial regions from images. This tool automates the process of detecting and cropping faces within a given image dataset.

## Features
- **Automated Face Detection**: Utilizes state-of-the-art facial detection algorithms to locate faces within images.
- **Precise Cropping**: Extracts facial regions with accuracy, preserving the essential facial features.
- **Batch Processing**: Capable of handling large image datasets, streamlining the extraction process.
- **Output Folder Creation**: Generates an organized output folder containing cropped facial images.

![](assets/Face-crop.png)

## Installation 

1. Git clone this repo 
```bash
git clone https://github.com/Mohankrish08/Face-crop.git
```
2. Install the dependencies
```bash
pip install -r requirements.txt
```

## How to Run

1. Place images in the designated input folder.
2. Execute the tool, specifying the input folder path.
3. Obtain cropped facial images in the output folder.

Inference this model

```bash
python main.py --folder <input folder> --weight <weights> --output_folder <name of the output folder>
```
