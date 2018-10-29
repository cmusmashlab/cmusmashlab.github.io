---
abstract: |-
  With the resurgence of head-mounted displays for virtual reality, users need new input devices that can accurately track their hands and fingers in motion. We introduce Finexus, a multipoint tracking system using magnetic field sensing. By instrumenting the fingertips with electromagnets, the system can track fine fingertip movements in real time using only four magnetic sensors. To keep the system robust to noise, we operate each electromagnet at a different frequency and leverage bandpass filters to distinguish signals attributed to individual sensing points. We develop a novel algorithm to efficiently calculate the 3D positions of multiple electromagnets from corresponding field strengths. In our evaluation, we report an average accuracy of 1.33 mm, as compared to results from an optical tracker. Our real-time implementation shows Finexus is applicable to a wide variety of human input tasks, such as writing in the air.
authors:
- chen
- patel
- Sean Keller
award: 'Honorable Mention Award'
bibtex: |-
  @inproceedings{Chen:2016:FTP:2858036.2858125,
   author = {Chen, Ke-Yu and Patel, Shwetak N. and Keller, Sean},
   title = {Finexus: Tracking Precise Motions of Multiple Fingertips Using Magnetic Sensing},
   booktitle = {Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems},
   series = {CHI '16},
   year = {2016},
   isbn = {978-1-4503-3362-7},
   location = {Santa Clara, California, USA},
   pages = {1504--1514},
   numpages = {11},
   url = {http://doi.acm.org/10.1145/2858036.2858125},
   doi = {10.1145/2858036.2858125},
   acmid = {2858125},
   publisher = {ACM},
   address = {New York, NY, USA},
   keywords = {3D space, electromagnet, fingertips, localization, magnetic field, real-time, tracking, wearable},
  }
caption: 'Finexus can track the fine 3D motions of multiple electromagnets attached to fingertips using four magnetic sensors. The system leverages frequency multiplexing and a bandpass filter to achieve robustness against ambient noise.'
citation: |-
  Ke-Yu Chen, Shwetak N. Patel, and Sean Keller. 2016. Finexus: Tracking Precise Motions of Multiple Fingertips Using Magnetic Sensing.  In Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems (CHI '16). ACM, New York, NY, USA,  1504-1514. DOI: http://dx.doi.org/10.1145/2858036.2858125
conference: Conference on Human Factors in Computing Systems (CHI), 2016
date: '2016-05-07'
image: '/images/pubs/finexus.png'
pdf: /pdfs/finexus.pdf
thumbnail: '/images/pubs/finexus_thumb.png'
title: 'Finexus: Tracking Precise Motions of Multiple Fingertips Using Magnetic Sensing'
video: 'https://www.youtube.com/watch?v=fHhbM_2UMiI'
video_embed: '<iframe width="560" height="315" src="https://www.youtube.com/embed/fHhbM_2UMiI" frameborder="0" allowfullscreen></iframe>'
---