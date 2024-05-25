# Advanced Image Search System with Machine Learning and Elasticsearch
### medium article is [Building an Advanced Image Search System with Machine Learning and ElasticSearch](https://guttikondaparthasai.medium.com/building-an-advanced-image-search-system-with-machine-learning-and-elasticsearch-b2155ebbeada)
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
