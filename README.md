GuardianNews
==============================

Analysis of content from  the Guardian publications (The Guardian newpaper, The Observer Newspaper and guardian.com).

<h2>Status</h2> 

So far have:
- scraped the full article data on a day by day basis for several years from API: [src/data/guardian_api_pull.py](https://github.com/TSGreen/GuardianNews_NLP/blob/master/src/data/guardian_api_pull.py)
- collated the raw json files of daily data into single csv files for each year: [src/data/create_dataframe.py](https://github.com/TSGreen/GuardianNews_NLP/blob/master/src/data/create_dataframe.py)
- processed and cleaned the data files: [src/data/clean_dataframe.py](https://github.com/TSGreen/GuardianNews_NLP/blob/master/src/data/clean_dataframe.py)
- performed EDA: [notebooks/exploratory_analysis](https://github.com/TSGreen/GuardianNews_NLP/blob/master/notebooks/exploratory_analysis.ipynb)
- performed exploratory NLP and word tokenisation: [notebooks/notebooks/exploratory_nlp](https://github.com/TSGreen/GuardianNews_NLP/blob/master/notebooks/exploratory_nlp.ipynb)

Possible avenues of exploration:
- build classification model to classify articles into streams of content (e.g. news, opinion, sports, lifestyle, arts) using the text content of an article.
- explore sentiment analysis on articles
- use NER for topic classification (politics, health, education, etc)
- use NER to analyse trending topics in news reporting  -- compare relative proportion of reporting on topics such as health, education or politics over time.  

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
# GuardianNews_NLP
