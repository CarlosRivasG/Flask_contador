from flask import Flask, render_template, session, redirect

app= Flask(__name__)
app.secret_key = "Mastodonte86"

#Ejercicio 1
@app.route('/')
def index():
    if 'counter' in session:
        session['counter']=session['counter'] +1
    else:
        session['counter']=1
    return render_template( 'index.html')
   
   
@app.route('/index+2')
def index2():
    if 'counter' in session:
        session['counter']=session['counter'] + 2
    else:
        session['counter']=1
    return render_template( 'index.html')

@app.route('/destroy_session' ,methods=['GET'])
def res():
    session.clear()
    return redirect('/')





if __name__=="__main__":
    app.run(debug=True)
