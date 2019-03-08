# Large-scale_Point_Cloud_Semantic_Segmentation
### Progection Fusion
This project is a point cloud semantic segmentation network trained by the snapnet network on semantic3D data. The network first generates images for training on the point cloud and then uses other image semantic segmentation networks to train on the images. When processing new point cloud data, RGB images are automatically generated on the point cloud, and these images are labeled by the image semantic segmentation network. The network backprojects the results of the image segmentation to the point cloud.
<br>
The following GIF is the result of the network segmentation point cloud
<br>

<img width="430" height="250" src="https://github.com/ZGX010/Large-scale_Point_Cloud_Semantic_Segmentation/blob/master/doc/1.gif"/></div><img width="430" height="250" src="https://github.com/ZGX010/Large-scale_Point_Cloud_Semantic_Segmentation/blob/master/doc/2.gif"/></div>
<br>
<br>

### SnapNet & Semantic 3D dataset
#### ShapNet
<div align=center><img width="850" height="220" src="https://github.com/ZGX010/Large-scale_Point_Cloud_Semantic_Segmentation/blob/master/doc/fllow.png"/></div>
<br>

SnapＮet's performance on the semantic 3D dataset is second only to SPGraph. It is the best network based on tensorflow in the field of point cloud segmentation. Then the snapnet network later introduced the robot version snapNet++ for target detection.
<br>

#### Semantic 3D dataset
They provide training and test data as a compressed ascii text file format of {x, y, z, intensity, r, g, b}. The basic facts are provided in the form of a single column ascii file, where the row id of the class labels corresponds to the point. 7zip is used for compression and is available for Windows and Linux. <br>
Data download link：　http://www.semantic3d.net/view_dbase.php?chl=1
<br>
<br>

### Operating Environment
#### C++：　
* Cython
* PCL　＝　
* OpenMP　＝　
* NanoFlann: nanoflann.hpp should be included in the include directory
* Eigen: Eigen should also be included in the include directory
<br>
<br>

#### Python: 
* TensorFlow
* TQDM, Scipy, Numpy
<br>
<br>

### Building
pointcloud文件夹中放置了安装文件，在文件中运行pointcloud_tools脚本安装软件．
```python
cd pointcloud_tools
python setup.py install --home="."
```
<br>
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
<br>

### Processing training datas
* Ｔhe point cloud decimation <br>
* views and images generation <br>
请按照提供的训练数据下载地址，下载训练与测试数据．然后运行图像生成脚本生成的图像文件和对应的相机位置文件，这些文件将放置在对应的文件夹．
```python
python3 sem3d_gen_images.py --config config.json 
```
<br>
<br>

### Train the models (rgb, composite and fusion) from scratch
此时需要训练的是
```python
python3 sem3d_train_tf.py --config config.json
```
<br>
<br>

### semantic on decimated clouds
* The semantic predictions on images <br>
* back-projection on the decimated clouds <br>
```python
python3 sem3d_test_backproj.py --config config.json
```
<br>
<br>

### Assign a Label to original point
* generate the files at the Semantic 3D format <br>
* assign a label to each point of the original point cloud <br>
```python
python3 sem3d_test_to_sem3D_labels.py --config config.json
```
<br>
<br>

### 利用网络在新点上进行推理
#### 对点云数据进行预处理
#### 将点云数据输入网络

