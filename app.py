from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

articles = []
article_number = 1

## HTML을 주는 부분
@app.route('/')
def home():
   return 'This is Home!'

@app.route('/mypage')
def mypage():
   return render_template('index.html')

## API 역할을 하는 부분
@app.route('/test', methods=['POST'])
def test_post():
   # url_give를 받는 부분
   global articles
   global article_number
   url_receive = request.form['url_give']
   comment_receive = request.form['comment_give']
   category_receive = request.form['category_give']

   # global 변수 articles에 받은 것을 덮어쓰기

   article = {}
   article['url'] = url_receive
   article['comment'] = comment_receive
   article['category'] = category_receive
   article['no'] = article_number
   articles.append(article)
   article_number = article_number + 1
   print(articles)

   return jsonify({'result':'success'})

@app.route('/test', methods=['GET'])
def test_get():
   # global 변수 name을 보여주기
   global articles
   return jsonify({'result':'success', 'values': articles})

@app.route('/del', methods=['POST'])
def test_delete():
   global articles
   no_receive = request.form['no_give']

   for article in articles:
       if str(article['no']) == no_receive: #데이터 형을 같게 해준다
           articles.remove(article)
           return jsonify({'result':'success'})
   return jsonify({'result':'해당 번호의 article이 없습니다.'})
   print(articles)
if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)