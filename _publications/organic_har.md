---
abstract: "Deploying human activity recognition (HAR) at home is still rare because sensor signals vary wildly across houses, people, and time, essentially requiring in-situ data collection and training. Prior approaches use cameras to generate training labels for privacy-preserving sensors (LiDAR, RADAR, Thermal), but this forces sensors to detect predefined activities that cameras can see yet the sensors themselves cannot reliably distinguish. In this work, we introduce OrganicHAR, an activity discovery framework that inverts this relationship by placing sensor capabilities at the center of activity discovery. Our approach identifies naturally occurring signal patterns using privacy-preserving sensors, leverages Vision Language Models (VLMs) only during these key moments for scene understanding, and discovers discrete activity labels at granularities that these sensors can reliably detect. Our evaluation with 12 participants demonstrates OrganicHAR's effectiveness: it achieves 79% accuracy for coarse (4-5) activities using only basic ambient sensors (radar, lidar, thermal arrays), and 73% accuracy for fine-grained (8-9) activities when a wearable IMU, depth, and pose sensor are added. OrganicHAR maintains 77% accuracy on average across configurations while discovering 4-8 categories per user (15 across all users) tailored to each environment and sensor capabilities. By triggering video processing only at key moments identified by local sensors, we reduce queries to VLM by 90%, enabling practical and privacy-preserving activity recognition in natural settings."
authors:
- patidar
- arakawa
- Ricardo Graça
- Rúben Moutinho
- Adriano Soares
- Ana Vasconcelos
- Filippo Talami
- Joana Couto da Silva
- Inês Silva
- Cristina Mendes Santos
- goel
- Yuvraj Agarwal

bibtex: '@inproceedings{Patidar2025,

  title={OrganicHAR: Towards Activity Discovery in Organic Settings for Privacy Preserving Sensors Using Efficient Video Analysis},

  author={Prasoon Patidar, Riku Arakawa, Ricardo Graça, Rúben Moutinho, Adriano Soares, Ana Vasconcelos, Filippo Talami, Joana Couto da Silva, Inês Silva, Cristina Mendes Santos, Mayank Goel, Yuvraj Agarwal},

  booktitle={Proceedings of the ACM on Interactive, Mobile, Wearable, and Ubiquitous
  Technologies (IMWUT)},

  year={2025}

  }'
blurb: Organically discovering at-home activities that users actually care about
category: activity,privacy
citation: 'Prasoon Patidar, Riku Arakawa, Ricardo Graça, Rúben Moutinho, Adriano Soares, Ana Vasconcelos, Filippo Talami, Joana Couto da Silva, Inês Silva, Cristina Mendes Santos, Mayank Goel, Yuvraj Agarwal. 2025. OrganicHAR: Towards Activity Discovery in Organic Settings for Privacy Preserving Sensors Using Efficient Video Analysis. Proceedings of the ACM on Interactive, Mobile, Wearable, and Ubiquitous Technologies (IMWUT)'
conference: Proceedings of the ACM on Interactive, Mobile, Wearable, and Ubiquitous
  Technologies (IMWUT)
date: 2025-12-02
image: /images/pubs/organic_har.png
name: OrganicHAR
onhomepage: true
pdf: /pdfs/organic_har.pdf
thumbnail: /images/pubs/organic_har.png
title: 'OrganicHAR: Towards Activity Discovery in Organic Settings for Privacy Preserving Sensors Using Efficient Video Analysis'
year: '2025'
---
