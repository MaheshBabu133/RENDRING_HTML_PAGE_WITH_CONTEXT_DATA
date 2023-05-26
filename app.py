from flask import Flask,render_template
FAI=Flask(__name__)


@FAI.route('/Harshad')
def Harshad():
    return render_template('Harshad.html')
@FAI.route('/Greeshma')
def Greeshma():
    return render_template('Greeshma.html',name='Greeshma Shetty',Age=22,Trainer='SQL Trainer')

if __name__=="__main__":
    FAI.run(debug=True)