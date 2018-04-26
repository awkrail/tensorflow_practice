import tensorflow as tf

a = tf.constant(3, name='const1')
b = tf.Variable(0, name='val1')

# a + b
add = tf.add(a, b)

# 変数bを足した結果をアサイン
assign = tf.assign(b, add)
c = tf.placeholder(tf.int32, name='input')

# アサインした結果とcを掛け算
mul = tf.multiply(assign, c)

# 変数の初期化
init = tf.global_variables_initializer()

with tf.Session() as sess:
  sess.run(init)
  for i in range(3):
    print(sess.run(mul, feed_dict={c:3}))