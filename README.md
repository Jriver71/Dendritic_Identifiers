John - I have uploaded two files. One is the DendriteTest.py and Dendritic_Identifiers. The .py executes the code to train from the provided .YAML and test an image from a given path. 
You can save a dendrite image on your compute, give the .py the path to that file and it will test that image and give an output. I have found that if the code runs but at the very end it
gives an error, it likely simply cannot find the identifier. This will probably change as we have more photos to train with. Also, in the .YAML file, you will need to change the paths to the 
folders/images on your computer.

You can read the comments in the code but here are couple notes on some things in the code:
.YAML File
A plain-text configuration file used by YOLO to specify paths to training/validation images and class names. It follows a structured, indentation-based syntax that defines your dataset setup.

Epochs
An epoch is one complete pass through the entire training dataset. Multiple epochs allow the model to repeatedly see the data, refining its parameters over time for better accuracy.

imgsz
Defines the input image size during training. Larger sizes can capture more detail (beneficial for small objects) but require more computational resources, while smaller sizes train faster but may lose important details.
