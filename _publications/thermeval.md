---
abstract: |-
  Vision language models (VLMs) achieve strong performance on RGB imagery, but they do not generalize to thermal images. Thermal sensing plays a critical role in settings where visible light fails, including nighttime surveillance, search and rescue, autonomous driving, and medical screening. Unlike RGB imagery, thermal images encode physical temperature rather than color or texture, requiring perceptual and reasoning capabilities that existing RGB-centric benchmarks do not evaluate.

  We introduce ThermEval-B, a structured benchmark of approximately 55,000 thermal visual question answering pairs designed to assess the foundational primitives required for thermal vision language understanding. ThermEval-B integrates public datasets with our newly collected ThermEval-D, the first dataset to provide dense per-pixel temperature maps with semantic body-part annotations across diverse indoor and outdoor environments.

  Evaluating 25 open-source and closed-source VLMs, we find that models consistently fail at temperature-grounded reasoning, degrade under colormap transformations, and default to language priors or fixed responses, with only marginal gains from prompting or supervised fine-tuning. These results demonstrate that thermal understanding requires dedicated evaluation beyond RGB-centric assumptions, positioning ThermEval as a benchmark to drive progress in thermal vision language modeling.
authors:
- shrivastava
- Kirtan Gangani
- Laksh Jain
- goel
- Nipun Batra
bibtex: |-
  @article{shrivastava2026thermeval,
    title={ThermEval: A Structured Benchmark for Evaluation of Vision-Language Models on Thermal Imagery},
    author={Shrivastava, Ayush and Gangani, Kirtan and Jain, Laksh and Goel, Mayank and Batra, Nipun},
    journal={KDD 2026, The 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining},
    year={2026},
    doi={10.48550/arXiv.2602.14989}
  }
blurb: A structured benchmark for evaluating vision-language models on thermal imagery.
citation: 'Ayush Shrivastava, Kirtan Gangani, Laksh Jain, Mayank Goel, and Nipun Batra. 2026. ThermEval: A Structured Benchmark for Evaluation of Vision-Language Models on Thermal Imagery. arXiv preprint arXiv:2602.14989. https://doi.org/10.48550/arXiv.2602.14989'
conference: KDD 2026, The 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining
date: '2026-06-16'
image: /images/pubs/thermeval.jpg
thumbnail: /images/pubs/thermeval.jpg
pdf: /pdfs/thermeval.pdf
title: 'ThermEval: A Structured Benchmark for Evaluation of Vision-Language Models on Thermal Imagery'
name: ThermEval
year: '2026'
onhomepage: true
code: https://github.com/AyushShrivstava/ThermEval_KDD
dataset: https://www.kaggle.com/datasets/shriayush/thermeval
---
