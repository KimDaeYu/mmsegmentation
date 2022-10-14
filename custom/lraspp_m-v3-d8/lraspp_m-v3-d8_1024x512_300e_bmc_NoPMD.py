_base_ = [
    './lraspp_m-v3-d8.py',
    '../base/bmc_dataset_1024x512_NoPMD.py',
    '../base/default_runtime.py',
    '../base/schedule_300e.py'
]

model = dict(pretrained='open-mmlab://contrib/mobilenet_v3_large')

data = dict(samples_per_gpu=2, workers_per_gpu=2)
