import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split


def train_DNN(X, Y):


	classifier = tf.contrib.learn.DNNClassifier(
		feature_columns=feature_columns, hidden_units=[1024, 512, 256],
		n_classes = 2, model_dir = "./weights", 
		optimizer=tf.train.ProximalAdagradOptimizer( learning_rate=1e-4, l1_regularization_strength=.001))
	classifier.fit(x=x_train,y=y_train,steps=5000)
