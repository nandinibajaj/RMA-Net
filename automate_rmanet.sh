git clone https://github.com/nandinibajaj/RMA-Net

 
yes y | conda create --name rmanet_test5 python=3.8
#conda init bash
conda activate rmanet_test5

yes y | conda install pytorch=1.6.0 torchvision=0.7.0 cudatoolkit=10.2 -c pytorch

yes y | conda install -c conda-forge igl

export CUDA_HOME=/usr/local/cuda-10.2

cd RMA-Net

yes y | conda install h5py
yes y | conda install -U matplotlib
yes y | conda install opencv
yes y | pip install trimesh
yes y | conda install basemap

python build_cuda.py
mkdir pre_trained
cd pre_trained

#download weights
fileId=14XbhBu0CrHxplVnA6TTLOb_q5soCVCli
fileName=deform.pt
curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${fileId}" > /dev/null
code="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"  
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${code}&id=${fileId}" -o ${fileName}

fileId=1WGLsDeirieYjooh9WXk1ZSLZifu28M4D
fileName=mobilenet40.pt
curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${fileId}" > /dev/null
code="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"  
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${code}&id=${fileId}" -o ${fileName}

cd ..

python inference.py --weight './pre_trained/mobilenet40.pt' --src './lander/sourceCAD_2055.obj' --tgt './lander/farthestObj_surface2055.obj' --iteration 7 --device_id 0 --if_nonrigid 1

python inference.py --weight './pre_trained/deform.pt' --src './lander/sourceCAD_2055.obj' --tgt './lander/farthestObj_surface2055.obj' --iteration 7 --device_id 0 --if_nonrigid 1







