# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys
import time
import os
import numpy as np
import pandas as pd
import tensorflow as tf
os.chdir('C:')
os.chdir(r'\Users')
os.chdir(r'Home')
os.chdir(r'tensorflow-for-poets-2')
def load_graph(model_file):
    graph = tf.Graph()
    graph_def = tf.GraphDef()

    with open(model_file, "rb") as f:
        graph_def.ParseFromString(f.read())
    with graph.as_default():
        tf.import_graph_def(graph_def)

    return graph

def read_tensor_from_image_file(file_name, input_height=299, input_width=299,
				input_mean=0, input_std=255):
    input_name = "file_reader"
    output_name = "normalized"
    file_reader = tf.read_file(file_name, input_name)
    if file_name.endswith(".png"):
        image_reader = tf.image.decode_png(file_reader, channels = 3,
                                       name='png_reader')
    elif file_name.endswith(".gif"):
        image_reader = tf.squeeze(tf.image.decode_gif(file_reader,
                                                  name='gif_reader'))
    elif file_name.endswith(".bmp"):
        image_reader = tf.image.decode_bmp(file_reader, name='bmp_reader')
    else:
        image_reader = tf.image.decode_jpeg(file_reader, channels = 3,
                                        name='jpeg_reader')
    float_caster = tf.cast(image_reader, tf.float32)
    dims_expander = tf.expand_dims(float_caster, 0);
    resized = tf.image.resize_bilinear(dims_expander, [input_height, input_width])
    normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
    sess = tf.Session()
    result = sess.run(normalized)

    return result

def load_labels(label_file):
    label = []
    proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
    for l in proto_as_ascii_lines:
        label.append(l.rstrip())
    return label

if __name__ == "__main__":
    #df = pd.DataFrame(index=np.arange(0, 4260), columns=('image', 'umbrella', 'shirt', 'shorts', 'skirt' , 'sweater', 'suit', 
    #                 'jeans', 'gun', 'jacket', 'bag', 'gloves', 'trousers', 'tie', 'dress',
     #                'hat', 'scarf', 'glasses') )
    
    
    images = nos.listdir(r'C:/Users/Home/tensorflow-for-poets-2/test')
    
    
    model_file = "tf_files/retrained_graph.pb"
    label_file = "tf_files/retrained_labels.txt"
    input_height = 299#299
    input_width = 299
    input_mean = 128
    input_std = 128
    input_layer = "Mul"#Mul#input
    output_layer = "final_result"
    
    graph = load_graph(model_file)
   

    input_name = "import/" + input_layer
    output_name = "import/" + output_layer
    input_operation = graph.get_operation_by_name(input_name);
    output_operation = graph.get_operation_by_name(output_name);
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", help="image to be processed")
    args = parser.parse_args()
    
    k = int(args.k)
    #k=0
    filename='filename'+str(k)+'.csv'
    df=pd.read_csv(r'C:/Users/Home/tensorflow-for-poets-2/scripts/csv/'+filename)
    k+=1
    while k<4260:#4260
        
        image_name = images[k]
        file_name = r'tf_files/test/' +image_name

        t = read_tensor_from_image_file(file_name,
                                  input_height=input_height,
                                  input_width=input_width,
                                  input_mean=input_mean,
                                  input_std=input_std)

       

        with tf.Session(graph=graph) as sess:
            
            results = sess.run(output_operation.outputs[0],
                      {input_operation.outputs[0]: t})
            
        results = np.squeeze(results)

        top_k = results.argsort()[-5:][::-1]
        labels = load_labels(label_file)
        mas=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        mas[0] = image_name
        for i in range(len(labels)):
            for j in range(18):#19
                if df.columns[j] == labels[i]:
                    mas[j]=results[i]
        df.loc[k] = mas
        print(k)
        #print(mas)
        if k%50 ==0 or k==4260 or k==4259 or k==10:
            os.chdir('scripts')
            os.chdir('csv')
            filename='filename'+str(k)+'.csv'
            df.to_csv(filename, index=False)
            print('Saved, filename', k)
            k-=50
            filename='filename'+str(k)+'.csv'
            os.remove(filename)
            k+=50
            os.chdir('C:')
            os.chdir(r'\Users')
            os.chdir(r'Home')
            os.chdir(r'tensorflow-for-poets-2')
        k+=1