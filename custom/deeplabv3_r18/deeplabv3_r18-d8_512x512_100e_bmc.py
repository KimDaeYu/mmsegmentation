_base_ = [
    '../base/bmc_dataset_512x512.py',
    '../base/default_runtime.py',
    '../base/schedule_100e.py'
]
model = dict(
    pretrained='open-mmlab://resnet18_v1c',
    backbone=dict(depth=18),
    decode_head=dict(
        in_channels=512,
        channels=128,
    ),
    auxiliary_head=dict(in_channels=256, channels=64))
