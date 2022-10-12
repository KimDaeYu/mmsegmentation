_base_ = [
    './lraspp_m-v3-d8.py',
    '../base/bmc_dataset_1024x512.py',
    '../base/default_runtime.py',
    '../base/schedule_100e.py'
]

model = dict(pretrained='open-mmlab://contrib/mobilenet_v3_large')

data = dict(samples_per_gpu=1, workers_per_gpu=1)
