# **Simple Pattern Recognition Script**

This is a simple wrapper script for OpenCV written in python. It can count the matched patterns in a larger image using OpenCV library's `TM_CCOEFF_NORMED` matching method. It also draws squares around the places that the pattern was detected. 

## 🔧 Dependencies

This script requires these python modules to be installed : `numpy, matplotlib, cv2, colorama`. you can install them via the commands given below:

``` bash
$ pip install numpy
$ pip install colorama
$ pip install numpy
$ pip install matplotlib
$ pip instal opencv-python
```

## ⚠️ Limitations

🟥 Keep in mind that even so this script can be used for any type of image, there is no guarantee that it'll work for nosiy or obscure photos. Best results are yield when **pattern is a cropped down section of the main image.** Preferably the resolution of pattern file should match the exact pixels of the repeating pattern in the image file you'll be searching for patterns in.

🟥 As of now due to my lack of knowledge on how python paths work in that OS, **this script will not work in Linux it as is.**

🟥 **This program only works with ***PNG*** Images**. This behavior was intentional as JPG photos lack the quality to be proccessed.

## 🤔 How It Works

Now to give you an example, let's imagine that you wanna build an awesome map art in Minecraft! *(Yes that's exactly how this was created!😁)* The website that generates the pixel art gives you an image like this:

![image](https://raw.githubusercontent.com/lonelyglitch/simple-pattern-recognition/main/src/image.png)

As you can see, it would extremly difficult to count how many of each block you're going to need in order to build this map art. And this is where you install the requirements and clone this repo to your computer using :

``` bash
$ git clone https://github.com/lonelyglitch/simple-pattern-recognition.git
```

Now we're going to find all the cobblestones in the image. To do so, you need a texture of cobblestone to be used as the template. You can use editing softwares to crop the pattern and extract it from the original image.

Here's the pattern for cobblestone : ![pattern](https://raw.githubusercontent.com/lonelyglitch/simple-pattern-recognition/main/patterns/cobblestone.png)

why is it so tiny? That's because as mentioned in limitations, script works better when the exact number of pixels that the pattern occupies in the original image is used as the template. In this example, the original image is a 1600 by 1600 png and the cobblestone template we extracted is a 16 by 16 png image.

Next step would be to put the template image in the ``patterns`` folder. 

Then you'd execute the script: 

``` bash
$ python matcher.py
```
program asks you to specify the name of the image file and the threshold for OpenCV match-makking algorithm. In this case 0.98 would be an optimal threshold but **you may need to use a diffrent number** if the pixels in image and pattern don't match.

Finally this is the output:

![terminal output](https://raw.githubusercontent.com/lonelyglitch/simple-pattern-recognition/main/src/screen-shot.png)

![image output](https://raw.githubusercontent.com/lonelyglitch/simple-pattern-recognition/main/src/result-preview.png)

The script has identified and counted the occurences of the ``cobblestone.png`` pattern in ``image.png`` and it has drawn a square around where the pattern was found!