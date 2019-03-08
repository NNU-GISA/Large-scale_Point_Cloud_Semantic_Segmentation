# Large-scale_Point_Cloud_Semantic_Segmentation
### Progection Fusion
本项目是基于snapnet网络在semantic３Ｄ数据上训练得到的点云语义分割网络．该网络是从标注好的点云作为对象，生成用于训练的二维图像．并集成其他专有图像语义分割网络，在生成的图像上进行训练．当处理新的点云数据时网络会自动在点云上生成ＲＧＢ图像数据，并交由二维语义分割网络进行分割，最终又将二维分割的结果返投影至点云上实现对每一个点的标注．
下面的这个ＧＩＦ是网络分割后的结果
<br>
<img width="430" height="250" src="https://github.com/ZGX010/Large-scale_Point_Cloud_Semantic_Segmentation/blob/master/doc/1.gif"/></div><img width="430" height="250" src="https://github.com/ZGX010/Large-scale_Point_Cloud_Semantic_Segmentation/blob/master/doc/2.gif"/></div>

<br>

### ShapeNet & Semantic 3D dataset
#### ShapeNet
<div align=center><img width="850" height="220" src="https://github.com/ZGX010/Large-scale_Point_Cloud_Semantic_Segmentation/blob/master/doc/fllow.png"/></div>
<br>
<br>

#### Semantic 3D dataset
<br>

### Operating Environment
#### C++：　
* Cython
* PCL
* OpenMP
* NanoFlann: nanoflann.hpp should be included in the include directory
* Eigen: Eigen should also be included in the include directory

#### Python: 
* TensorFlow
* TQDM(进度条), Scipy, Numpy
<br>

### Building
```python
cd pointcloud_tools
python setup.py install --home="."
```
<br>

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
<br>

### Processing training datas
* Ｔhe point cloud decimation <br>
* views and images generation <br>
```python
python3 sem3d_gen_images.py --config config.json 
```
<br>

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
