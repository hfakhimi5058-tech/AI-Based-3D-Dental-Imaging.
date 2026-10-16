ToothFairy2: 3D Dental CBCT Segmentation

Project Overview

This project explores 3D dental CBCT segmentation using a pretrained nnU-Net v2 model from the ToothFairy2 benchmark.

Dataset

- Input: ToothFairy2F_001_0000.mha
- Volume dimensions: 262 × 512 × 512 voxels
- Voxel spacing: approximately 0.3 mm
- Imaging modality: Dental cone-beam computed tomography (CBCT)

Model Configuration

- Framework: nnU-Net v2
- Configuration: "3d_fullres_resample_torch_256_bs8_ctnorm"
- Checkpoint: "checkpoint_final.pth"
- Inference environment: Google Colab with NVIDIA T4 GPU

Current Progress

The pretrained checkpoint was loaded successfully, and sliding-window inference reached 18/18 patches. However, the process terminated before a final segmentation file was saved.

A complete segmentation output and quantitative evaluation are not yet available.

Next Steps

- Resolve inference memory limitations.
- Generate and validate the final 3D segmentation.
- Visualize the segmentation overlaid on the original CBCT.
- Evaluate the results using appropriate segmentation metrics.

Reproducibility Note

This file documents the current experimental status. It does not claim successful segmentation or validated model performance.