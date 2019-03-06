


from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
#添加
import os
from distutils.sysconfig import get_config_vars
 
(opt,) = get_config_vars('OPT')
os.environ['OPT'] = " ".join(
    flag for flag in opt.split() if flag != '-Wstrict-prototypes'
)

#pcl的位置
pcl_include_dir = "/usr/include/pcl-1.9" # /home/xiaolong/pcl /usr/local/include/pcl-1.8
pcl_lib_dir = "/home/szu/pcl/release/lib" # /usr/local/lib 
vtk_include_dir = "/usr/include/vtk-5.10" 

# depending on the distribution, change the directory according to the installed version
# example for stock ubuntu 16.04:
# vtk_include_dir = "/usr/include/vtk-5.10"

ext_modules = [Extension(
       "PcTools",
       sources=["Semantic3D.pyx", "Sem3D.cxx","pointCloud.cxx", "pointCloudLabels.cxx"],  # source file(s)
       include_dirs=["third_party_includes/",pcl_include_dir, vtk_include_dir],
       language="c++",             # generate C++ code
       library_dirs=[pcl_lib_dir],
       libraries=["pcl_common","pcl_kdtree","pcl_features","pcl_surface","pcl_io"],
       extra_compile_args = ["-fopenmp", "-std=c++11"]
  )]

setup(
    name = "PointCloud tools",
    ext_modules = ext_modules,
    cmdclass = {'build_ext': build_ext},
)
