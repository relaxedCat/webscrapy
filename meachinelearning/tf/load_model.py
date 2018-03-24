import tensorflow as tf
saver = tf.train.Saver()
Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0))
biases = tf.Variable(tf.zeros([1]))
with tf.Session() as sess:
    saver.restore(sess,'./model/')
