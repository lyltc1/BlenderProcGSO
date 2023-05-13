# BlenderProcGSO
Physically Based Rendering for Google Scanned Object using BlenderProc2
## Supported Platforms
- Linux 22.04 (Tested)
## Prerequisite
```
conda create -n pbr python=3.9
conda activate pbr
```
pull with
```
git clone --recursive https://github.com/lyltc1/BlenderProcGSO.git
```
or
```
git clone https://github.com/lyltc1/BlenderProcGSO.git
cd BlenderProcGSO
git submodule update --init
```
build environment
```
sudo apt install gfortran, liblapack-dev
sudo apt install libfreetype6-dev
pip3 install Cython==0.29.24
cd path/to/bop_toolkit
pip install -r requirements.txt -e .
cd path/to/BlenderProc
pip install -e .
```
**Note: Install any other missing dependency if prompted.

## Prepare data
### Google Scanned Objects
- download

option 1: download by Script provided by GSO origin paper
```
TODO
```
option2: download by Baiduyun
```
TODO
```
- extract
```
cp path/to/BlenderProcGSO/utility/unzipGSO.py path/to/BlenderProc/resources/GoogleScannedObjects
cd path/to/BlenderProc/resources/GoogleScannedObjects
python unzipGSO.py
```

### cc_texture
- download

option 1: download by script provided by blenderproc
```
blenderproc download cc_textures path/to/BlenderProc/resources
```
option 2: download by Baiduyun
```
TODO
```
option 3: download by OneDrive
```
TODO
```
## Customization
