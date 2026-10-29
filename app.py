from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template("register.html")
@app.route('\register',methods=['POST'])
def  register():
    name=request.form['name']
    id=request.form['id']
    email=request.form['email']
    no=request.form['no']
    return render_template("success.html",name=name,id=id,email=email,no=no)
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
