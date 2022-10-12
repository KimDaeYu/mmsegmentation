_base_ = [
    './deeplabv3_r18-d8.py',
    '../base/bmc_dataset_512x512.py',
    '../base/default_runtime.py',
    '../base/schedule_100e.py'
]
model = dict(decode_head=dict(num_classes=150), auxiliary_head=dict(num_classes=150))
