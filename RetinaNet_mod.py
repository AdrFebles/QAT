# GENETARED BY NNDCT, DO NOT EDIT!

import torch
import pytorch_nndct as py_nndct
class RetinaNet_mod(torch.nn.Module):
    def __init__(self):
        super(RetinaNet_mod, self).__init__()
        self.module_0 = py_nndct.nn.Input() #RetinaNet_mod::input_0
        self.module_1 = py_nndct.nn.quant_input() #RetinaNet_mod::RetinaNet_mod/QuantStub[quant_stub]/input.1
        self.module_2 = py_nndct.nn.Conv2d(in_channels=3, out_channels=64, kernel_size=[7, 7], stride=[2, 2], padding=[3, 3], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Conv2d[conv1]/input.2
        self.module_4 = py_nndct.nn.ReLU(inplace=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/ReLU[relu]/11955
        self.module_5 = py_nndct.nn.MaxPool2d(kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], ceil_mode=False) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/MaxPool2d[maxpool]/input.4
        self.module_6 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer1]/BasicBlock[0]/Conv2d[conv1]/input.5
        self.module_8 = py_nndct.nn.ReLU(inplace=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer1]/BasicBlock[0]/ReLU[relu]/input.7
        self.module_9 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer1]/BasicBlock[0]/Conv2d[conv2]/input.8
        self.module_11 = py_nndct.nn.Add() #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer1]/BasicBlock[0]/input.9
        self.module_12 = py_nndct.nn.ReLU(inplace=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer1]/BasicBlock[0]/ReLU[relu]/input.10
        self.module_13 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer1]/BasicBlock[1]/Conv2d[conv1]/input.11
        self.module_15 = py_nndct.nn.ReLU(inplace=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer1]/BasicBlock[1]/ReLU[relu]/input.13
        self.module_16 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer1]/BasicBlock[1]/Conv2d[conv2]/input.14
        self.module_18 = py_nndct.nn.Add() #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer1]/BasicBlock[1]/input.15
        self.module_19 = py_nndct.nn.ReLU(inplace=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer1]/BasicBlock[1]/ReLU[relu]/input.16
        self.module_20 = py_nndct.nn.Conv2d(in_channels=64, out_channels=128, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer2]/BasicBlock[0]/Conv2d[conv1]/input.17
        self.module_22 = py_nndct.nn.ReLU(inplace=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer2]/BasicBlock[0]/ReLU[relu]/input.19
        self.module_23 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer2]/BasicBlock[0]/Conv2d[conv2]/input.20
        self.module_25 = py_nndct.nn.Conv2d(in_channels=64, out_channels=128, kernel_size=[1, 1], stride=[2, 2], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer2]/BasicBlock[0]/Sequential[downsample]/Conv2d[0]/input.21
        self.module_27 = py_nndct.nn.Add() #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer2]/BasicBlock[0]/input.22
        self.module_28 = py_nndct.nn.ReLU(inplace=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer2]/BasicBlock[0]/ReLU[relu]/input.23
        self.module_29 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer2]/BasicBlock[1]/Conv2d[conv1]/input.24
        self.module_31 = py_nndct.nn.ReLU(inplace=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer2]/BasicBlock[1]/ReLU[relu]/input.26
        self.module_32 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer2]/BasicBlock[1]/Conv2d[conv2]/input.27
        self.module_34 = py_nndct.nn.Add() #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer2]/BasicBlock[1]/input.28
        self.module_35 = py_nndct.nn.ReLU(inplace=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer2]/BasicBlock[1]/ReLU[relu]/input.29
        self.module_36 = py_nndct.nn.Conv2d(in_channels=128, out_channels=256, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer3]/BasicBlock[0]/Conv2d[conv1]/input.30
        self.module_38 = py_nndct.nn.ReLU(inplace=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer3]/BasicBlock[0]/ReLU[relu]/input.32
        self.module_39 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer3]/BasicBlock[0]/Conv2d[conv2]/input.33
        self.module_41 = py_nndct.nn.Conv2d(in_channels=128, out_channels=256, kernel_size=[1, 1], stride=[2, 2], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer3]/BasicBlock[0]/Sequential[downsample]/Conv2d[0]/input.34
        self.module_43 = py_nndct.nn.Add() #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer3]/BasicBlock[0]/input.35
        self.module_44 = py_nndct.nn.ReLU(inplace=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer3]/BasicBlock[0]/ReLU[relu]/input.36
        self.module_45 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer3]/BasicBlock[1]/Conv2d[conv1]/input.37
        self.module_47 = py_nndct.nn.ReLU(inplace=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer3]/BasicBlock[1]/ReLU[relu]/input.39
        self.module_48 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer3]/BasicBlock[1]/Conv2d[conv2]/input.40
        self.module_50 = py_nndct.nn.Add() #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer3]/BasicBlock[1]/input.41
        self.module_51 = py_nndct.nn.ReLU(inplace=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer3]/BasicBlock[1]/ReLU[relu]/input.42
        self.module_52 = py_nndct.nn.Conv2d(in_channels=256, out_channels=512, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer4]/BasicBlock[0]/Conv2d[conv1]/input.43
        self.module_54 = py_nndct.nn.ReLU(inplace=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer4]/BasicBlock[0]/ReLU[relu]/input.45
        self.module_55 = py_nndct.nn.Conv2d(in_channels=512, out_channels=512, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer4]/BasicBlock[0]/Conv2d[conv2]/input.46
        self.module_57 = py_nndct.nn.Conv2d(in_channels=256, out_channels=512, kernel_size=[1, 1], stride=[2, 2], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer4]/BasicBlock[0]/Sequential[downsample]/Conv2d[0]/input.47
        self.module_59 = py_nndct.nn.Add() #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer4]/BasicBlock[0]/input.48
        self.module_60 = py_nndct.nn.ReLU(inplace=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer4]/BasicBlock[0]/ReLU[relu]/input.49
        self.module_61 = py_nndct.nn.Conv2d(in_channels=512, out_channels=512, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer4]/BasicBlock[1]/Conv2d[conv1]/input.50
        self.module_63 = py_nndct.nn.ReLU(inplace=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer4]/BasicBlock[1]/ReLU[relu]/input.52
        self.module_64 = py_nndct.nn.Conv2d(in_channels=512, out_channels=512, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer4]/BasicBlock[1]/Conv2d[conv2]/input.53
        self.module_66 = py_nndct.nn.Add() #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer4]/BasicBlock[1]/input.54
        self.module_67 = py_nndct.nn.ReLU(inplace=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/IntermediateLayerGetter[body]/Sequential[layer4]/BasicBlock[1]/ReLU[relu]/input.55
        self.module_68 = py_nndct.nn.Conv2d(in_channels=512, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/FeaturePyramidNetwork[fpn]/Conv2d[inner_blocks]/ModuleList[2]/input.56
        self.module_69 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/FeaturePyramidNetwork[fpn]/Conv2d[layer_blocks]/ModuleList[2]/input.77
        self.module_70 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/FeaturePyramidNetwork[fpn]/Conv2d[inner_blocks]/ModuleList[1]/12984
        self.module_71 = py_nndct.nn.Module('shape') #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/FeaturePyramidNetwork[fpn]/12998
        self.module_72 = py_nndct.nn.Module('shape') #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/FeaturePyramidNetwork[fpn]/13002
        self.module_73 = py_nndct.nn.Interpolate() #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/FeaturePyramidNetwork[fpn]/Interpolate[interpolate]/13007
        self.module_74 = py_nndct.nn.Add() #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/FeaturePyramidNetwork[fpn]/Add[add]/input.57
        self.module_75 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/FeaturePyramidNetwork[fpn]/Conv2d[layer_blocks]/ModuleList[1]/input.68
        self.module_76 = py_nndct.nn.Conv2d(in_channels=128, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/FeaturePyramidNetwork[fpn]/Conv2d[inner_blocks]/ModuleList[0]/13280
        self.module_77 = py_nndct.nn.Module('shape') #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/FeaturePyramidNetwork[fpn]/13297
        self.module_78 = py_nndct.nn.Module('shape') #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/FeaturePyramidNetwork[fpn]/13301
        self.module_79 = py_nndct.nn.Interpolate() #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/FeaturePyramidNetwork[fpn]/Interpolate[interpolate]/13306
        self.module_80 = py_nndct.nn.Add() #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/FeaturePyramidNetwork[fpn]/Add[add]/input.58
        self.module_81 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/FeaturePyramidNetwork[fpn]/Conv2d[layer_blocks]/ModuleList[0]/input.59
        self.module_82 = py_nndct.nn.MaxPool2d(kernel_size=[1, 1], stride=[2, 2], padding=[0, 0], dilation=[1, 1], ceil_mode=False) #RetinaNet_mod::RetinaNet_mod/BackboneWithFPN[backbone]/FeaturePyramidNetwork[fpn]/LastLevelMaxPool[extra_blocks]/MaxPool2d[maxpool]/input.86
        self.module_83 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/Conv2d[0]/input.60
        self.module_84 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/ReLU[1]/input.61
        self.module_85 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/Conv2d[2]/input.62
        self.module_86 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/ReLU[3]/input.63
        self.module_87 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/Conv2d[4]/input.64
        self.module_88 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/ReLU[5]/input.65
        self.module_89 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/Conv2d[6]/input.66
        self.module_90 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/ReLU[7]/input.67
        self.module_91 = py_nndct.nn.Conv2d(in_channels=256, out_channels=18, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Conv2d[cls_logits]/13626
        self.module_92 = py_nndct.nn.Module('shape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/13628
        self.module_93 = py_nndct.nn.Module('shape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/13636
        self.module_94 = py_nndct.nn.Module('shape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/13640
        self.module_95 = py_nndct.nn.Module('reshape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/13646
        self.module_96 = py_nndct.nn.Module('permute') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/13653
        self.module_97 = py_nndct.nn.Module('reshape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/13657
        self.module_98 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/Conv2d[0]/input.69
        self.module_99 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/ReLU[1]/input.70
        self.module_100 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/Conv2d[2]/input.71
        self.module_101 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/ReLU[3]/input.72
        self.module_102 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/Conv2d[4]/input.73
        self.module_103 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/ReLU[5]/input.74
        self.module_104 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/Conv2d[6]/input.75
        self.module_105 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/ReLU[7]/input.76
        self.module_106 = py_nndct.nn.Conv2d(in_channels=256, out_channels=18, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Conv2d[cls_logits]/13756
        self.module_107 = py_nndct.nn.Module('shape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/13758
        self.module_108 = py_nndct.nn.Module('shape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/13766
        self.module_109 = py_nndct.nn.Module('shape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/13770
        self.module_110 = py_nndct.nn.Module('reshape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/13776
        self.module_111 = py_nndct.nn.Module('permute') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/13783
        self.module_112 = py_nndct.nn.Module('reshape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/13787
        self.module_113 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/Conv2d[0]/input.78
        self.module_114 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/ReLU[1]/input.79
        self.module_115 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/Conv2d[2]/input.80
        self.module_116 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/ReLU[3]/input.81
        self.module_117 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/Conv2d[4]/input.82
        self.module_118 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/ReLU[5]/input.83
        self.module_119 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/Conv2d[6]/input.84
        self.module_120 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/ReLU[7]/input.85
        self.module_121 = py_nndct.nn.Conv2d(in_channels=256, out_channels=18, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Conv2d[cls_logits]/13886
        self.module_122 = py_nndct.nn.Module('shape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/13888
        self.module_123 = py_nndct.nn.Module('shape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/13896
        self.module_124 = py_nndct.nn.Module('shape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/13900
        self.module_125 = py_nndct.nn.Module('reshape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/13906
        self.module_126 = py_nndct.nn.Module('permute') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/13913
        self.module_127 = py_nndct.nn.Module('reshape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/13917
        self.module_128 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/Conv2d[0]/input.87
        self.module_129 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/ReLU[1]/input.88
        self.module_130 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/Conv2d[2]/input.89
        self.module_131 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/ReLU[3]/input.90
        self.module_132 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/Conv2d[4]/input.91
        self.module_133 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/ReLU[5]/input.92
        self.module_134 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/Conv2d[6]/input.93
        self.module_135 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Sequential[conv]/ReLU[7]/input.94
        self.module_136 = py_nndct.nn.Conv2d(in_channels=256, out_channels=18, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Conv2d[cls_logits]/14016
        self.module_137 = py_nndct.nn.Module('shape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/14018
        self.module_138 = py_nndct.nn.Module('shape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/14026
        self.module_139 = py_nndct.nn.Module('shape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/14030
        self.module_140 = py_nndct.nn.Module('reshape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/14036
        self.module_141 = py_nndct.nn.Module('permute') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/14043
        self.module_142 = py_nndct.nn.Module('reshape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/14047
        self.module_143 = py_nndct.nn.Cat() #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetClassificationHead_mod[classification_head]/Cat[cat]/ip.1
        self.module_144 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/Conv2d[0]/input.95
        self.module_145 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/ReLU[1]/input.96
        self.module_146 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/Conv2d[2]/input.97
        self.module_147 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/ReLU[3]/input.98
        self.module_148 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/Conv2d[4]/input.99
        self.module_149 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/ReLU[5]/input.100
        self.module_150 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/Conv2d[6]/input.101
        self.module_151 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/ReLU[7]/input.102
        self.module_152 = py_nndct.nn.Conv2d(in_channels=256, out_channels=36, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Conv2d[bbox_reg]/14149
        self.module_153 = py_nndct.nn.Module('shape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/14151
        self.module_154 = py_nndct.nn.Module('shape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/14159
        self.module_155 = py_nndct.nn.Module('shape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/14163
        self.module_156 = py_nndct.nn.Module('reshape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/14169
        self.module_157 = py_nndct.nn.Module('permute') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/14176
        self.module_158 = py_nndct.nn.Module('reshape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/14180
        self.module_159 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/Conv2d[0]/input.103
        self.module_160 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/ReLU[1]/input.104
        self.module_161 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/Conv2d[2]/input.105
        self.module_162 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/ReLU[3]/input.106
        self.module_163 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/Conv2d[4]/input.107
        self.module_164 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/ReLU[5]/input.108
        self.module_165 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/Conv2d[6]/input.109
        self.module_166 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/ReLU[7]/input.110
        self.module_167 = py_nndct.nn.Conv2d(in_channels=256, out_channels=36, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Conv2d[bbox_reg]/14279
        self.module_168 = py_nndct.nn.Module('shape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/14281
        self.module_169 = py_nndct.nn.Module('shape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/14289
        self.module_170 = py_nndct.nn.Module('shape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/14293
        self.module_171 = py_nndct.nn.Module('reshape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/14299
        self.module_172 = py_nndct.nn.Module('permute') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/14306
        self.module_173 = py_nndct.nn.Module('reshape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/14310
        self.module_174 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/Conv2d[0]/input.111
        self.module_175 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/ReLU[1]/input.112
        self.module_176 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/Conv2d[2]/input.113
        self.module_177 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/ReLU[3]/input.114
        self.module_178 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/Conv2d[4]/input.115
        self.module_179 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/ReLU[5]/input.116
        self.module_180 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/Conv2d[6]/input.117
        self.module_181 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/ReLU[7]/input.118
        self.module_182 = py_nndct.nn.Conv2d(in_channels=256, out_channels=36, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Conv2d[bbox_reg]/14409
        self.module_183 = py_nndct.nn.Module('shape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/14411
        self.module_184 = py_nndct.nn.Module('shape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/14419
        self.module_185 = py_nndct.nn.Module('shape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/14423
        self.module_186 = py_nndct.nn.Module('reshape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/14429
        self.module_187 = py_nndct.nn.Module('permute') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/14436
        self.module_188 = py_nndct.nn.Module('reshape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/14440
        self.module_189 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/Conv2d[0]/input.119
        self.module_190 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/ReLU[1]/input.120
        self.module_191 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/Conv2d[2]/input.121
        self.module_192 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/ReLU[3]/input.122
        self.module_193 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/Conv2d[4]/input.123
        self.module_194 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/ReLU[5]/input.124
        self.module_195 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/Conv2d[6]/input.125
        self.module_196 = py_nndct.nn.ReLU(inplace=False) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Sequential[conv]/ReLU[7]/input
        self.module_197 = py_nndct.nn.Conv2d(in_channels=256, out_channels=36, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Conv2d[bbox_reg]/14539
        self.module_198 = py_nndct.nn.Module('shape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/14541
        self.module_199 = py_nndct.nn.Module('shape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/14549
        self.module_200 = py_nndct.nn.Module('shape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/14553
        self.module_201 = py_nndct.nn.Module('reshape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/14559
        self.module_202 = py_nndct.nn.Module('permute') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/14566
        self.module_203 = py_nndct.nn.Module('reshape') #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/14570
        self.module_204 = py_nndct.nn.Cat() #RetinaNet_mod::RetinaNet_mod/RetinaNetHead_mod[head]/RetinaNetRegressionHead_mod[regression_head]/Cat[cat]/ip
        self.module_205 = py_nndct.nn.dequant_output() #RetinaNet_mod::RetinaNet_mod/DeQuantStub[dequant_stub]/14577
        self.module_206 = py_nndct.nn.dequant_output() #RetinaNet_mod::RetinaNet_mod/DeQuantStub[dequant_stub]/14579
        self.module_207 = py_nndct.nn.dequant_output() #RetinaNet_mod::RetinaNet_mod/DeQuantStub[dequant_stub]/14584
        self.module_208 = py_nndct.nn.dequant_output() #RetinaNet_mod::RetinaNet_mod/DeQuantStub[dequant_stub]/14586
        self.module_209 = py_nndct.nn.dequant_output() #RetinaNet_mod::RetinaNet_mod/DeQuantStub[dequant_stub]/14588
        self.module_210 = py_nndct.nn.dequant_output() #RetinaNet_mod::RetinaNet_mod/DeQuantStub[dequant_stub]/14590

    def forward(self, *args):
        output_module_0 = self.module_0(input=args[0])
        output_module_0 = self.module_1(input=output_module_0)
        output_module_0 = self.module_2(output_module_0)
        output_module_0 = self.module_4(output_module_0)
        output_module_0 = self.module_5(output_module_0)
        output_module_6 = self.module_6(output_module_0)
        output_module_6 = self.module_8(output_module_6)
        output_module_6 = self.module_9(output_module_6)
        output_module_6 = self.module_11(input=output_module_6, other=output_module_0, alpha=1)
        output_module_6 = self.module_12(output_module_6)
        output_module_13 = self.module_13(output_module_6)
        output_module_13 = self.module_15(output_module_13)
        output_module_13 = self.module_16(output_module_13)
        output_module_13 = self.module_18(input=output_module_13, other=output_module_6, alpha=1)
        output_module_13 = self.module_19(output_module_13)
        output_module_20 = self.module_20(output_module_13)
        output_module_20 = self.module_22(output_module_20)
        output_module_20 = self.module_23(output_module_20)
        output_module_25 = self.module_25(output_module_13)
        output_module_20 = self.module_27(input=output_module_20, other=output_module_25, alpha=1)
        output_module_20 = self.module_28(output_module_20)
        output_module_29 = self.module_29(output_module_20)
        output_module_29 = self.module_31(output_module_29)
        output_module_29 = self.module_32(output_module_29)
        output_module_29 = self.module_34(input=output_module_29, other=output_module_20, alpha=1)
        output_module_29 = self.module_35(output_module_29)
        output_module_36 = self.module_36(output_module_29)
        output_module_36 = self.module_38(output_module_36)
        output_module_36 = self.module_39(output_module_36)
        output_module_41 = self.module_41(output_module_29)
        output_module_36 = self.module_43(input=output_module_36, other=output_module_41, alpha=1)
        output_module_36 = self.module_44(output_module_36)
        output_module_45 = self.module_45(output_module_36)
        output_module_45 = self.module_47(output_module_45)
        output_module_45 = self.module_48(output_module_45)
        output_module_45 = self.module_50(input=output_module_45, other=output_module_36, alpha=1)
        output_module_45 = self.module_51(output_module_45)
        output_module_52 = self.module_52(output_module_45)
        output_module_52 = self.module_54(output_module_52)
        output_module_52 = self.module_55(output_module_52)
        output_module_57 = self.module_57(output_module_45)
        output_module_52 = self.module_59(input=output_module_52, other=output_module_57, alpha=1)
        output_module_52 = self.module_60(output_module_52)
        output_module_61 = self.module_61(output_module_52)
        output_module_61 = self.module_63(output_module_61)
        output_module_61 = self.module_64(output_module_61)
        output_module_61 = self.module_66(input=output_module_61, other=output_module_52, alpha=1)
        output_module_61 = self.module_67(output_module_61)
        output_module_61 = self.module_68(output_module_61)
        output_module_69 = self.module_69(output_module_61)
        output_module_70 = self.module_70(output_module_45)
        output_module_71 = self.module_71(input=output_module_70, dim=2)
        output_module_72 = self.module_72(input=output_module_70, dim=3)
        output_module_73 = self.module_73(input=output_module_61, size=[output_module_71,output_module_72], scale_factor=None, mode='nearest')
        output_module_74 = self.module_74(input=output_module_70, other=output_module_73, alpha=1)
        output_module_75 = self.module_75(output_module_74)
        output_module_76 = self.module_76(output_module_29)
        output_module_77 = self.module_77(input=output_module_76, dim=2)
        output_module_78 = self.module_78(input=output_module_76, dim=3)
        output_module_79 = self.module_79(input=output_module_74, size=[output_module_77,output_module_78], scale_factor=None, mode='nearest')
        output_module_80 = self.module_80(input=output_module_76, other=output_module_79, alpha=1)
        output_module_80 = self.module_81(output_module_80)
        output_module_82 = self.module_82(output_module_69)
        output_module_83 = self.module_83(output_module_80)
        output_module_83 = self.module_84(output_module_83)
        output_module_83 = self.module_85(output_module_83)
        output_module_83 = self.module_86(output_module_83)
        output_module_83 = self.module_87(output_module_83)
        output_module_83 = self.module_88(output_module_83)
        output_module_83 = self.module_89(output_module_83)
        output_module_83 = self.module_90(output_module_83)
        output_module_83 = self.module_91(output_module_83)
        output_module_92 = self.module_92(input=output_module_83, dim=0)
        output_module_93 = self.module_93(input=output_module_83, dim=2)
        output_module_94 = self.module_94(input=output_module_83, dim=3)
        output_module_95 = self.module_95(input=output_module_83, shape=[output_module_92,-1,2,output_module_93,output_module_94])
        output_module_95 = self.module_96(dims=[0,3,4,1,2], input=output_module_95)
        output_module_95 = self.module_97(input=output_module_95, shape=[output_module_92,-1,2])
        output_module_98 = self.module_98(output_module_75)
        output_module_98 = self.module_99(output_module_98)
        output_module_98 = self.module_100(output_module_98)
        output_module_98 = self.module_101(output_module_98)
        output_module_98 = self.module_102(output_module_98)
        output_module_98 = self.module_103(output_module_98)
        output_module_98 = self.module_104(output_module_98)
        output_module_98 = self.module_105(output_module_98)
        output_module_98 = self.module_106(output_module_98)
        output_module_107 = self.module_107(input=output_module_98, dim=0)
        output_module_108 = self.module_108(input=output_module_98, dim=2)
        output_module_109 = self.module_109(input=output_module_98, dim=3)
        output_module_110 = self.module_110(input=output_module_98, shape=[output_module_107,-1,2,output_module_108,output_module_109])
        output_module_110 = self.module_111(dims=[0,3,4,1,2], input=output_module_110)
        output_module_110 = self.module_112(input=output_module_110, shape=[output_module_107,-1,2])
        output_module_113 = self.module_113(output_module_69)
        output_module_113 = self.module_114(output_module_113)
        output_module_113 = self.module_115(output_module_113)
        output_module_113 = self.module_116(output_module_113)
        output_module_113 = self.module_117(output_module_113)
        output_module_113 = self.module_118(output_module_113)
        output_module_113 = self.module_119(output_module_113)
        output_module_113 = self.module_120(output_module_113)
        output_module_113 = self.module_121(output_module_113)
        output_module_122 = self.module_122(input=output_module_113, dim=0)
        output_module_123 = self.module_123(input=output_module_113, dim=2)
        output_module_124 = self.module_124(input=output_module_113, dim=3)
        output_module_125 = self.module_125(input=output_module_113, shape=[output_module_122,-1,2,output_module_123,output_module_124])
        output_module_125 = self.module_126(dims=[0,3,4,1,2], input=output_module_125)
        output_module_125 = self.module_127(input=output_module_125, shape=[output_module_122,-1,2])
        output_module_128 = self.module_128(output_module_82)
        output_module_128 = self.module_129(output_module_128)
        output_module_128 = self.module_130(output_module_128)
        output_module_128 = self.module_131(output_module_128)
        output_module_128 = self.module_132(output_module_128)
        output_module_128 = self.module_133(output_module_128)
        output_module_128 = self.module_134(output_module_128)
        output_module_128 = self.module_135(output_module_128)
        output_module_128 = self.module_136(output_module_128)
        output_module_137 = self.module_137(input=output_module_128, dim=0)
        output_module_138 = self.module_138(input=output_module_128, dim=2)
        output_module_139 = self.module_139(input=output_module_128, dim=3)
        output_module_140 = self.module_140(input=output_module_128, shape=[output_module_137,-1,2,output_module_138,output_module_139])
        output_module_140 = self.module_141(dims=[0,3,4,1,2], input=output_module_140)
        output_module_140 = self.module_142(input=output_module_140, shape=[output_module_137,-1,2])
        output_module_95 = self.module_143(dim=1, tensors=[output_module_95,output_module_110,output_module_125,output_module_140])
        output_module_144 = self.module_144(output_module_80)
        output_module_144 = self.module_145(output_module_144)
        output_module_144 = self.module_146(output_module_144)
        output_module_144 = self.module_147(output_module_144)
        output_module_144 = self.module_148(output_module_144)
        output_module_144 = self.module_149(output_module_144)
        output_module_144 = self.module_150(output_module_144)
        output_module_144 = self.module_151(output_module_144)
        output_module_144 = self.module_152(output_module_144)
        output_module_153 = self.module_153(input=output_module_144, dim=0)
        output_module_154 = self.module_154(input=output_module_144, dim=2)
        output_module_155 = self.module_155(input=output_module_144, dim=3)
        output_module_156 = self.module_156(input=output_module_144, shape=[output_module_153,-1,4,output_module_154,output_module_155])
        output_module_156 = self.module_157(dims=[0,3,4,1,2], input=output_module_156)
        output_module_156 = self.module_158(input=output_module_156, shape=[output_module_153,-1,4])
        output_module_159 = self.module_159(output_module_75)
        output_module_159 = self.module_160(output_module_159)
        output_module_159 = self.module_161(output_module_159)
        output_module_159 = self.module_162(output_module_159)
        output_module_159 = self.module_163(output_module_159)
        output_module_159 = self.module_164(output_module_159)
        output_module_159 = self.module_165(output_module_159)
        output_module_159 = self.module_166(output_module_159)
        output_module_159 = self.module_167(output_module_159)
        output_module_168 = self.module_168(input=output_module_159, dim=0)
        output_module_169 = self.module_169(input=output_module_159, dim=2)
        output_module_170 = self.module_170(input=output_module_159, dim=3)
        output_module_171 = self.module_171(input=output_module_159, shape=[output_module_168,-1,4,output_module_169,output_module_170])
        output_module_171 = self.module_172(dims=[0,3,4,1,2], input=output_module_171)
        output_module_171 = self.module_173(input=output_module_171, shape=[output_module_168,-1,4])
        output_module_174 = self.module_174(output_module_69)
        output_module_174 = self.module_175(output_module_174)
        output_module_174 = self.module_176(output_module_174)
        output_module_174 = self.module_177(output_module_174)
        output_module_174 = self.module_178(output_module_174)
        output_module_174 = self.module_179(output_module_174)
        output_module_174 = self.module_180(output_module_174)
        output_module_174 = self.module_181(output_module_174)
        output_module_174 = self.module_182(output_module_174)
        output_module_183 = self.module_183(input=output_module_174, dim=0)
        output_module_184 = self.module_184(input=output_module_174, dim=2)
        output_module_185 = self.module_185(input=output_module_174, dim=3)
        output_module_186 = self.module_186(input=output_module_174, shape=[output_module_183,-1,4,output_module_184,output_module_185])
        output_module_186 = self.module_187(dims=[0,3,4,1,2], input=output_module_186)
        output_module_186 = self.module_188(input=output_module_186, shape=[output_module_183,-1,4])
        output_module_189 = self.module_189(output_module_82)
        output_module_189 = self.module_190(output_module_189)
        output_module_189 = self.module_191(output_module_189)
        output_module_189 = self.module_192(output_module_189)
        output_module_189 = self.module_193(output_module_189)
        output_module_189 = self.module_194(output_module_189)
        output_module_189 = self.module_195(output_module_189)
        output_module_189 = self.module_196(output_module_189)
        output_module_189 = self.module_197(output_module_189)
        output_module_198 = self.module_198(input=output_module_189, dim=0)
        output_module_199 = self.module_199(input=output_module_189, dim=2)
        output_module_200 = self.module_200(input=output_module_189, dim=3)
        output_module_201 = self.module_201(input=output_module_189, shape=[output_module_198,-1,4,output_module_199,output_module_200])
        output_module_201 = self.module_202(dims=[0,3,4,1,2], input=output_module_201)
        output_module_201 = self.module_203(input=output_module_201, shape=[output_module_198,-1,4])
        output_module_156 = self.module_204(dim=1, tensors=[output_module_156,output_module_171,output_module_186,output_module_201])
        output_module_95 = self.module_205(input=output_module_95)
        output_module_156 = self.module_206(input=output_module_156)
        output_module_207 = self.module_207(input=output_module_80)
        output_module_208 = self.module_208(input=output_module_75)
        output_module_209 = self.module_209(input=output_module_69)
        output_module_210 = self.module_210(input=output_module_82)
        return output_module_95,output_module_156,output_module_207,output_module_208,output_module_209,output_module_210
