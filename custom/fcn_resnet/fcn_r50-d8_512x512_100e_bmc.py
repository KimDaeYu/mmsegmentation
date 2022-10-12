_base_ = [
    './fcn_r50-d8.py',
    '../base/bmc_dataset_512x512.py',
    '../base/default_runtime.py',
    '../base/schedule_100e.py'
]

checkpoint = "open-mmlab://resnet50_v1c"

model = dict(pretrained=checkpoint,decode_head=dict(num_classes=150))

data = dict(samples_per_gpu=2, workers_per_gpu=2)
