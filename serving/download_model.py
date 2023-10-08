import os
from pathlib import Path
import wandb

if not os.environ.get("WANDB_API_KEY"):
    raise ValueError("You must set up the WANDB_API_KEY environment variable in order to download the model.")

wandb_team = "usf-annie"
wandb_project = "Foodformer-new"
wandb_model = "vit:v0"
wandb_model_path = f"{wandb_team}/{wandb_project}/{wandb_model}"

run = wandb.init()

current_folder = Path(__file__).parent
path = wandb.use_artifact(wandb_model_path, type='model').download(root = current_folder)
