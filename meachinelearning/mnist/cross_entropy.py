import tensorflow as tf
import meachinelearning.mnist.regessive_model as rm
import meachinelearning.mnist.constants as const
import meachinelearning.mnist.download_data as data
y_lable = tf.placeholder(tf.float32,[None,10])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_lable * tf.log(rm.y),reduction_indices=[1]))
train = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(const.total_steps + 1):
        batch_xs,batch_ys =data.mnist .train.next_batch(const.batch_size)
        sess.run(train,feed_dict={rm.w:batch_xs,rm.y:batch_ys})
        correct_prediction = tf.equal(tf.arg_max(rm.y,axis = 1),tf.arg_max(y_lable,axis = 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
        if step % const.step_per_test == 0:
            print(step,sess.run(accuracy,feed_dict={rm.x:data.mnist.test.images,y_lable:data.mnist.test.labels}))