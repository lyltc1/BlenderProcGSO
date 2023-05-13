# BlenderProcGSO
Physically Based Rendering for Google Scanned Object using BlenderProc2

## Supported Platforms
- Linux 16.04 (Not Tested)
- Linux 18.04 (Not Tested)
- Linux 20.04 (Not Tested)
- Linux 22.04 (Tested)
- Mac (Not Tested)
- Windows (Not supported because BlenderProc is currently not supported on Windows. However, BOP toolkit supports direct rendering using its own renderers.)
## Create Conda Environment
```
conda create -n pbr python=3.9
conda activate pbr
```

## Git Pull

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

## Get Started

### 1. Prerequisite

Notice: For detailed instructions, check

https://github.com/thodan/bop_toolkit

```
pip install pyyaml
pip install cython
pip install -r bop_toolkit/requirements.txt
sudo apt install freetype
sudo apt install libglfw3
```
**Note: If freetype cannot be installed, try install it with the following command:**
```
sudo apt update && sudo apt install freetype2-demos
```
Install any other missing dependency if prompted.

### 2. Run Image Generation

## Customization
