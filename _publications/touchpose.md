---
abstract: |-
  Today’s touchscreen devices commonly detect the coordinates of user input using capacitive sensing. Yet, these coordinates are the mere 2D manifestations of the more complex 3D configuration of the whole hand—a sensation that touchscreen devices so far remain oblivious to. In this work, we introduce the problem of reconstructing a 3D hand skeleton from capacitive images, which encode the sparse observations captured by touch sensors. These low-resolution images represent intensity mappings that are proportional to the distance to the user’s fingers and hands. We present the first dataset of capacitive images with corresponding depth maps and 3D hand pose coordinates, comprising 65,374 aligned records from 10 participants. We introduce our supervised method TouchPose, which learns a 3D hand model and a corresponding depth map using a cross-modal trained embedding from capacitive images in our dataset. We quantitatively evaluate TouchPose’s accuracy in touch contact classification, depth estimation, and 3D joint reconstruction, showing that our model generalizes to hand poses it has never seen during training and that it can infer joints that lie outside the touch sensor’s volume. Enabled by TouchPose, we demonstrate a series of interactive apps and novel interactions on multitouch devices. These applications show TouchPose’s versatile capability to serve as a general-purpose model, operating independent of use-case, and establishing 3D hand pose as an integral part of the input dictionary for application designers and developers. We also release our dataset, code, and model to enable future work in this domain.
authors:
- ahuja
- Paul Streli
- Christian Holz
caption: ''
citation: |-
  Karan Ahuja, Paul Streli, and Christian Holz. 2021. TouchPose: Hand Pose Prediction, Depth Estimation, and Touch Classification from Capacitive Images. <i>The 34th Annual ACM Symposium on User Interface Software and Technology</i>. Association for Computing Machinery, New York, NY, USA, 997–1009. DOI:https://doi.org/10.1145/3472749.3474801
conference: Proceedings of User Interface Software and Technology (UIST) 2021
date: '2021-10-1'
image: '/images/pubs/touchpose.png'
pdf: /pdfs/touchpose.pdf
thumbnail: '/images/pubs/touchpose.png'
name: 'TouchPose'
title: 'TouchPose: Hand Pose Prediction, Depth Estimation, and Touch Classification from Capacitive Images'
video: 'https://youtu.be/Lv7POLbZxcs'
video_embed: '<iframe width="560" height="315" src="https://www.youtube.com/embed/Lv7POLbZxcs" frameborder="0" allowfullscreen></iframe>'
onhomepage: false
blurb: Hand Pose Prediction, Depth Estimation, and Touch Classification from Capacitive Images
category: interaction
---
