from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    
@app.route('/play')                           
def play():
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html')  
    

@app.route('/play/<num>')                           
def play_num(num):
   
   return render_template('index.html',num=int(num))  



@app.route('/play/<num>/<color>')                           
def play_color(num,color):
   
   return render_template('index.html',num=int(num),color=color) 




if __name__=="__main__":
    app.run(debug=True)
