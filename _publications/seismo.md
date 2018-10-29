---
authors:
    - wang
    - zhu_junyi
    - jain
    - lee
    - saba
    - Lama Nachman
    - patel
abstract: |
  Seismo is a BP measurement technique using the existing sensors on the smartphone. Seismo uses pulse transit time (PTT), the time taken by the heart's pulse to propagate between two arterial sites, which is inversely related to BP. In particular, Seismo tracks the time when the blood is ejected from the heart as the aortic valve opens and when the pulse arrives at the fingertip. To perform this, Seismo relies on Seismocardiography (SCG), which uses the vibration caused by the movement of the blood and valve activities as the heart beats, allowing for accurate measurement of aortic valve opening time. The SCG is captured using the phone's accelerometer pressed against the chest. In this position, the user holds the phone with their finger covering the camera, which then captures the photoplethysmogram (PPG) at the finger, thus measuring the pulse as it arrives. This technique conveniently captures both the proximal (close to the heart) and distal (away from the heart) timing all from one device, without the need for any supplemental hardware. Additionally, PTT-based techniques can measure beat-to-beat BP, thus it can more reliably measure short-term BP changes (such as post-exercise), which are difficult to measure using cuff-based devices. One major distinction between Seismo and previous solutions that enable smartphone blood pressure tracking without additional hardware is the use of accelerometer to capture SCG as a proximal timing. Other work has mainly focused on using the sound created by the heart, otherwise known as phonocardiography (PCG). However, the fundamental limitation of using PCG as a proximal timing is that the sound being captured is actually created by the closing of the heart valves rather than the opening, thus not an ideal reference for when the blood is actually ejected. 
award: 'Honorable Mention Award'
bibtex: |-
    @inproceedings{Wang:2018:SBP:3173574.3173999,
     author = {Wang, Edward Jay and Zhu, Junyi and Jain, Mohit and Lee, Tien-Jui and Saba, Elliot and Nachman, Lama and Patel, Shwetak N.},
     title = {Seismo: Blood Pressure Monitoring Using Built-in Smartphone Accelerometer and Camera},
     booktitle = {Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems},
     series = {CHI '18},
     year = {2018},
     isbn = {978-1-4503-5620-6},
     location = {Montreal QC, Canada},
     pages = {425:1--425:9},
     numpages = {9},
     url = {http://doi.acm.org/10.1145/3173574.3173999},
     doi = {10.1145/3173574.3173999},
     acmid = {3173999},
     publisher = {ACM},
     address = {New York, NY, USA},
     keywords = {noninvasive blood pressure, photoplethysmography, physiological sensing, ppg, ptt, pulse transit time, scg, seismocardiography},
    }
caption: 'Seismo is a smartphone application that uses the built-in accelerometer and camera to calculate pulse transit time.'
citation: |
  Edward Jay Wang, Junyi Zhu, Mohit Jain, Tien-Jui Lee, Elliot Saba, Lama Nachman, and Shwetak N. Patel. 2018. Seismo: Blood Pressure Monitoring using Built-in Smartphone Accelerometer and Camera. In Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems (CHI '18). ACM, New York, NY, USA, Paper 425, 9 pages. DOI: https://doi.org/10.1145/3173574.3173999
conference: Conference on Human Factors in Computing Systems (CHI), 2018
date: '2018-04-19'
image: '/images/pubs/seismo.jpg'
pdf: '/pdfs/seismo.pdf'
thumbnail: '/images/pubs/seismo_thumb.jpg'
title: 'Seismo: Blood Pressure Monitoring using Built-in Smartphone Accelerometer and Camera'
video: 'https://youtu.be/Xd6hSQYHVCc'
video_embed: '<iframe width="560" height="315" src="https://www.youtube.com/embed/Xd6hSQYHVCc" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>'
redirect_from: /projects/seismo/
---
