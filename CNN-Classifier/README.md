# CNN-Classifier
An image classifier based on TensorFlow, which can process and analyze any image. The only thing you need to do is collecting your image data.

## Prepare Environment

#### Install Pre-requisite Packages

```sh
pip3 install -r requirements.txt
```

- Tested and passed ```opencv-python``` version is ```opencv-python==3.4.1.15```
- If there is compliant about multi version of ```numpy```, you need to delete all then install and just keep the latest

```sh
pip3 uninstall numpy
```
```sh
cd ~/.local/lib/python3.5/site-packages/; ls -d numpy*
numpy  numpy-1.16.1.dist-info
```

#### Download ```vgg16.npy```, which is the pre-trained lib

https://mega.nz/#!YU1FWJrA!O1ywiCS2IiOlUCtCpI6HTJOMrneN-Qdv3ywQP5poecM

#### The Directory Tree

```sh
├── checkpoint
├── create-dataset
│   ├── create_hdf5.py
│   ├── images
│   │   ├── in_5500.jpg
│   │   ├── in_5501.jpg
│   │   ├── in_5502.jpg
│   │   ├── in_5503.jpg
│   │   ├── in_5504.jpg
│   │   ├── in_5505.jpg
│   │   ├── in_5506.jpg
│   │   ├── in_5507.jpg
│   │   ├── in_5508.jpg
│   │   ├── in_5509.jpg
│   │   ├── out_5500.jpg
│   │   ├── out_5501.jpg
│   │   ├── out_5502.jpg
│   │   ├── out_5503.jpg
│   │   ├── out_5504.jpg
│   │   ├── out_5505.jpg
│   │   ├── out_5506.jpg
│   │   ├── out_5507.jpg
│   │   ├── out_5508.jpg
│   │   └── out_5509.jpg
│   ├── __init__.py
│   ├── list_images_and_lable.py
│   ├── load_images.py
│   └── utils.py
├── index.py
├── __init__.py
├── manage.py
├── my_test_model.data-00000-of-00001
├── my_test_model.index
├── my_test_model.meta
├── predictImage.py
├── predict.py
├── __pycache__
│   ├── vgg16.cpython-35.pyc
│   └── vggnet_16.cpython-35.pyc
├── README.md
├── requirements.txt
├── settings.py
├── tools
│   ├── cnn_utils.py
│   ├── dataset.py
│   ├── __init__.py
│   └── __pycache__
│       ├── cnn_utils.cpython-35.pyc
│       ├── dataset.cpython-35.pyc
│       └── __init__.cpython-35.pyc
├── train_model.py
├── urls.py
├── vgg16.npy
├── vgg16.py
├── vggnet_16.py
└── wsgi.py

5 directories, 51 files
```

> The training images are loaded in ```create-dataset/images```

## Image Processing

- Rename your image

  Make sure your image name include the class name. For example, if you want to train a model to classify whether an image is a cat or a dog. Rename your image as `cat.jpg` or `dog.jpg`.

  You could define your own class by modifying the function in `tools/dataset.py`.

  ```python

  def list_images_and_lables(images_path, keyword='in', shuffle_data = True):
      """
      List images location and lables in the same dimensions.

      Arguments:
      images_path -- data path, the directory where saved image data.
      keyword -- image filter.
      shuffle_data -- whether shuffle data.

      Returns:
      (addrs, labels, ...) -- tuple of train/dev/test sets and lables.
      """

      # read addresses and labels from the 'train' folder
      addrs = glob.glob(images_path)

      # you can determine how many image types here
      # labels = [1 if keyword in addr else 0 for addr in addrs]  # 1 = keyword,0 = non-keyword
      labels = []
      for i in range(len(addrs)):
          # fix me! use constants or parameters here! I will fix it later
          if keyword in addrs[i]:
              labels.append(0)
          else:
              labels.append(1)
      # to shuffle data
      if shuffle_data:
          c = list(zip(addrs, labels))
          shuffle(c)
          addrs, labels = zip(*c)

      # Divide the hata into 60% train, 20% validation, and 20% test
      train_addrs = addrs[0:int(0.8*len(addrs))]
      train_labels = labels[0:int(0.8*len(labels))]

      test_addrs = addrs[int(0.8*len(addrs)):]
      test_labels = labels[int(0.8*len(labels)):]

      return (train_addrs, train_labels, test_addrs, test_labels)
  ```

- Place your image in the designated directory

- Load ```vgg16``` Model

  Use ```vgg16``` class defined in the file `vgg16.py`, then run the code in the `train_model.py` line 272-276.


  ```python
    # load pretrained vgg16 model
    vgg = vgg16.Vgg16()
    with tf.name_scope("content_vgg"):
        # load VGG16
        vgg.build(X)
  ```

## Train Model

Run `python train_model.py`, there are several important parameters you could adjust. in the line 252 - line 253, train_model.py.

- starter_learning_rate: the beginning learning rate.
- num_epochs: the loop count.
- minibatch_size: how many images load into memory in each training. I strongly recommend you choose the as 2 to the capital N power the value, such as 1, 2, 4, 8, 16, 32, 64, ...

## Save Model

In the line 366 - line 368, train_model.py.

```python
# save trained model
saver = tf.train.Saver()
tf.add_to_collection('predict_op', predict_op)
saver.save(sess, './my_test_model')
```

__Note__: You don't have to do anything about it. The model will be saved automatically once the training finish.

## Predict

- load the model you trained.

In the line 18 - line 23, in the `predict.py`.

```python
new_saver = tf.train.import_meta_graph('my_test_model.meta')
new_saver.restore(sess, 'my_test_model')

predict_op = tf.get_collection('predict_op')[0]
dataFlowGraph = tf.get_default_graph()
x = dataFlowGraph.get_tensor_by_name("X:0")
```

- Run the predict function.

In the line 50 to the end, `predict.py`.

```python
def predictImage(file_path):
    image = np.array(ndimage.imread(file_path, flatten = False))
    my_image = scipy.misc.imresize(image, size = (224, 224), mode = 'RGB')
    # my_image = my_image / 255.
    my_image_work = np.expand_dims(my_image, 0)
    print("Using a picture of shape", my_image_work.shape, "for the prediction")
    print (my_image.shape)
    prediction = sess.run(predict_op, feed_dict = {x: my_image_work})
    print("\nThe predicted image class is:", str(np.squeeze(prediction)))
    return np.squeeze(prediction)
```

Run `python predict.py <image path>`

And you'll see

```
('\nThe predicted image class is:', '0')
```

in the last line.

#### Which parameters should you choose to improve your performance?

there are somes tips:

1. learning rate
2. mini-batch size
3. hidden layers

## Have fun :)
