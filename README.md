# Multilingual Customer Review Analyzer

## Description

This project analyzes customer reviews in multiple languages (focusing on complaints), automatically detecting:

- Sentiment (positive / neutral / negative)
- Complaint category (delivery / refund / product defect / customer service / other)
- Urgency level (1 - 5)

**Features:** translation, sentiment analysis, topic classification, urgency detection, visualization.

**Languages**: English, Japanese, German, French, Chinese, Spanish.

---

## Tech Stack

- **Models**:
- **Translation**:
- **Frontend**:
- **Data**: [Multilingual Amazon Reviews Corpus](https://www.amazon.science/publications/the-multilingual-amazon-reviews-corpus)

---

## Installation

Run the followings:

```bash
git clone https://github.com/dangtran278/multilingual-customer-review-analyzer.git
cd multilingual-complaint-analyzer
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
./scripts/get_dataset.py
```

## Citation

Please cite the following paper [(arXiv)](https://arxiv.org/abs/2010.02573) if you found this dataset useful:

Phillip Keung, Yichao Lu, György Szarvas and Noah A. Smith. "The Multilingual Amazon Reviews Corpus." In Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing, 2020.

```
@inproceedings{marc_reviews,
    title={The Multilingual Amazon Reviews Corpus},
    author={Keung, Phillip and Lu, Yichao and Szarvas, György and Smith, Noah A.},
    booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},
    year={2020}
}
```
