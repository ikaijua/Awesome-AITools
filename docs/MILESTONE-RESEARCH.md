# Milestone Research that Changed the Course of AI

This document archives the revolutionary research papers and projects that have fundamentally shifted the landscape of Artificial Intelligence, arranged in chronological order.

---

### LeNet (1998)
*   **Paper:** *Gradient-Based Learning Applied to Document Recognition*
*   **Authors:** Yann LeCun, Léon Bottou, Yoshua Bengio, Patrick Haffner
*   **Link:** [Official PDF (Yann LeCun's site)](http://yann.lecun.com/exdb/publis/pdf/lecun-01a.pdf)
*   **Impact:** One of the earliest successful applications of Convolutional Neural Networks (CNNs). It laid the groundwork for modern deep learning and was widely used for handwritten digit recognition (MNIST).

### ImageNet (2009)
*   **Paper:** *ImageNet: A Large-Scale Hierarchical Image Database*
*   **Authors:** Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, Li Fei-Fei
*   **Link:** [Official PDF (CVPR)](http://www.image-net.org/papers/imagenet_cvpr09.pdf)
*   **Impact:** More than a paper, ImageNet provided the massive dataset and the annual competition (ILSVRC) that acted as the primary catalyst for the deep learning revolution.

### AlexNet (2012)
*   **Paper:** *ImageNet Classification with Deep Convolutional Neural Networks*
*   **Authors:** Alex Krizhevsky, Ilya Sutskever, Geoffrey E. Hinton
*   **Link:** [arXiv:1207.0580](https://arxiv.org/abs/1207.0580) | [NeurIPS](https://proceedings.neurips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf)
*   **Impact:** The winner of the 2012 ImageNet challenge. It demonstrated the power of deep CNNs combined with GPU acceleration, marking the start of the modern deep learning era.

### GAN (2014)
*   **Paper:** *Generative Adversarial Nets*
*   **Authors:** Ian J. Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, Yoshua Bengio
*   **Link:** [arXiv:1406.2661](https://arxiv.org/abs/1406.2661) | [NeurIPS](https://proceedings.neurips.cc/paper/2014/file/5ca3e9b122f61f8f06494c97b1afccf3-Paper.pdf)
*   **Impact:** Introduced a game-theoretic framework for generative modeling (Generator vs. Discriminator). It was the dominant paradigm for image generation for nearly a decade.

### R-CNN (2014)
*   **Paper:** *Rich feature hierarchies for accurate object detection and semantic segmentation*
*   **Authors:** Ross Girshick, Jeff Donahue, Trevor Darrell, Jitendra Malik
*   **Link:** [arXiv:1311.2524](https://arxiv.org/abs/1311.2524) | [CVPR](https://openaccess.thecvf.com/content_cvpr_2014/papers/Girshick_Rich_Feature_Hierarchies_2014_CVPR_paper.pdf)
*   **Impact:** Revolutionized object detection by using deep learning for region-based classification, replacing traditional hand-crafted features.

### ResNet (2015)
*   **Paper:** *Deep Residual Learning for Image Recognition*
*   **Authors:** Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun
*   **Link:** [arXiv:1512.03385](https://arxiv.org/abs/1512.03385) | [CVPR](https://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf)
*   **Impact:** Introduced Residual Learning (skip connections) to solve the vanishing gradient problem, enabling the training of networks with hundreds or even thousands of layers.

### Faster R-CNN (2015)
*   **Paper:** *Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks*
*   **Authors:** Shaoqing Ren, Kaiming He, Ross Girshick, Jian Sun
*   **Link:** [arXiv:1506.01497](https://arxiv.org/abs/1506.01497) | [NeurIPS](https://proceedings.neurips.cc/paper/2015/file/14bfa6bb14875e45bba028a21ed38046-Paper.pdf)
*   **Impact:** Integrated the region proposal process into the neural network itself, making high-accuracy, real-time object detection feasible.

### Transformer (2017)
*   **Paper:** *Attention Is All You Need*
*   **Authors:** Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, Illia Polosukhin
*   **Link:** [arXiv:1706.03762](https://arxiv.org/abs/1706.03762) | [NeurIPS](https://proceedings.neurips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf)
*   **Impact:** Introduced the "Attention" mechanism, completely replacing RNNs and CNNs for sequence modeling. It is the foundational architecture for virtually all modern LLMs.

### BERT (2018)
*   **Paper:** *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding*
*   **Authors:** Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova
*   **Link:** [arXiv:1810.04805](https://arxiv.org/abs/1810.04805) | [ACL Anthology](https://aclanthology.org/N19-1423/)
*   **Impact:** Popularized the "Pre-train then Fine-tune" paradigm using bidirectional training, significantly improving the state-of-the-art across dozens of NLP tasks.

### NeRF (2020)
*   **Paper:** *NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis*
*   **Authors:** Ben Mildenhall, Pratul P. Srinivasan, Matthew Tancik, Jonathan T. Barron, Ravi Ramamoorthi, Ren Ng
*   **Link:** [arXiv:2003.08934](https://arxiv.org/abs/2003.08934) | [Project Page](https://www.matthewtancik.com/nerf)
*   **Impact:** Revolutionized 3D scene representation by using neural networks to map 3D coordinates and viewing angles to color and density.

### GPT-3 (2020)
*   **Paper:** *Language Models are Few-Shot Learners*
*   **Authors:** Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, et al. (OpenAI)
*   **Link:** [arXiv:2005.14165](https://arxiv.org/abs/2005.14165) | [NeurIPS](https://proceedings.neurips.cc/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf)
*   **Impact:** Demonstrated that scaling language models to 175 billion parameters leads to emergent "few-shot" capabilities across a wide range of tasks.

### ViT (Vision Transformer) (2020)
*   **Paper:** *An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale*
*   **Authors:** Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, et al. (Google Research)
*   **Link:** [arXiv:2010.11929](https://arxiv.org/abs/2010.11929) | [OpenReview](https://openreview.net/forum?id=YicbFdNTTy)
*   **Impact:** Successfully applied the Transformer architecture to computer vision, proving that Transformers can match or outperform CNNs at scale.

### Diffusion Models (DDPM) (2020)
*   **Paper:** *Denoising Diffusion Probabilistic Models*
*   **Authors:** Jonathan Ho, Ajay Jain, Pieter Abbeel
*   **Link:** [arXiv:2006.11239](https://arxiv.org/abs/2006.11239) | [NeurIPS](https://proceedings.neurips.cc/paper/2020/file/4c5bcfec8584af0d967f1ab10179ca4b-Paper.pdf)
*   **Impact:** Established Diffusion as a powerful new paradigm for high-quality image synthesis, eventually surpassing GANs in popularity and performance.

### CLIP (2021)
*   **Paper:** *Learning Transferable Visual Models From Natural Language Supervision*
*   **Authors:** Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, et al. (OpenAI)
*   **Link:** [arXiv:2103.00020](https://arxiv.org/abs/2103.00020) | [OpenAI Blog](https://openai.com/research/clip)
*   **Impact:** A pioneer in multimodal contrastive learning, connecting images and text in a shared embedding space to enable zero-shot classification.

### Gaussian Splatting (2023)
*   **Paper:** *3D Gaussian Splatting for Real-Time Radiance Field Rendering*
*   **Authors:** Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, George Drettakis
*   **Link:** [arXiv:2308.04079](https://arxiv.org/abs/2308.04079) | [Project Page](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/)
*   **Impact:** A major leap in efficiency for 3D radiance fields, enabling high-quality, real-time rendering using explicit 3D Gaussian representations.
