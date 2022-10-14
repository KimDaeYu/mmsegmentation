_base_ = [
    './deeplabv3_r18-d8.py',
    '../base/bmc_dataset_512x512_NoPMD.py',
    '../base/default_runtime.py',
    '../base/schedule_300e.py'
]
model = dict(decode_head=dict(num_classes=150), auxiliary_head=dict(num_classes=150))

data = dict(samples_per_gpu=2, workers_per_gpu=2)