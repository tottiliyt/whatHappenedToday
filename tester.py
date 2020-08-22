from flask import Flask
from flask import render_template
from flask import request
import nltk
from cnn import get_cnn_headline
from cnn import get_cnn_text

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def test_website():
    if request.method == "GET":
        print("GET")
        return render_template('test.html', message="GET")
    else:
        print("POST")
        source = request.form['input']
        text = get_cnn_headline(source)
        tokens = nltk.word_tokenize(text)
        tagged_tokens = nltk.pos_tag(tokens)
        nouns = [token[0] for token in tagged_tokens if token[1] in ['JJ', 'JJR', 'JJS', 'FW', 'NN', 'NNS', 'NNP', 'NNPS']]
        frequency = nltk.FreqDist(nouns).most_common(20)
        print(*frequency)
        frequent_word = []
        for p in frequency:
            if p[0] is not '’' and '‘':
                frequent_word.append(p[0])
    return render_template('test2.html', RESULT=str(frequent_word))


if __name__ == "__main__":
    app.run(debug=True)