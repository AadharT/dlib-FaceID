# dlib-FaceID
Dlib face recognition implementation with automatic person registrations

## Installation

### Requirements

  * Python 3.3+ or Python 2.7
  * macOS or Linux

### Installation Options:

#### Installing on Mac or Linux

First, make sure you have dlib already installed with Python bindings:

  * [How to install dlib from source on macOS or Ubuntu](https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf)

Then, install this module from pypi using `pip3` (or `pip2` for Python 2):

```bash
pip install face_recognition
```

## Capturing new faces

Use capture.py, first enter the name of the person and press Spacebar to save pictures to recognize.
Make sure there is only once face in the frame while pressing Spacebar, press ESC to exit.

```bash
python capture.py
```
Changes still need to be made to this to change the file format of saved array from npy to HDF5

## Deploying

```bash
python recognize.py
```

## Demo

A standalone program that can be run by just saving two jpg images as person1 and person2 in same folder.

```bash
python faceidtest.py
```
