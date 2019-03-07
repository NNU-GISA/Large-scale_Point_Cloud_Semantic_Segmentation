# Large-scale_Point_Cloud_Semantic_Segmentation
### Progection Fusion
<br>

### ShapeNet & Semantic 3D dataset
* We pick many suitable snapshots of the point cloud. We generate two types of images: a Red-Green-Blue (RGB) view and a depth composite view containing geometric features. <br>
* We then perform a pixel-wise labeling of each pair of 2D snapshots using fully convolutional networks. Different architectures are tested to achieve a profitable fusion of our heterogeneous inputs. <br>
* Finally, we perform fast back-projection of the label predictions in the 3D space using efficient buffering to label every 3D point. Experiments show that our method is suitable for various types of point clouds such as Lidar or photogrammetric data.
<br>

### Operating Environment
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

### Building
```python
cd pointcloud_tools
python setup.py install --home="."
```
### Configuration file
```python
{
    "train_input_dir":"path_to_directory_TRAIN",
    "test_input_dir":"path_to_directory_TEST",
    "train_results_root_dir":"where_to_put_training_products",
    "test_results_root_dir":"where_to_put_test_products",
    "images_dir":"images",

    training:true,

    "imsize":224,
    "voxel_size":0.1,

    "train_cam_number":10,
    "train_create_mesh" : true,
    "train_create_views" : true,
    "train_create_images" : true,

    "test_cam_number":10,
    "test_create_mesh" : true,
    "test_create_views" : true,
    "test_create_images" : true,

    "vgg_weight_init":"path_to_vgg_weights",
    "batch_size" : 24,
    "learning_rate" : 1e-4,
    "epoch_nbr" : 100,
    "label_nbr" : 10,
    "input_ch" : 3,

    "train_rgb" : true,
    "train_composite" : true,
    "train_fusion" : true,

    "saver_directory_rgb" : "path_to_rgb_model_directory",
    "saver_directory_composite" : "path_to_composite_model_directory",
    "saver_directory_fusion" : "path_to_fusion_model_directory",
    "output_directory":"path_to_output_product_directory"
}
```

### Processing training datas
* Ｔhe point cloud decimation <br>
* views and images generation <br>
```python
python3 sem3d_gen_images.py --config config.json 
```

### Train the models (rgb, composite and fusion) from scratch
```python
python3 sem3d_train_tf.py --config config.json
```
<br>

### semantic on decimated clouds
* The semantic predictions on images <br>
* back-projection on the decimated clouds <br>
```python
python3 sem3d_test_backproj.py --config config.json
```
<br>

### Assign a Label to original point
* generate the files at the Semantic 3D format <br>
* assign a label to each point of the original point cloud <br>
```python
python3 sem3d_test_to_sem3D_labels.py --config config.json
```
<br>
