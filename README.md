# Large-scale_Point_Cloud_Semantic_Segmentation
### 1 Progection Fusion
<br>

### 2 ShapeNet & Semantic 3D dataset
* We pick many suitable snapshots of the point cloud. We generate two types of images: a Red-Green-Blue (RGB) view and a depth composite view containing geometric features. <br>
* We then perform a pixel-wise labeling of each pair of 2D snapshots using fully convolutional networks. Different architectures are tested to achieve a profitable fusion of our heterogeneous inputs. <br>
* Finally, we perform fast back-projection of the label predictions in the 3D space using efficient buffering to label every 3D point. Experiments show that our method is suitable for various types of point clouds such as Lidar or photogrammetric data.
<br>

### 3 Operating Environment
#### C++：　<br>
* Cython
* PCL
* OpenMP
* NanoFlann: nanoflann.hpp should be included in the include directory
* Eigen: Eigen should also be included in the include directory

#### Python: <br>
* TensorFlow
* TQDM, Scipy, Numpy
<br>

###  Building
```python
cd pointcloud_tools
python setup.py install --home="."
```

### 4 Processing training datas
*　Ｔhe point cloud decimation <br>
*　views and images generation <br>
```python
python3 sem3d_gen_images.py --config config.json 
```

### 5 Train the models (rgb, composite and fusion) from scratch
```python
python3 sem3d_train_tf.py --config config.json
```
<br>

### 6 semantic on decimated clouds
* The semantic predictions on images <br>
* back-projection on the decimated clouds <br>
```python
python3 sem3d_test_backproj.py --config config.json
```
<br>

### 7 Assign a Label to original point
* generate the files at the Semantic 3D format <br>
* assign a label to each point of the original point cloud <br>
```python
python3 sem3d_test_to_sem3D_labels.py --config config.json
```
<br>
