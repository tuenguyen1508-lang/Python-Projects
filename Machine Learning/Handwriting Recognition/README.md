# ✍️ Handwritten Character Recognition with Classical ML and CNNs  

This project tackles handwritten character recognition on a 62-class dataset covering uppercase letters (A–Z), lowercase letters (a–z), and digits (0–9). The aim is to compare traditional machine-learning models with a modern convolutional neural network (CNN), then select and package a robust model for reuse. The work grew out of an earlier assignment on full-name handwriting recognition, where large, noisy scans of handwritten names needed to be converted into text at scale. That original corpus (400,000+ names) was too large and messy for the current constraints, so I pivoted to a smaller, well-labelled character dataset that preserved the core challenge—recognising handwriting—while remaining computationally manageable.  

The dataset is neatly organised into training, test, and augmented sets: **2,728** original training images, **13,640** augmented images, and **682** test images, perfectly stratified across the 62 classes. Preprocessing standardises all inputs by resizing images (up to 128×128), converting to grayscale, and scaling pixel values to the [0,1] range. For deep models, the 2D spatial structure is preserved so convolutional layers can learn strokes and shapes. For classical models such as logistic regression and SVM, images are flattened into 1D vectors, sometimes with dimensionality reduction (e.g., PCA) to control complexity. Exploratory visualisations highlight strong foreground–background contrast and substantial intra-class variation in stroke width, slant, and alignment, underscoring the need for augmentation and regularisation.  

<img width="658" height="484" alt="Screenshot 2025-11-15 115130" src="https://github.com/user-attachments/assets/93931e0c-18e1-4666-9b56-b19a0fa9bfb5" />

<img width="993" height="583" alt="Screenshot 2025-11-15 115224" src="https://github.com/user-attachments/assets/82cca437-8317-42f4-8d5d-a0a8841193f0" />

<img width="983" height="538" alt="Screenshot 2025-11-15 115240" src="https://github.com/user-attachments/assets/fc3743e3-7ec4-4308-b6cb-45df54c3dac0" />

<img width="979" height="574" alt="Screenshot 2025-11-15 115256" src="https://github.com/user-attachments/assets/fb209d4a-fe1a-4f2e-8ee3-5f07d3cc4fe8" />

<img width="916" height="683" alt="Screenshot 2025-11-15 115314" src="https://github.com/user-attachments/assets/89ca0328-d891-4482-a15d-02edb426c1c2" />

<img width="605" height="743" alt="Screenshot 2025-11-15 115415" src="https://github.com/user-attachments/assets/86be0d34-4bd0-42a3-ad76-fdca443fd31a" />

Three algorithm families were explored: **logistic regression**, **SVMs**, and **CNNs**. Logistic regression serves as a simple, transparent baseline but achieves only around **5% accuracy** on this 62-class task, confirming that linear decision boundaries are inadequate for complex image structure. An RBF-kernel SVM performs better, reaching **36.8% accuracy** initially and **43.0%** after a focused grid search over the regularisation parameter `C` with class-weight balancing. This tuning improves macro-F1 to approximately **0.43** and yields more stable performance across classes, but many thin-stroke and look-alike characters remain poorly classified, revealing the limits of raw-pixel SVMs.  

The **CNN** is the main model of interest. It operates on 128×128 inputs and uses five convolutional blocks with Batch Normalisation, pooling, Dropout, and a global average pooling layer before the final dense output layer. Training uses augmented data (rotations, translations, slight distortions) and a clean validation/test split. A compact hyperparameter search over learning rate, batch size, and label smoothing identifies an effective configuration: **learning rate = 1e-4**, **batch size = 64**, **label smoothing = 0.05** with augmentation enabled. Under this setup, the CNN reaches **89.3% test accuracy** with **macro-F1 ≈ 0.89**, dramatically outperforming both logistic regression and the tuned SVM.  

<img width="675" height="519" alt="Screenshot 2025-11-15 115453" src="https://github.com/user-attachments/assets/d49a9d50-23d2-4e4b-8bf5-046181cd4231" />

<img width="604" height="463" alt="Screenshot 2025-11-15 115513" src="https://github.com/user-attachments/assets/d40a007f-2dcb-4a04-8671-337a5971ce1a" />

<img width="538" height="353" alt="Screenshot 2025-11-15 115538" src="https://github.com/user-attachments/assets/a3e7834d-13a0-4fa6-887f-c3865a53e65e" />


Error analysis reveals that most remaining mistakes involve visually similar symbols such as **O/0/o**, **I/l/1**, and **x/X**. Top-k evaluation shows that allowing a top-3 suggestion boosts performance to about **98.7%**, indicating that the correct class is almost always among the first few predictions—useful for interactive correction or assistive interfaces.  

<img width="802" height="652" alt="Screenshot 2025-11-15 115628" src="https://github.com/user-attachments/assets/7a3b13b1-5770-445e-8e57-8946e08bf658" />

<img width="798" height="597" alt="Screenshot 2025-11-15 115651" src="https://github.com/user-attachments/assets/17ac88c0-5afb-4c44-9f7b-87fd1d1ff869" />

<img width="976" height="591" alt="Screenshot 2025-11-15 115728" src="https://github.com/user-attachments/assets/dd6be434-ccc5-4e92-9e9b-8d9a01a8465a" />

<img width="952" height="585" alt="Screenshot 2025-11-15 115746" src="https://github.com/user-attachments/assets/d0becc22-a98b-42f1-819f-51ddf5bde706" />

The final CNN is exported as a reusable artefact: the full model (`.keras`), separate weights, class mappings, preprocessing configuration, and simple inference utilities. This packaging enables reliable deployment, further fine-tuning on new handwriting styles, and future work on pair-aware evaluation and targeted augmentation for the hardest character pairs.

