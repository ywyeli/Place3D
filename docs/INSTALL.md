## Installation

We test our codebase on Ubuntu 20.04. Please follow the steps below to set up the environment and prepare the dataset. 

### Step 1 Collect Dataset

Download [CARLA v0.9.10](https://carla.org/2020/09/25/release-0.9.10/) and extract it to the `./carla` directory. Then Install the required Python packages:

```bash
pip install -r docs/requirements.txt
```

Run the CARLA simulator with:

```bash
cd ./carla
sh CarlaUE4.sh
```

Then run the following command in a new termial to collect dataset. 

```bash
cd ./carla_nus/scripts
bash routes_baselines.sh
```

This process typically takes ~6 hours on an NVIDIA RTX 4090. Sensor configurations are defined in `carla_nus/hyperparams/`. You are encouraged to try different setups by modifying the config path in `routes_baselines.sh`.

The collected dataset will be saved to `./carla_nus/dataset`. 
LiDAR point clouds: `./carla_nus/dataset/nus/LiDAR_p{i}_samples`. 
Images: `./carla_nus/dataset/nus/IMAGE`. 

### Step 2 Generate Annotations

Please run the following command to generate ground truth labels in `nuScenes` format (same annotations for all sensor setups)

```bash
cd ./nus_tool
bash run_create_label.sh
```

Annotations will be saved in `v1.0-trainval` folder.
Note: Our dataset does not use maps, but for compatibility with the nuScenes-devkit, you must still download the map files from [nuScenes Downloads](https://www.nuscenes.org/nuscenes#download). Please organize your dataset as the following directory structure:

```
dataset
├── nus
│   ├── LiDAR_p{i}_samples
│   │   ├── maps
│   │   ├── samples
|   |   |   ├── CAM_BACK
|   |   |   ├── CAM_BACK_LEFT
|   |   |   ├── CAM_BACK_RIGHT
|   |   |   ├── CAM_FRONT
|   |   |   ├── CAM_FRONT_LEFT
|   |   |   ├── CAM_FRONT_RIGHT
|   |   |   ├── LIDAR_TOP
|   |   ├── v1.0-trainval

```

Then you can filter out unused data frames using the following script:

```bash
cd ./nus_tool
python check_sensor.py
```

### Step 3 Setup for Development

To ensure compatibility, add our customized `dataset_utils` path to your `PYTHONPATH`. Edit `~/.bashrc` or `~/.zshrc`:

```bash
export PYTHONPATH="$PYTHONPATH:/[YOUR_PARENT_FOLDER]/Place3D/projects/dataset_utils"
```

Apply the change:
```bash
source ~/.bashrc  # or ~/.zshrc
```

Do not install the official `nuscenes-devkit`, as it may cause compatibility issues. Our dataset is in `nuScenes` format, but requires our customized tools. Then you can use the dataset the same as `nuScenes`.

We provide a custimized version of [BEVFusion](https://github.com/mit-han-lab/bevfusion) under `Place3D/projects/bevfusion/`. Create a symbolic link from the dataset root: 

```bash
ln -s ./carla_nus/dataset/nus/LiDAR_p{i}_samples $BEVFUSION_DIR/data/nuscenes 
```

Then follow BEVFusion’s instructions (again, without installing `nuscenes-devkit`) to train and evaluate on the collected dataset.








