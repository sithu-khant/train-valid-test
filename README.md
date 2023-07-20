# Train Valid Test

Codes for splitting training, validation, and testing dataset. To read the full blog post about
this, [see here](https://medium.com/artificialis/why-how-we-split-train-valid-and-test-fb4d6746ede)

![Photo by Pietro Jeng on Unsplash](images/cover-img.jpg)

During coding your machine learning project or learning machine learning, did you confuse about the data to split? I
don’t know about you, but I did like that. Not only train and test data set but also valid data set. Why do we split
like that
there and how to split? This is [a good blog](https://www.fast.ai/posts/2017-11-13-validation-sets.html) by Rachel
Thomas from Fast.ai and you should read that blog too. His blog
and mine will give you the same concepts and workflow but with different points of view.

Before talking about the train, validate and test. Let’s talk about machine learning. As you know machine learning
models/algorithms depend on the data. The more data, the better it works. Not just with more data, but it also should be
the right data. Even though you have plenty of data with not the right features/values, your model cannot work well. So,
this is where the train, valid, and test data sets come in. See the short brief definition of these three:

1. Training set — to train your model on this data set
2. Validation set — to test your different models on this before testing the data set, to make hyperparameter tuning
3. Testing set — to test your model on this; after testing and tuning on the validation set, to know how well your model
   in real-time

If you want to read the full blog about
this, [read it](https://medium.com/artificialis/why-how-we-split-train-valid-and-test-fb4d6746ede) on my medium account under
handle of [Artificialis](https://medium.com/artificialis) publication.

## Requirements

* Pandas
* NumPy
* Scikit-Learn

If you like to read my blogs, you can follow me on [Medium](https://medium.com/@sithukhantai)

If you have any problem or want to contact me, [email me](mailto:sithukhantai@gmail.com)
