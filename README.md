# Train Valid Test

Codes for splitting training, validation and testing dataset. To read the full blog post about
this, [see here](https://iukt.medium.com/why-how-we-split-train-valid-and-test-fb4d6746ede)

![Photo by Pietro Jeng on Unsplash](images/cover-img.jpg)

During coding your machine learning project or learning machine learning, did you confuse about the data to split? I
don’t no about you, but I did. Not only train and test data set but also valid data set. Why we split like that there
and how to split? This is [a good blog](https://www.fast.ai/posts/2017-11-13-validation-sets.html) by Rachel Thomas from
Fast.ai and you also should read that blog too. His blog and mine will give you the same concepts and workflow, but with
different point of view.

Before talking about train, valid and test. Let’s talk about machine learning. As you know machine learning
model/algorithm depend on the data. The more data, the better it works. Not just with the more data, it also should be
the right data. Even though you have a plenty of data with not the right features/values, your model cannot work well.
So, this is where train, valid and test data set come in. See the short brief definition of these three:

1. Training set — to train your model on this data set
2. Validation set — to test your model on this before testing data set, to make hyperparameter tuning on these
3. Testing set — to test your model on this; after testing and tuning on validation set, to know how well done your
   model on real time

If you want to read full blog about this, read it on my medium account under handle
of [Artificialis](https://medium.com/artificialis) publication.

## Requirements

* Pandas
* NumPy
* Scikit-Learn

If you love to read my blogs, you can follow me on [Medium](https://iukt.medium.com/)

If you have any problem or want to contact with me, [email me](mailto:iukt@tuta.io)
