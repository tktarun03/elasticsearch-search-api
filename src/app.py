from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch(["http://localhost:9200"])

INDEX_NAME = "documents"

@app.route("/index", methods=["POST"])
def index_document():
    data = request.json
    res = es.index(index=INDEX_NAME, body=data)
    return jsonify(res)

@app.route("/search", methods=["GET"])
def search_document():
    query = request.args.get("q", "")
    search_body = {
        "query": {
            "match": {
                "content": query
            }
        }
    }
    res = es.search(index=INDEX_NAME, body=search_body)
    return jsonify(res["hits"]["hits"])

if __name__ == "__main__":
    app.run(debug=True)
