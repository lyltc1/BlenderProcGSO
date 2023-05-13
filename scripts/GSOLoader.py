"""Provides functions to load the objects inside the google scanned objects."""

import os
from random import choice
from typing import List, Optional, Tuple

import bpy
import numpy as np
from mathutils import Matrix, Vector

from blenderproc.python.utility.SetupUtility import SetupUtility
from blenderproc.python.camera import CameraUtility
from blenderproc.python.types.MeshObjectUtility import MeshObject
from blenderproc.python.utility.MathUtility import change_source_coordinate_frame_of_transformation_matrix
from blenderproc.python.loader.ObjectLoader import load_obj

def load_gso_objs(gso_model_path: str, 
                  model_names: Optional[List[str]] = None,
                  num_of_models: Optional[int] = None,
                  copy_limit: int = -1, mm2m: bool = False) -> List[MeshObject]:
    """ Loads all or a subset of 3D models of gso_model_path

    :param gso_model_path: Path to google scanned objects folder.
    :param model_names: List of object names to load. Default: [] (load all models from gso_model_path)
    :param num_of_models: Amount of models to sample. If this amount is bigger
                                  than the dataset actually contains, then all models will be loaded.
    :param copy_limit: Limits the amount of object copies when sampling. Default: -1 (no limit).
    :return: The list of loaded mesh objects.
    """
    models_dir = [item for item in os.listdir(gso_model_path) if os.path.isdir(os.path.join(gso_model_path, item))]
    print(f"gso_model_path contains {len(models_dir)}")