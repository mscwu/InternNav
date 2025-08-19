from internnav.configs.agent import AgentCfg
from internnav.configs.evaluator import (
    EnvCfg,
    EvalCfg,
    EvalDatasetCfg,
    SceneCfg,
    TaskCfg,
)

eval_cfg = EvalCfg(
    agent=AgentCfg(
        server_port=8087,
        model_name='cma',
        ckpt_path='checkpoints/r2r/fine_tuned/cma',
        model_settings={},
    ),
    env=EnvCfg(
        env_type='vln_pe',
        env_settings={
            'use_fabric': False,
            'headless': True,
        },
    ),
    task=TaskCfg(
        task_name='cma_plus_eval',
        task_settings={
            'env_num': 2,
            'use_distributed': False,
            'proc_num': 2,
        },
        scene=SceneCfg(
            scene_type='mp3d',
            scene_data_dir='data/scene_data/mp3d_pe',
        ),
        robot_name='h1',
        robot_usd_path='data/Embodiments/vln-pe/h1/h1_vln_pointcloud.usd',
        camera_resolution=[256,256], # (W,H)
        camera_prim_path='torso_link/h1_pano_camera_0',
        vlnce=False,   # vlnpe by default
        obstacle_detection=False,   # whether allow flash across obstacle
    ),
    dataset=EvalDatasetCfg(
        dataset_type="mp3d",
        dataset_settings={
            'base_data_dir': 'data/vln_pe/raw_data/r2r',
            'split_data_types': ['val_unseen', 'val_seen'],
            'filter_stairs': False,
        },
    ),
    eval_settings={
        'save_to_json': False,
        'vis_output': True     
    }
)
