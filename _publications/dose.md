---
abstract: |-
  Electricity and appliance usage information can often reveal the nature of human activities in a home. For instance, sensing the use of vacuum cleaner, a microwave oven, and kitchen appliances can give insights into a person's current activities. Instead of putting a sensor on each appliance, our technique is based on the idea that appliance usage can be sensed by their manifestations in an environment's existing electrical infrastructure. Prior approaches using this technique could only detect an appliance's on-off states; that is, they only sense “what” is being used, but not “how” it is used. In this paper, we introduce DOSE, a significant advancement for inferring operating states of electronic devices from a single sensing point in a home. When an electronic device is in operation, it generates time-varying Electromagnetic Interference (EMI) based upon its operating states (e.g., vacuuming on a rug vs. hardwood floor). This EMI noise is coupled to the power line and can be picked up from a single sensing hardware attached to the wall outlet in a house. Unlike prior data-driven approaches, we employ domain knowledge of the device's circuitry for semi-supervised model training to avoid tedious labeling process. We evaluated DOSE in a residential house for 2 months and found that operating states for 16 appliances could be estimated with an average accuracy of 93.8%. These fine-grained electrical characteristics affords rich feature sets of electrical events and have the potential to support various applications such as in-home activity inference, energy disaggregation and device failure detection.
authors:
- chen
- gupta
- larson
- patel
award: ''
bibtex: |-
  @INPROCEEDINGS{7146508, 
  author={K. Y. Chen and S. Gupta and E. C. Larson and S. Patel}, 
  booktitle={Pervasive Computing and Communications (PerCom), 2015 IEEE International Conference on}, 
  title={DOSE: Detecting user-driven operating states of electronic devices from a single sensing point}, 
  year={2015}, 
  pages={46-54}, 
  keywords={electric sensing devices;electromagnetic interference;microwave ovens;power cables;DOSE;EMI noise;appliance on-off state detection;electronic device;fine-grained electrical characteristic;kitchen appliance sensing;microwave oven sensing;power line;semisupervised model training;single sensing point;time-varying electromagnetic interference;user-driven operating states detection;vacuum cleaner sensing;Commutation;Electromagnetic interference;Home appliances;Noise;Permanent magnet motors;Sensors;Switched-mode power supply}, 
  doi={10.1109/PERCOM.2015.7146508}, 
  month={March},}
caption: 'DOSE detects user-driven operating states of electronic appliances through a single sensing point installed anywhere in the house.'
citation: |-
  K. Y. Chen, S. Gupta, E. C. Larson and S. Patel, "DOSE: Detecting user-driven operating states of electronic devices from a single sensing point," Pervasive Computing and Communications (PerCom), 2015 IEEE International Conference on, St. Louis, MO, 2015, pp. 46-54.
conference: IEEE International Conference on Pervasive Computing and Communications (PerCom), 2015
date: '2015-03-23'
image: '/images/pubs/DOSE.jpg'
pdf: /pdfs/dose.pdf
thumbnail: '/images/pubs/DOSE.jpg'
title: 'DOSE: Detecting user-driven operating states of electronic devices from a single sensing point'
video: 'https://www.youtube.com/watch?v=PixXD-RGxX8'
video_embed: '<iframe width="560" height="315" src="https://www.youtube.com/embed/PixXD-RGxX8" frameborder="0" allowfullscreen></iframe>'
---