# delta9-image-classification
This repository describes how to solve an image classification problem on Windows 8.1, using Tensorflow. it's transfer learning from a popular net made by Google and called "inception".

Originally, it's a set of steps I took in a Kaggle competition https://www.kaggle.com/c/delta9 (the final score is 0.937, but you may achieve more)

This guide in presentation format: https://docs.google.com/presentation/d/1TxEu8Xt8G9fhNi1tHI7-eT4vbbISf8zj5yPvw1EixUo/edit#slide=id.p



Challenge description
============
We are given:
* 36'900 images (file *train*)
* A table: csv-file (*train.csv*), in which there are 18 columns (image name and 17 classes: *umbrella, shirt, shorts, skirt, sweater, suit, jeans, gun, jacket, bag, gloves, trousers, tie, dress, hat, scarf, glasses*) and 36900 lines. Each line says to which class the image belongs (in other words, if there is an umbrella on the image, a csv-file will contain '1' in column 'umbrella' in line of that image).  
* another 4'260 images (file *test*), which are to be classified
* Sample submission file

The challenge is to create the same csv-file for test images

Step guide
============
Basically, we need to do the following:
1. Install *Anaconda*
2. Install packages
3. Download the code from open-source
4. Sort images in folders by classes
5. Retrain the model
4. Modify the labeling script

Installing Anaconda
============
Just download it from the official site https://www.anaconda.com/download/ . There mustn't be any problems. Pay attention to this step, it's is really necessary for *tensorflow* package. There is a pip version of tensorflow, which can be installed only for 64-bit Python 3.5 and which is not running the following code.

Installing packages
============
In *Anaconda prompt* run the following lines:

*conda install tensorflow*

*conda install pandas*

Tensorflow is a popular framework for machine learning, and pandas provides working with *csv* files

Downloading the scripts
============
There is a wonderful repository of tensorflow called *tensorflow for poets-2* on github. https://github.com/googlecodelabs/tensorflow-for-poets-2

Click *download* button there. A folder *tensorflow-for poets-2* will be created in your home directory.

Sort images by classes
============
We need that step because that's how the retraining script is working. The output classes will be named after the folders.

You may use file *sort.py* of this repository. For this install *shutil* package. Create a folder "photoes" in *tf_files* directory. The result must be 17 folders, each named after the class.

The script only creates one folder. In this version we have to start it 17 times, each time manually writing the path in line *shutil.copy*

Run the retraining script
============
Now everythin is ready. Open Anaconda prompt, *cd* to *tensorflow-for-poets-2* directory and run the following (it's one line):
*python -m scripts.retrain *

*--bottleneck_dir=tf_files\bottlenecks *

*--how_many_training_steps=4000 *

*--model_dir=tf_files\models*

*--summaries_dir=tf_files\training_summaries\inception_v3*

*--architecture=inception_v3*

*--image_dir=tf_files\photoes*

*--learning_rate=0.01*

The script will download the inception model to *model_dir*. Then it will start to create bottleneck files, which basically are the descriptions of every image. In CPU it will take a lot of time (about 6-8 hours), and only then the script will train the network. Once bottlenecks are ready, you can train other inception_v3 models with different parameters on them. You also my vary the number of traing steps and learning rate, and you may use other architectures(for example, write *mobilenet_1.0_224* instead of *inception_v3*. This net is smaller and works faster, but with less accuracy). The result is the file *retrained_graph.pb* - it's your model. You can analyze the net using *tensorboard*. Run the following:

tensorboard --logdir=tf_files\training_summaries

Open your browser and write to the address line: *http:\\HomeLaptop::6006*. This will show you a set of graphics. Pay attention to cross entropy: the less it is, the better your model.

Modify the labeling script
============
Once the net is trained, you may test it running the following line (still in *tensorflow-for-poets-2* directory):

python -m scripts.label_image --graph=tf_files\retrained_graph.pb --image=tf_files\photoes\000000.jpg

The original folder *test* must be placed in *tensorflow-for-poets-2\tf_files*.

In order to get the required result, run *label_csv* script. For inception_v3 model it will take about 8 hours to go through with it. Pay attention: the more time the net is working, the slower it gets (really, several times slower). So about every 200 images you shold save current results, interrupt the code with Ctrl+C and restart the code with other number.

The script *label_csv* intializes the csv-file. It's started with line *python -m scripts.run_csv*. During process it will be showing numbers - thos are the numbers of images. After every 50 images the csv file will be saved to folder *scripts\csv*

After that, wait until the first alert *Saved, filename <n>*, interrupt the code and run the script *label_csv2*:
  
  python -m scripts.label_csv2 --k=n
 
where n is the same n which is the number of labeled images.

Researching the net
============
In the final part of the presentation above there are images, describing, which parts of an image the net bases on while classifying (pay attention that those are not the ones containing the object itself!). You may write the same thing, based on files *map0, map1* and *map2*

*map0* makes images with cut black(or white) squares and saves them to  folder

*map1* runs the net and makes a csv file with classified results

*map2* paints the red squares


  
