import tensorflow as tf

matrix1=tf.constant([
           [1,2],
           [4,5]
])
matrix2=tf.constant([
              [5,3],
              [3,4]
])
print(tf.matmul(matrix1,matrix2))