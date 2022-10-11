---
abstract: |-
  Despite advances in audio- and motion-based human activity recognition (HAR) systems, a practical, power-efficient, and privacy-sensitive activity recognition system has remained elusive. State-of-the-art activity recognition systems often require power-hungry and privacy-invasive audio data. This is especially challenging for resource-constrained wearables, such as smartwatches. To counter the need for an always-on audio-based activity classification system, we first make use of power and compute-optimized IMUs sampled at 50~Hz to act as a trigger for detecting activity events. Once detected, we use a multimodal deep learning model that augments the motion data with audio data captured on a smartwatch. We subsample this audio to rates $\leq$~1~kHz, rendering spoken content unintelligible, while also reducing power consumption on mobile devices. Our multimodal deep learning model achieves a recognition accuracy of 92.2\% across 26 daily activities in four indoor environments. Our findings show that subsamping audio from 16~kHz down to 1~kHz, in concert with motion data, does not result in a significant drop in inference accuracy. We also analyze the speech content intelligibility and power requirements of audio sampled at less than 1~kHz and demonstrate that our proposed approach can improve the practicality of human activity recognition systems.
authors:
- mollyn
- ahuja
- Dhruv Verma
- Chris Harrison
- goel
caption: ''
citation: |-
  Vimal Mollyn, Karan Ahuja, Dhruv Verma, Chris Harrison, Mayank Goel. 2022. SAMoSA: Sensing Activities with Motion and Subsampled Audio. Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies (IMWUT). 2022"
conference: Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies (IMWUT)
date: '2022-09-10'
image: '/images/pubs/samosa.png'
pdf: /pdfs/samosa.pdf
thumbnail: '/images/pubs/samosa.png'
name: 'SAMoSA'
title: 'SAMoSA: Sensing Activities with Motion and Subsampled Audio'
video: 'https://youtu.be/v6fj7OL8gp0'
video_embed: '<iframe width="560" height="315" src="https://www.youtube.com/embed/v6fj7OL8gp0" frameborder="0" allowfullscreen></iframe>'
onhomepage: true
blurb: Practical and deployable activity recognition using motion and sound sensed on watches
category: activity
---
