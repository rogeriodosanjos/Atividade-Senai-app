from flask import Flask, jsonify, request

app = Flask(__name__)

comments = [
    {
        "content_id":1,
        "Nome":"Rogerio dos Anjos",
        "Faculdade":"Senai Fatesg",
        "Disciplina":"Infraestrutura Agil",
        "Professor":"Bruno Urbano"
    }
]

@app.route('/api/comment/list/<int:content_id>', methods=['GET'])
def comment_id(content_id):
    comment_id_number = [comment for comment in comments if comment['content_id'] == content_id ]
    return jsonify(comment_id_number), 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
