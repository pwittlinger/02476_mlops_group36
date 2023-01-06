# MLOPS project description - News article summarization using Natural Language Processing

### Motivation

In our current fast pace society, it is impossible to keep up with the information being generated every single minute.  
Even if one limits itself to articles, the volume will still be too much. However, not everything contained in an article is actually relevant.
With the abundance of information available, it is therefore neccessary to focus only on relevant information and articles.

### Overall goal of the project
Our aim is to perform abstractive and extractive text summarization on news articles. This will reduce the time spent on any given article.

### What framework are you going to use (Kornia, Transformer, Pytorch-Geometrics)
The [Transformers](https://github.com/huggingface/transformers) framework provided by HuggingFace provides high-performance NLP models suitable for a wide range of application - including text summarization.


### What data are you going to run on (initially, may change)
The [CNN Dailymail](https://www.kaggle.com/datasets/gowrishankarp/newspaper-text-summarization-cnn-dailymail) Dataset contains approximately 300k new articles.
Each entry contains the article alongside the summarized article, as well as a unique id.
If time allows, we may expand our model by the [XSum dataset and additional articles from Multi-News](https://www.kaggle.com/datasets/sbhatti/news-summarization), available on Kaggle as well.

### What deep learning models do you expect to use
Due to both time- and computational constraints, we will refer to pre-trained models, which we intend to fine-tune on the dataset.
As the dataset is fairly popular for text summarization, there are several models fitted to it already available. We will use [BigBirdPegasus](https://huggingface.co/docs/transformers/model_doc/bigbird_pegasus) or [Pegasus](https://huggingface.co/docs/transformers/model_doc/pegasus), and might extend using [DistilBERT](https://huggingface.co/docs/transformers/model_doc/distilbert) or [ALBERT](https://huggingface.co/docs/transformers/model_doc/albert)


## Checklist
See [CHECKLIST.md]