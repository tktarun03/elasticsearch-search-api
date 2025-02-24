# elasticsearch-search-api

A simple search API built with Python and Elasticsearch for full-text search capabilities.

## 🚀 Features
- Uses **Elasticsearch** for full-text search.
- Provides **indexing & search capabilities** via API.
- Lightweight and easy to deploy.

## 📂 Project Structure
```
elasticsearch-search-api/
│── src/
│   ├── app.py  # Flask API for search functionality
│── requirements.txt  # Dependencies
│── README.md
```

## 🛠 Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/tktarun03/elasticsearch-search-api.git
   cd elasticsearch-search-api
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start Elasticsearch (Ensure it's running at `http://localhost:9200`):
   ```bash
   docker run -d -p 9200:9200 -e "discovery.type=single-node" elasticsearch:7.10.1
   ```

4. Start the Flask API server:
   ```bash
   python src/app.py
   ```

5. Use the API:
   - **Index a document** (POST): `http://127.0.0.1:5000/index`  
   - **Search a document** (GET): `http://127.0.0.1:5000/search?q=your_query`  

## 👨‍💻 About the Author

🚀 Created by [Arunkumar Thamilarasu](https://github.com/tktarun03) | UI Technical Architect | Elasticsearch & Search Expert

## ⭐ Contribute & Support
- Fork & Star this repository! ⭐
- Submit Issues and PRs to improve the search API.

---
🎯 **Follow me on GitHub**: [@tktarun03](https://github.com/tktarun03)
