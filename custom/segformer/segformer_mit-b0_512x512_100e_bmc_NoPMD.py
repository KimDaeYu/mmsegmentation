_base_ = [
    './segformer_mit-b0.py',
    '../base/bmc_dataset_512x512_NoPMD.py',
    '../base/default_runtime.py',
    '../base/schedule_100e.py'
]

checkpoint = 'https://download.openmmlab.com/mmsegmentation/v0.5/pretrain/segformer/mit_b0_20220624-7e0fe6dd.pth'  # noqa

model = dict(pretrained=checkpoint, decode_head=dict(num_classes=150))

data = dict(samples_per_gpu=2, workers_per_gpu=2)
