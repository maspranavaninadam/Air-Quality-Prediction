from flask import Flask, render_template, redirect, request
from sklearn.externals import joblib


app = Flask(__name__)

model = joblib.load("model.pkl")
model_dtr = joblib.load("model_dtr.pkl")

@app.route('/')
def hello():
	return render_template("index.html")


@app.route('/predict', methods = ['POST'])
def air():
	if request.method == 'POST':
		CO = request.form['CO']  
		if CO == "":
			return render_template("index.html", msg="Dont leave fields Empty")
		else:
			CO = float(CO)
		S1 = request.form['S1']
		if S1 == "":
			return render_template("index.html", msg="Dont leave fields Empty S1")
		else:
			S1 = float(S1)
		S2 = request.form['S2']
		if S2 == "":
			return render_template("index.html", msg="Dont leave fields Empty")
		else:
			S2 = float(S2)
		NOx = request.form['NOx']
		if NOx == "":
			return render_template("index.html", msg="Dont leave fields Empty")
		else:
			NOx = float(NOx)
		S3 = request.form['S3']  
		if S3 == "":
			return render_template("index.html", msg="Dont leave fields Empty")
		else:
			S3 = float(S3)
		NO2 = request.form['NO2']
		if NO2 == "":
			return render_template("index.html", msg="Dont leave fields Empty")
		else:
			NO2 = float(NO2)
		S4 = request.form['S4']
		if S4 == "":
			return render_template("index.html", msg="Dont leave fields Empty")
		else:
			S4 = float(S4)
		S5 = request.form['S5']
		if S5 == "":
			return render_template("index.html", msg="Dont leave fields Empty")
		else:
			S5 = float(S5)

		c6h6 = str(model_dtr.predict([[CO,S1,S2,NOx,S3,NO2,S4,S5]])[0])
	return render_template("index.html", air_quality=round(float(c6h6), 3))


if __name__ == '__main__':
	app.run(debug = True)