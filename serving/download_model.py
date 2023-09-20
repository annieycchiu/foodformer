import os
from pathlib import Path
import wandb

if not os.environ.get("WANDB_API_KEY"):
    raise ValueError("You must set up the WANDB_API_KEY environment bvariable in order to download the model.")


run = wandb.init()
artifact = run.use_artifact('usf-annie/model-registry/foodformer:v0', type='model')
artifact_dir = artifact.download(root="current_folder")