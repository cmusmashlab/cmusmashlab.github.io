---
abstract: |-
  The proliferation of sensors powered by state-of-the-art machine learning techniques can now infer context, recognize activities and enable interactions. A key component required to build these automated sensing systems is labeled training data. However, the cost of collecting and labeling new data impedes our ability to deploy new sensors to recognize human activities. We tackle this challenge using domain adaptation i.e., using existing labeled data in a different domain to aid the training of a machine learning model for a new sensor. In this paper, we use off-the-shelf smartwatch IMU datasets to train an activity recognition system for mmWave radar sensor with minimally labeled data. We demonstrate that despite the lack of extensive datasets for mmWave radar, we are able to use our domain adaptation approach to build an activity recognition system that classifies between 10 activities with an accuracy of 70% with only 15 seconds of labeled doppler data. We also present results for a range of available labeled data (10 - 30 seconds) and show that our approach outperforms the baseline in every single scenario. We take our approach a step further and show that multiple IMU datasets can be combined together to act as a single source for our domain adaptation approach.
authors:
- Sejal Bhalla
- goel
- khurana
caption: ''
citation: |-
  Sejal Bhalla, Mayank Goel, Rushil Khurana. 2021. "IMU2Doppler: Cross-Modal Domain Adaptation for Doppler-based Activity Recognition Using IMU Data." Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies 5.4 (2021): 1-20.
conference: Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies (IMWUT) 2022
date: '2021-12-21'
image: '/images/pubs/imu2dop.png'
pdf: /pdfs/imu2dop.pdf
thumbnail: '/images/pubs/imu2dop.png'
name: 'IMU2Doppler'
title: 'IMU2Doppler: Cross-Modal Domain Adaptation for Doppler-based Activity Recognition Using IMU Data'
video: 'https://youtu.be/3EbK2MT-fDk'
video_embed: '<iframe width="560" height="315" src="https://www.youtube.com/embed/3EbK2MT-fDk" frameborder="0" allowfullscreen></iframe>'
onhomepage: true
blurb: Synthesizing Doppler Radar Data from Motion Sensors for Enabling Deployable Activity Recognition
category: activity
---
