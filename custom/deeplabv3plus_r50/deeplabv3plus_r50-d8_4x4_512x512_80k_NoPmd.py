_base_ = [
    './deeplabv3plus_r50-d8.py',
    '../base/bmc_dataset_512x512_NoPMD.py',
    '../base/default_runtime.py',
    '../base/schedule_100e.py'
]
model = dict(
    decode_head=dict(num_classes=6), auxiliary_head=dict(num_classes=6))
