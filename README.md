# Advanced Image Search System with Machine Learning and Elasticsearch

### medium article is [Building an Advanced Image Search System with Machine Learning and ElasticSearch](https://guttikondaparthasai.medium.com/building-an-advanced-image-search-system-with-machine-learning-and-elasticsearch-b2155ebbeada)

[![Elastic Stack version](https://img.shields.io/badge/Elastic%20Stack-8.13.3-00bfb3?style=flat&logo=elastic-stack)](https://www.elastic.co/blog/category/releases)
[![Build Status](https://github.com/deviantony/docker-elk/workflows/CI/badge.svg?branch=main)](https://github.com/deviantony/docker-elk/actions?query=workflow%3ACI+branch%3Amain)
[![Join the chat](https://badges.gitter.im/Join%20Chat.svg)](https://app.gitter.im/#/room/#deviantony_docker-elk:gitter.im)

Run the latest version of the [Elastic stack][elk-stack] with Docker and Docker Compose.

It gives you the ability to analyze any data set by using the searching/aggregation capabilities of Elasticsearch and
the visualization power of Kibana.

Based on the [official Docker images][elastic-docker] from Elastic:

* [Elasticsearch](https://github.com/elastic/elasticsearch/tree/main/distribution/docker)
* [Logstash](https://github.com/elastic/logstash/tree/main/docker)
* [Kibana](https://github.com/elastic/kibana/tree/main/src/dev/build/tasks/os_packages/docker_generator)

Other available stack variants:

* [`tls`](https://github.com/deviantony/docker-elk/tree/tls): TLS encryption enabled in Elasticsearch, Kibana (opt in),
  and Fleet
* [`searchguard`](https://github.com/deviantony/docker-elk/tree/searchguard): Search Guard support

> [!IMPORTANT]
> [Platinum][subscriptions] features are enabled by default for a [trial][license-mngmt] duration of **30 days**. After
> this evaluation period, you will retain access to all the free features included in the Open Basic license seamlessly,
> without manual intervention required, and without losing any data. Refer to the [How to disable paid
> features](#how-to-disable-paid-features) section to opt out of this behaviour.

---

## tl;dr

```sh
docker-compose up setup
```

```sh
docker-compose up
```

![Animated demo](https://user-images.githubusercontent.com/3299086/155972072-0c89d6db-707a-47a1-818b-5f976565f95a.gif)

---

# Advanced Image Search System with Machine Learning and Elasticsearch

## Overview

This project demonstrates the creation of an advanced image search system using OpenAI's CLIP model and Elasticsearch. The system allows for searching images using other images rather than keywords, leveraging machine learning techniques to process images into feature vectors and Elasticsearch for storing and searching these vectors using cosine similarity.

## Prerequisites

- Docker
- Python 3.7+
- Libraries: `torch`, `transformers`, `pillow`, `requests`, `torchvision`, `matplotlib`, `flask`
- Jupyter Notebook

## Project Structure

```
.
├── templates
├── uploads
├── SearchEngine.ipynb
├── app.py
```

## Setup

### Step 1: Set Up the ELK Stack Using Docker

1. Clone the repository:

    ```bash
    git clone https://github.com/propardhu/Docker_ELK_Image_Search.git
    cd Docker_ELK_Image_Search
    ```

2. Bring up the ELK stack using Docker Compose:

    ```bash
    docker-compose up
    ```

3. Verify the setup:
    - Elasticsearch: [http://localhost:9200](http://localhost:9200)
    - Kibana: [http://localhost:5601](http://localhost:5601)
        - Username: `elastic`
        - Password: `changeme`

### Step 2: Install Python Dependencies

Install the necessary Python libraries:

```bash
pip install torch transformers pillow requests torchvision matplotlib flask jupyter
```

### Step 3: Preprocess Images and Store Vectors in Elasticsearch

1. Start Jupyter Notebook:

    ```bash
    jupyter notebook
    ```

2. Open the `SearchEngine.ipynb` notebook and run all cells to preprocess the Oxford Pets dataset and store the image vectors in Elasticsearch.

### Step 4: Run the Flask App

1. Ensure the project structure is as follows:

    ```
    .
    ├── templates
    ├── uploads
    ├── SearchEngine.ipynb
    ├── app.py
    ```

2. Start the Flask app by running:

    ```bash
    python app.py
    ```

3. Access the web interface by opening your browser and going to [http://localhost:5000](http://localhost:5000).

## Conclusion

In this project, we built an advanced image search system using OpenAI's CLIP model and Elasticsearch. By setting up the ELK stack with Docker, installing the necessary dependencies, running the Jupyter notebook to preprocess and store vectors, and running the Flask app, you can search for images using other images through a user-friendly web interface.

---

Would you like me to remember anything specific about this project or your work with it?
