import os
from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename
import torch
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import requests
import json
import matplotlib.pyplot as plt

# Use the Agg backend for non-interactive plotting
import matplotlib
matplotlib.use('Agg')

# Load the CLIP model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Function to preprocess images and extract features
def extract_features(image):
    inputs = processor(images=image, return_tensors="pt")
    with torch.no_grad():
        image_features = model.get_image_features(**inputs)
    image_features = image_features / image_features.norm(dim=-1, keepdim=True)
    return image_features.squeeze().tolist()

# Elasticsearch settings
ES_HOST = "http://localhost:9200"
ES_INDEX = "image-index"
ES_USER = "elastic"
ES_PASS = "changeme"

# Function to search for similar images
def search_similar_images(query_image_path, k=5):
    query_image = Image.open(query_image_path)
    query_features = extract_features(query_image)
    search_query = {
        "knn": {
            "field": "vector",
            "query_vector": query_features,
            "k": k,
            "num_candidates": 100
        }
    }
    response = requests.post(
        f"{ES_HOST}/{ES_INDEX}/_knn_search",
        headers={"Content-Type": "application/json"},
        auth=(ES_USER, ES_PASS),
        data=json.dumps(search_query)
    )
    return response.json()

# Function to display images
def display_images(query_image_path, search_results, output_path):
    query_image = Image.open(query_image_path)
    fig, axes = plt.subplots(1, 6, figsize=(20, 5))

    # Display the query image
    axes[0].imshow(query_image)
    axes[0].set_title("Query Image")
    axes[0].axis('off')
    print(search_results)
    # Display the top 5 similar images
    for i, hit in enumerate(search_results['hits']['hits']):
        image_id = hit['_id']
        label = hit['_source']['label']
        similar_image_path = os.path.join('./oxford_pets', f"image_{image_id}.jpg")
        
        similar_image = Image.open(similar_image_path)
        axes[i + 1].imshow(similar_image)
        axes[i + 1].set_title(f"Label: {label}\nScore: {hit['_score']:.2f}")
        axes[i + 1].axis('off')

    plt.savefig(output_path)
    plt.close()

# Initialize the Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def upload_form():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        query_result = search_similar_images(filepath)
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'result.png')
        display_images(filepath, query_result, output_path)

        return send_from_directory(app.config['UPLOAD_FOLDER'], 'result.png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

