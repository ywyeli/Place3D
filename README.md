<p align="right">English | <a href="./README_CN.md">简体中文</a></p>  


<p align="center">
  <img src="docs/figs/logo.png" align="center" width="26%">
  
  <h3 align="center"><strong>Is Your LiDAR Placement Optimized for 3D Scene Understanding?</strong></h3>

  <p align="center">
      <a href="https://ywyeli.github.io/" target='_blank'>Ye Li</a><sup>1</sup>&nbsp;&nbsp;&nbsp;
      <a href="https://ldkong.com/" target='_blank'>Lingdong Kong</a><sup>2</sup>&nbsp;&nbsp;&nbsp;
      <a href="https://hanjianghu.net/" target='_blank'>Hanjiang Hu</a><sup>3</sup>&nbsp;&nbsp;&nbsp;
      <a href="https://scholar.google.com/citations?user=3Ifn2DoAAAAJ" target='_blank'>Xiaohao Xu</a><sup>1</sup>&nbsp;&nbsp;&nbsp;
      <a href="https://robotics.umich.edu/profile/xiaonan-sean-huang/" target='_blank'>Xiaonan Huang</a><sup>1</sup>
  <br />
  <sup>1</sup>University of Michigan, Ann Arbor&nbsp;&nbsp;&nbsp;
  <sup>2</sup>National University of Singapore&nbsp;&nbsp;&nbsp;
  <sup>3</sup>Carnegie Mellon University
  </p>

</p>

<p align="center">
  <a href="https://arxiv.org/abs/2403.17009" target='_blank'>
    <img src="https://img.shields.io/badge/Paper-%F0%9F%93%83-slategray">
  </a>
  
  <a href="" target='_blank'>
    <img src="https://img.shields.io/badge/Project-%F0%9F%94%97-lightblue">
  </a>
  
  <a href="" target='_blank'>
    <img src="https://img.shields.io/badge/Demo-%F0%9F%8E%AC-pink">
  </a>
  
  <a href="" target='_blank'>
    <img src="https://img.shields.io/badge/%E4%B8%AD%E8%AF%91%E7%89%88-%F0%9F%90%BC-red">
  </a>
  
  <a href="" target='_blank'>
    <img src="https://visitor-badge.laobi.icu/badge?page_id=ywyeli.Place3D&left_color=gray&right_color=firebrick">
  </a>
</p>


## About

`Place3D` is a full-cycle pipeline that encompasses LiDAR placement optimization, data generation, and downstream evaluations. 

- To identify the most effective configurations for multi-LiDAR systems, we introduce the Surrogate Metric of the Semantic Occupancy Grids (M-SOG) to evaluate LiDAR placement quality.
- Leveraging the M-SOG metric, we propose a novel optimization strategy to refine multi-LiDAR placements.
- Centered around the theme of multi-condition multi-LiDAR perception, we collect a 364,000-frame dataset from both clean and adverse conditions.

We showcase exceptional robustness in both 3D object detection and LiDAR semantic segmentation tasks, under diverse adverse weather and sensor failure conditions.



| <img src="docs/figs/waymo.jpg" align="center" width="210"> | <img src="docs/figs/motional.jpg" align="center" width="210"> | <img src="docs/figs/cruise.jpg" align="center" width="210"> | <img src="docs/figs/pony.jpg" align="center" width="210"> |
| :-: | :-: | :-: | :-: |
| Waymo | Motional | Cruise | Pony.ai |
| <img src="docs/figs/zoox.jpg" align="center" width="210"> | <img src="docs/figs/toyota.jpg" align="center" width="210"> | <img src="docs/figs/momenta.jpg" align="center" width="210"> | <img src="docs/figs/ford.jpg" align="center" width="210">
| Zoox | Toyota | Momenta | Ford | 

Visit our [project page]() to explore more examples. :blue_car:



## Updates

- \[2024.09\] - Place3D was selected as a spotlight at NeurIPS 2024!
- \[2024.03\] - Our [paper](https://arxiv.org/abs/2403.17009) is available on arXiv. The code has been made publicly accessible. :rocket:



## Outline

- [Installation](#gear-installation)
- [Data Preparation](#hotsprings-data-preparation)
- [Sensor Placement](#blue_car-sensor-placement)
- [Place3D Pipeline](#ferris_wheel-place3d-pipeline)
- [Getting Started](#rocket-getting-started)
- [SOG Generation](#hammer_and_wrench-sog-generation)
- [Model Zoo](#dragon-model-zoo)
- [Place3D Benchmark](#bar_chart-place3d-benchmark)
- [TODO List](#memo-todo-list)
- [Citation](#citation)
- [License](#license)
- [Acknowledgements](#acknowledgements)



## :gear: Installation

For details related to installation and environment setups, kindly refer to [INSTALL.md](docs/INSTALL.md).



## :hotsprings: Data Preparation

The `Place3D` dataset consists of a total of eleven LiDAR placements, in which seven baselines are inspired by existing self-driving configurations from autonomous vehicle companies and four LiDAR placements are obtained by sensor optimization.

Each LiDAR placement contains four LiDAR sensors. For each LiDAR configuration, the sub-dataset consists of 13,600 frames of samples, comprising 11,200 samples for training and 2,400 samples for validation, following the split ratio used in nuScenes.

| <img src="docs/figs/town01.png" align="center" width="125"> | <img src="docs/figs/town03.png" align="center" width="125"> | <img src="docs/figs/town04.png" align="center" width="125"> | <img src="docs/figs/town06.png" align="center" width="125">
| :-: | :-: | :-: | :-: | 
| Town 1 | Town 3 | Town 4 | Town 6 |

We choose four maps (Towns 1, 3, 4, and 6) in CARLA v0.9.10 to collect point cloud data and generate ground truth information. For each map, we manually set 6 ego-vehicle routes to cover all roads with no roads overlapped. The frequency of the simulation is set to 20 Hz. 

Our datasets are hosted by [OpenDataLab](https://opendatalab.com/).
><img src="https://raw.githubusercontent.com/opendatalab/dsdl-sdk/2ae5264a7ce1ae6116720478f8fa9e59556bed41/resources/opendatalab.svg" width="32%"/><br>
> OpenDataLab is a pioneering open data platform for the large AI model era, making datasets accessible. By using OpenDataLab, researchers can obtain free formatted datasets in various fields.

Kindly refer to [DATA_PREPARE.md](docs/document/DATA_PREPARE.md) for the details to prepare the `Place3D` dataset.



## :blue_car: Sensor Placement

| <img src="docs/figs/1_center.png" align="center" width="210"> | <img src="docs/figs/2_line.png" align="center" width="210"> | <img src="docs/figs/3_pyramid.png" align="center" width="210"> | <img src="docs/figs/4_square.png" align="center" width="210"> |
| :-: | :-: | :-: | :-: |
| Center | Line | Pyramid | Square |
| <img src="docs/figs/5_trapezoid.png" align="center" width="210"> | <img src="docs/figs/6_line_roll.png" align="center" width="210"> | <img src="docs/figs/8_ours_det.png" align="center" width="210"> | <img src="docs/figs/7_ours_seg.png" align="center" width="210">
| Trapezoid | Line-Roll | Ours (Det) | Ours (Seg) | 



## :ferris_wheel: Place3D Pipeline

| <img src="docs/figs/pipeline.png" align="center" width="98%"> |
We first generate Probabilistic SOG (b) by merging multiple frames of data synthesized in CARLA into dense point cloud (a) and obtain voxels covered by LiDAR rays to compute the Surrogate Metric of Semantic Occupancy Grids (M-SOG) based on the joint probability distribution of covered voxels (c). We propose a CMA-ES-based optimization strategy to maximize M-SOG, finding optimal LiDAR placement (d). To verify the effectiveness of our optimization strategy, we contribute a multi-condition multi-LiDAR dataset (e). We train several state-of-the-art models and evaluate the performance of baseline and optimized placements on both clean and corruption data (f). Our optimized placement generally outperforms all baseline placements in experiments.



## :rocket: Getting Started

To learn more usage about this codebase, kindly refer to [GET_STARTED.md](docs/GET_STARTED.md).



## :hammer_and_wrench: SOG Generation

| <img src="docs/figs/sog.png" align="center" width="99%"> |
We generate dense point clouds (b) by merging multiple frames of raw point clouds (a). Then, we voxelize the dense point clouds into Semantic Occupancy Grids (SOG) (c), and traverse all frames of dense point clouds to compute Probabilistic Semantic Occupancy Grids (P-SOG) (d).



## :dragon: Model Zoo

<details open>
<summary>&nbsp<b>LiDAR Semantic Segmentation</b></summary>

> - [x] **[MinkUNet](https://arxiv.org/abs/1904.08755), CVPR 2019.** <sup>[**`[Code]`**](https://github.com/NVIDIA/MinkowskiEngine)</sup>
> - [x] **[PolarNet](https://arxiv.org/abs/2003.14032), CVPR 2020.** <sup>[**`[Code]`**](https://github.com/edwardzhou130/PolarSeg)</sup>
> - [x] **[SPVCNN](https://arxiv.org/abs/2007.16100), ECCV 2020.** <sup>[**`[Code]`**](https://github.com/mit-han-lab/spvnas)</sup>
> - [x] **[Cylinder3D](https://arxiv.org/abs/2011.10033), CVPR 2021.** <sup>[**`[Code]`**](https://github.com/xinge008/Cylinder3D)</sup>

</details>

<details open>
<summary>&nbsp<b>3D Object Detection</b></summary>

> - [x] **[PointPillars](https://arxiv.org/abs/1812.05784), CVPR 2019.** <sup>[**`[Code]`**](https://github.com/nutonomy/second.pytorch)</sup>
> - [x] **[CenterPoint](https://arxiv.org/abs/2006.11275), CVPR 2021.** <sup>[**`[Code]`**](https://github.com/tianweiy/CenterPoint)</sup>
> - [x] **[BEVFusion](https://arxiv.org/abs/2205.13542), ICRA 2023.** <sup>[**`[Code]`**](https://github.com/mit-han-lab/bevfusion)</sup>
> - [x] **[FSTR](https://ieeexplore.ieee.org/document/10302363), TGRS 2023.** <sup>[**`[Code]`**](https://github.com/Poley97/FSTR)</sup>

</details>



## :bar_chart: Place3D Benchmark

### LiDAR Semantic Segmentation

<table>
    <thead>
        <tr>
            <th rowspan="2">Method</th>
            <th colspan="3">Center</th>
            <th colspan="3">Line</th>
            <th colspan="3">Pyramid</th>
            <th colspan="3">Square</th>
        </tr>
        <tr>
            <th>mIoU</th><th>mAcc</th><th>ECE</th><th>mIoU</th><th>mAcc</th><th>ECE</th><th>mIoU</th><th>mAcc</th><th>ECE</th><th>mIoU</th><th>mAcc</th><th>ECE</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>MinkUNet</td>
            <td>65.7</td>
            <td>72.4</td>
            <td>0.041</td>
            <td>59.7</td>
            <td>67.7</td>
            <td>0.037</td>
            <td>62.7</td>
            <td>70.6</td>
            <td>0.072</td>
            <td>60.7</td>
            <td>68.4</td>
            <td>0.043</td>
        </tr>
        <tr>
            <td>PolarNet</td>
            <td>71.0</td>
            <td>76.0</td>
            <td>0.033</td>
            <td>67.7</td>
            <td>74.1</td>
            <td>0.034</td>
            <td>67.7</td>
            <td>73.0</td>
            <td>0.032</td>
            <td>69.3</td>
            <td>74.7</td>
            <td>0.033</td>
        </tr>
        <tr>
            <td>SPVCNN</td>
            <td>67.1</td>
            <td>74.4</td>
            <td>0.034</td>
            <td>59.3</td>
            <td>66.7</td>
            <td>0.068</td>
            <td>67.6</td>
            <td>74.0</td>
            <td>0.037</td>
            <td>63.4</td>
            <td>70.2</td>
            <td>0.031</td>
        </tr>
        <tr>
            <td>Cylinder3D</td>
            <td>72.7</td>
            <td>79.2</td>
            <td>0.041</td>
            <td>68.9</td>
            <td>76.3</td>
            <td>0.045</td>
            <td>68.4</td>
            <td>76.0</td>
            <td>0.093</td>
            <td>69.9</td>
            <td>76.7</td>
            <td>0.044</td>
        </tr>
        <tr>
            <td><strong>Average</strong></span></td>
            <td>69.1</td>
            <td>75.5</td>
            <td>0.037</td>
            <td>63.9</td>
            <td>71.2</td>
            <td>0.046</td>
            <td>66.6</td>
            <td>73.4</td>
            <td>0.059</td>
            <td>65.8</td>
            <td>72.5</td>
            <td>0.038</td>
        </tr>
    </tbody>
    <tfoot>
        <tr>
            <th rowspan="2">Method</th>
            <th colspan="3">Trapezoid</th>
            <th colspan="3">Line-Roll</th>
            <th colspan="3">Pyramid-Roll</th>
            <th colspan="3">Ours</th>
        </tr>
        <tr>
            <th>mIoU</th><th>mAcc</th><th>ECE</th><th>mIoU</th><th>mAcc</th><th>ECE</th><th>mIoU</th><th>mAcc</th><th>ECE</th><th>mIoU</th><th>mAcc</th><th>ECE</th>
        </tr>
        <tr>
            <td>MinkUNet</td>
            <td>59.0</td>
            <td>66.2</td>
            <td>0.040</td>
            <td>58.5</td>
            <td>66.4</td>
            <td>0.047</td>
            <td>62.2</td>
            <td>69.6</td>
            <td>0.051</td>
            <td>66.5</td>
            <td>73.2</td>
            <td>0.031</td>
        </tr>
        <tr>
            <td>PolarNet</td>
            <td>66.8</td>
            <td>72.3</td>
            <td>0.034</td>
            <td>67.2</td>
            <td>72.8</td>
            <td>0.037</td>
            <td>70.9</td>
            <td>75.9</td>
            <td>0.035</td>
            <td>76.7</td>
            <td>81.5</td>
            <td>0.033</td>
        </tr>
        <tr>
            <td>SPVCNN</td>
            <td>61.0</td>
            <td>68.8</td>
            <td>0.044</td>
            <td>60.6</td>
            <td>68.0</td>
            <td>0.034</td>
            <td>67.9</td>
            <td>74.2</td>
            <td>0.033</td>
            <td>68.3</td>
            <td>74.6</td>
            <td>0.034</td>
        </tr>
        <tr>
            <td>Cylinder3D</td>
            <td>68.5</td>
            <td>75.4</td>
            <td>0.057</td>
            <td>69.8</td>
            <td>77.0</td>
            <td>0.048</td>
            <td>69.3</td>
            <td>77.0</td>
            <td>0.048</td>
            <td>73.0</td>
            <td>78.9</td>
            <td>0.037</td>
        </tr>
        <tr class="highlight">
            <td><strong>Average</strong></td>
            <td>63.8</td>
            <td>70.7</td>
            <td>0.044</td>
            <td>64.0</td>
            <td>71.1</td>
            <td>0.042</td>
            <td>67.6</td>
            <td>74.2</td>
            <td>0.042</td>
            <td>71.1</td>
            <td>77.1</td>
            <td>0.034</td>
        </tr>
    </tbody>
    </tfoot>
</table>

### 3D Object Detection

<table>
    <thead>
        <tr>
            <th rowspan="2"><strong>Method</strong></th>
            <th colspan="3"><strong>Center</strong></th>
            <th colspan="3"><strong>Line</strong></th>
            <th colspan="3"><strong>Pyramid</strong></th>
            <th colspan="3"><strong>Square</strong></th>
        </tr>
        <tr>
            <th>Car</th>
            <th>Ped</th>
            <th>Bicy</th>
            <th>Car</th>
            <th>Ped</th>
            <th>Bicy</th>
            <th>Car</th>
            <th>Ped</th>
            <th>Bicy</th>
            <th>Car</th>
            <th>Ped</th>
            <th>Bicy</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>PointPillars</td>
            <td>46.5</td>
            <td>19.4</td>
            <td>27.1</td>
            <td>43.4</td>
            <td>22.0</td>
            <td>27.7</td>
            <td>46.1</td>
            <td>24.4</td>
            <td>29.0</td>
            <td>43.8</td>
            <td>20.8</td>
            <td>27.1</td>
        </tr>
        <tr>
            <td>CenterPoint</td>
            <td>55.8</td>
            <td>28.7</td>
            <td>28.8</td>
            <td>54.0</td>
            <td>34.2</td>
            <td>37.7</td>
            <td>55.9</td>
            <td>37.4</td>
            <td>35.6</td>
            <td>54.0</td>
            <td>35.5</td>
            <td>34.1</td>
        </tr>
        <tr>
            <td>BEVFusionL</td>
            <td>52.5</td>
            <td>31.9</td>
            <td>32.2</td>
            <td>49.3</td>
            <td>29.0</td>
            <td>29.5</td>
            <td>51.0</td>
            <td>21.7</td>
            <td>27.9</td>
            <td>49.2</td>
            <td>27.0</td>
            <td>26.7</td>
        </tr>
        <tr>
            <td>FSTR</td>
            <td>55.3</td>
            <td>27.7</td>
            <td>29.3</td>
            <td>51.9</td>
            <td>30.2</td>
            <td>33.0</td>
            <td>55.7</td>
            <td>29.4</td>
            <td>33.8</td>
            <td>52.8</td>
            <td>30.3</td>
            <td>31.3</td>
        </tr>
        <tr class="highlight">
            <td><strong>Average</strong></td>
            <td>52.5</td>
            <td>26.9</td>
            <td>29.4</td>
            <td>49.7</td>
            <td>28.9</td>
            <td>32.0</td>
            <td>52.2</td>
            <td>28.2</td>
            <td>31.6</td>
            <td>50.0</td>
            <td>28.4</td>
            <td>29.8</td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <th rowspan="2"><strong>Method</strong></th>
            <th colspan="3"><strong>Trapezoid</strong></th>
            <th colspan="3"><strong>Line-Roll</strong></th>
            <th colspan="3"><strong>Pyramid-Roll</strong></th>
            <th colspan="3" class="place3d_blue"><strong>Ours</strong></th>
        </tr>
        <tr>
            <th>Car</th>
            <th>Ped</th>
            <th>Bicy</th>
            <th>Car</th>
            <th>Ped</th>
            <th>Bicy</th>
            <th>Car</th>
            <th>Ped</th>
            <th>Bicy</th>
            <th>Car</th>
            <th>Ped</th>
            <th>Bicy</th>
        </tr>
        <tr>
            <td>PointPillars</td>
            <td>43.5</td>
            <td>21.5</td>
            <td>27.3</td>
            <td>44.6</td>
            <td>21.3</td>
            <td>27.0</td>
            <td>46.1</td>
            <td>23.6</td>
            <td>27.9</td>
            <td>46.8</td>
            <td>24.9</td>
            <td>27.2</td>
        </tr>
        <tr>
            <td>CenterPoint</td>
            <td>55.4</td>
            <td>35.6</td>
            <td>37.5</td>
            <td>55.2</td>
            <td>32.7</td>
            <td>37.2</td>
            <td>56.2</td>
            <td>36.5</td>
            <td>35.9</td>
            <td>57.1</td>
            <td>34.4</td>
            <td>37.3</td>
        </tr>
        <tr>
            <td>BEVFusionL</td>
            <td>50.2</td>
            <td>30.0</td>
            <td>31.7</td>
            <td>50.8</td>
            <td>29.4</td>
            <td>29.5</td>
            <td>50.7</td>
            <td>22.7</td>
            <td>28.2</td>
            <td>53.0</td>
            <td>28.7</td>
            <td>29.5</td>
        </tr>
        <tr>
            <td>FSTR</td>
            <td>54.6</td>
            <td>30.0</td>
            <td>33.3</td>
            <td>53.5</td>
            <td>29.8</td>
            <td>32.4</td>
            <td>55.5</td>
            <td>29.9</td>
            <td>32.0</td>
            <td>56.6</td>
            <td>31.9</td>
            <td>34.1</td>
        </tr>
        <tr class="highlight">
            <td><strong>Average</strong></td>
            <td>50.9</td>
            <td>29.3</td>
            <td>32.5</td>
            <td>51.0</td>
            <td>28.3</td>
            <td>31.5</td>
            <td>52.1</td>
            <td>28.2</td>
            <td>31.0</td>
            <td>53.4</td>
            <td>30.0</td>
            <td>32.0</td>
        </tr>
    </tbody>
    </tfoot>
</table>


## :memo: TODO List
- [x] Initial release. 🚀
- [x] Add LiDAR placement benchmarks.
- [x] Add LiDAR placement datasets.
- [x] Add acknowledgments.
- [x] Add citations.
- [ ] Add more 3D perception models.



## Citation
If you find this work helpful for your research, please kindly consider citing our papers:

```bibtex
@article{li2024your,
  title={Is your lidar placement optimized for 3d scene understanding?},
  author={Li, Ye and Kong, Lingdong and Hu, Hanjiang and Xu, Xiaohao and Huang, Xiaonan},
  journal={Advances in Neural Information Processing Systems},
  volume={37},
  pages={34980--35017},
  year={2024}
}
```
```bibtex
@misc{mmdet3d,
    title = {MMDetection3D: OpenMMLab Next-Generation Platform for General 3D Object Detection},
    author = {MMDetection3D Contributors},
    howpublished = {\url{https://github.com/open-mmlab/mmdetection3d}},
    year = {2020}
}
```


## License

Place3D specific code is distributed under the MIT License.


## Acknowledgements

This work is developed based on the [MMDetection3D](https://github.com/open-mmlab/mmdetection3d) codebase.

> <img src="https://github.com/open-mmlab/mmdetection3d/blob/main/resources/mmdet3d-logo.png" width="31%"/><br>
> MMDetection3D is an open-source toolbox based on PyTorch, towards the next-generation platform for general 3D perception. It is a part of the OpenMMLab project developed by MMLab.

We acknowledge the use of the following public resources, during the course of this work: <sup>1</sup>[CARLA](https://github.com/carla-simulator/carla), <sup>2</sup>[nuScenes-devkit](https://github.com/nutonomy/nuscenes-devkit), <sup>3</sup>[SemanticKITTI-API](), <sup>4</sup>[MinkowskiEngine](https://github.com/NVIDIA/MinkowskiEngine), <sup>5</sup>[TorchSparse](https://github.com/mit-han-lab/torchsparse), <sup>6</sup>[Open3D-ML](https://github.com/isl-org/Open3D-ML), and <sup>7</sup>[Robo3D](https://github.com/ldkong1205/Robo3D).

We thank the exceptional contributions from the above open-source repositories! :heart:





