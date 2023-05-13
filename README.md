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
git clone --recursive https://github.com/lyltc1/BlenderProcGSO.git    # Not tested
```
or
```
git clone https://github.com/lyltc1/BlenderProcGSO.git
cd BlenderProcGSO
git submodule update --init  # Not tested
```
build environment
```
sudo apt install gfortran, liblapack-dev  # needed library
sudo apt install libfreetype6-dev         # needed library
pip3 install Cython==0.29.24              # needed library
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
cp -r GoogleScannedObjects path/to/BlenderProc/resources
```
option2: download by Baiduyun
```
TODO
cp -r GoogleScannedObjects path/to/BlenderProc/resources
```
- extract
```
cp path/to/BlenderProcGSO/utility/unzipGSO.py path/to/BlenderProc/resources/GoogleScannedObjects
cd path/to/BlenderProc/resources/GoogleScannedObjects
python unzipGSO.py
```

### cc_texture

option 1: download seperate texture folders by script provided by blenderproc
```
blenderproc download cc_textures path/to/BlenderProc/resources
```
option 2: download cc_textures.tar.gz by Baiduyun
```
TODO
sudo apt install pigz -y # multithread extract/compress tools
tar -I pigz -xvf cc_textures.tar.gz -C path/to/BlenderProc/resources  # do not test yet
# the compress command is tar -zcvf cc_textures.tar.gz path/to/cc_textures/
```
option 3: download cc_textures.tar.gz by OneDrive
```
TODO
```

The expected data structure:
```
BlenderProcGSO
├── BlenderProc
│   ├── resources 
│   │   ├── cc_textures
│   │   │   ├── AcousticFoam001
│   │   │   ├── ...
│   │   ├── GoogleScannedObjects
│   │   │   ├── 2_of_Jenga_Classic_Game
│   │   │   │   ├── materials
│   │   │   │   ├── ...
│   │   │   └── ...
│   │   └── ...
│   └── ...
├── bop_toolkit
├── utility
└── ...
```

## Customization
