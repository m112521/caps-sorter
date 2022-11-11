# caps-sorter

TBD:

- [ ] electronics/wiring
- [ ] 3D models, assembly
- [ ] final device photo 
- [ ] video of working device


Steps to reproduce:

1. Unzip saved model:

```bash
!unzip converted_savedmodel.zip
```


2. Convert to TFlite:
```python
import tensorflow as tf

# Convert the model
converter = tf.lite.TFLiteConverter.from_saved_model('model.savedmodel') # path to the SavedModel directory
tflite_model = converter.convert()

# Save the model.
with open('model.tflite', 'wb') as f:
    f.write(tflite_model)
```


3. TF LIte Interpreter:

```bash
cat /etc/os-release
python3
pip3 install --extra-index-url https://google-coral.github.io/py-repo/ tflite_runtime
[ERROR. Try next line] sudo pip3 install --extra-index-url https://google-coral.github.io/py-repo/ tflite_runtime
pip3 install https://github.com/google-coral/pycoral/releases/download/release-frogfish/tflite_runtime-2.5.0-cp37-cp37m-linux_armv7l.whl

```


4. Install OpenCV on RaspberryPi (Raspbian Buster) - could be outdated:

```bash
sudo apt-get update
sudo apt-get upgrade

# or

sudo apt update
sudo apt-get upgrade

<reboot>
sudo apt-get install build-essential cmake pkg-config
sudo apt-get install libavcodec-dev libavformat-dev
sudo apt-get install libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
sudo apt-get install libfontconfig1-dev libcairo2-dev
sudo apt-get install libgdk-pixbuf2.0-dev libpango1.0-dev
sudo apt-get install libgtk2.0-dev libgtk-3-dev
sudo apt-get install libatlas-base-dev gfortran
sudo apt-get install libhdf5-dev libhdf5-serial-dev libhdf5-103
sudo apt-get install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5

# <version==4.4.0.46>
sudo pip3 install opencv-contrib-python   
	
if numpy error:
  sudo pip3 install -U numpy
```


5. Run TFLite model (tflite_image.py, tflite_servo.py).
