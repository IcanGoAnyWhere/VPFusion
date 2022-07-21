python test.py --cfg_file /home/xrd/Documents/OpenPCDet/tools/cfgs/kitti_models/pv_rcnn.yaml --batch_size 2 --ckpt  ../pv_rcnn_8369.pth


python train.py --cfg_file /home/xrd/Documents/OpenPCDet/tools/cfgs/kitti_models/pv_rcnn.yaml

python demo.py --cfg_file cfgs/kitti_models/VPfusion.yaml \
    --ckpt ../output/kitti_models/VPfusion/default/ckpt/checkpoint_epoch_120.pth \
    --data_path ../data/kitti


python -m pcdet.datasets.nuscenes.nuscenes_dataset --func create_nuscenes_infos \
    --cfg_file tools/cfgs/dataset_configs/nuscenes_dataset_LI.yaml \
    --version v1.0-mini

tensorboard --logdir=/home/xrd/PycharmProjects/VPFusion/OpenPCDet/output/kitti_models/VPfusionRCNN_kitti/default/tensorboard --port 8123