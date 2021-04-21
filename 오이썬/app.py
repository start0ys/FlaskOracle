import db
from flask import Flask, render_template, request,redirect,url_for



app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    data1 = db.test()
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        content = request.form['content']
        db.test2(name,password,content)
        data1 = db.test() 
          
    if not data1:
        return render_template("index.html")
   
    return render_template("index.html",data=data1)


@app.route('/delete/')
def delete():
    id = request.args.get('id')
    db.test3(id)   
 
   
    return redirect(url_for("index"))

@app.route('/modify/',methods=['GET','POST'])
def modify():
    if request.method == 'POST':
        id = request.form['id']
        mdContent = request.form['mdContent']
   
        db.test4(id,mdContent)
        
      
    
          
  
   
    return redirect(url_for("index"))







if __name__ == "__main__":
    app.run(debug=True)


