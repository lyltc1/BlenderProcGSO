import blenderproc as bproc
import argparse
import os
import sys
import numpy as np

sys.path.append(os.path.dirname(__file__))


from GSOLoader import load_gso_objs

root = os.path.dirname(os.path.dirname(__file__))
gso_model_path_default = os.path.join(root, 'BlenderProc/resources/GoogleScannedObjects')
cc_textures_path_default = os.path.join(root, 'BlenderProc/resources/cc_textures')
output_dir_default = os.path.join(root, "output")

parser = argparse.ArgumentParser()
parser.add_argument('--gso_model_path', default=gso_model_path_default, help="Path to downloaded google scanned objects")
parser.add_argument('--cc_textures_path', default=cc_textures_path_default, help="Path to downloaded cc textures")
parser.add_argument('--output_dir', default=output_dir_default, help="Path to where the final files will be saved ")
parser.add_argument('--num_scenes', type=int, default=20, help="How many scenes with 5 images each to generate")
args = parser.parse_args()

# bproc.init()
load_gso_objs(args.gso_model_path)
