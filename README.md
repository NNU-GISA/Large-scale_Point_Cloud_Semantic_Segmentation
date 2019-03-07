# Large-scale_Point_Cloud_Semantic_Segmentation
### 1 Progection Fusion
<br>
<br>

### 2 ShapeNet & 
<br>
<br>

### 3 Operating Environment
<br>
<br>

### 4 Processing training datas
*　Ｔhe point cloud decimation <br>
*　views and images generation <br>
```python
python3 sem3d_gen_images.py --config config.json 
```
<br>
<br>

### 5 Train the models (rgb, composite and fusion) from scratch
```python
python3 sem3d_train_tf.py --config config.json
```
<br>
<br>

### 6 semantic on decimated clouds
* The semantic predictions on images <br>
* back-projection on the decimated clouds <br>
```python
python3 sem3d_test_backproj.py --config config.json
```
<br>
<br>

### 7 Assign a Label to original point
* generate the files at the Semantic 3D format <br>
* assign a label to each point of the original point cloud <br>
```python
python3 sem3d_test_to_sem3D_labels.py --config config.json
```
<br>
<br>
