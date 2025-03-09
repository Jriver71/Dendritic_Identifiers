######################################################################
Pip commands you will need after installing Python and Pip
You will not be able to run some of the scripts without doing these

pip install ultralytics
pip install opencv-python
pip install numpy
pip install matplotlib
pip install segment-anything
pip install torch torchvision torchaudio
pip install scikit-learn
pip install pillow pillow-heif

#####################################################################

John - 08MAR25
I have uploaded 4 new files. Below are the explainations. 
First a few points.
1. For this to work both the labels for the training and validation images need to be in the same folder with the same name. If you have image 0.jpg, then you should have a corresponding 0.txt label for the image right next to it in the same folder. 
2. You should have a training folder and a validation folder. The train and validation folders should be in the same parent folder. See my example below
     train: "C:/488/FindDendrites/Images/Train"  # e.g., "C:/datasets/dendrites/train"
     val: "C:/488/FindDendrites/Images/Val"      # e.g., "C:/datasets/dendrites/val"
   Both Train an validation images (and their labels) are in the same "Images" folder.

3. Once you run the DendriteTeach.py and it boxes your test image and identifies that its a dendrite, then you can run the Dendrite Identifier.py and it will try to identify the image you give it via the file path to the image. See important details below.

DendriteTeach.py
This code is what I used to teach the model. You will need to change the test image file path (line 7) to a .jpg or .png image you want to test. Ensure the .YAML file path (line 6) is the right file path for you. 
##################################################### !!IMPORTANT!! ##################################################################################################

After running this successfully, YOLO will create a few files. 

weights/best.pt	- The best-performing model (highest validation mAP). Use this for inference!
weights/last.pt	- The final model after training completes (may not be the best).
results.csv	- CSV log of training metrics (loss, mAP, precision, recall).
results.png	- A graph showing loss, precision, recall, and mAP curves.
train_batch0.jpg	- Sample images from training with labels.
val_batch0_labels.jpg	- Sample validation images with predictions.
confusion_matrix.png	- Confusion matrix (shows misclassifications).
F1_curve.png	- F1-score progression over training epochs.
P_curve.png	- Precision over epochs.
R_curve.png	- Recall over epochs.
PR_curve.png	- Precision-Recall curve to measure detection quality.
########################################################

The most important of these files is the first one, best.pt. These are the weights the model uses. This is what the model has "learned". You can keep training this model and it will update these weights.
The best.pt file is what you will need in the Dendrite Identifier.py.

######################################################################################################################################################################

Dendrite Identifier.py
This file will attempt to identify and box the presence of the dendrite. You will need the file path to the weights/best.pt file so the model know what weights to use when trying to detect. In line 7, you will insert the file path to an image you want the model to try and detect a dendrite for.

NameChanger.py
Given the dendrite photos often have names like "Screenshot_date_time_number", I wanted to have code that simplifies the names so we can track what dendrites are being tested and it is easier to input these names. This is simply for ease. You dont have to use it but testing image 10.jpg vs Screenshot_1231234asfdadf_@314123fasdf.jpg is easier.

ChangeToJPG.py
This code is to change the images that are not in the .jpg format to the .jpg format. YOLO does not work well with images not in the .jpg or .png format. If the photo is taken from an Iphone, you will need to run this code. This will require an input and output folder. Make them the same folder and the code will produce the .jpg image and put it in the same folder.
After, sort your file by type and delete all other non .jpg or.png files. Your images shoudl only be .jpg or .png.

15FEB25 John - I have uploaded two files. One is the DendriteTest.py and Dendritic_Identifiers. The .py executes the code to train from the provided .YAML and test an image from a given path. 
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



