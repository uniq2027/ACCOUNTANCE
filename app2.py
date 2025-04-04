from flask import Flask,jsonify,request,render_template

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import IntegerField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Required for CSRF protection

# Define a WTForm for PNR input
class PnrForm(FlaskForm):
    p= IntegerField('Enter Principal:', validators=[DataRequired()])
    n = IntegerField('Enter No_of_year:', validators=[DataRequired()])
    r = IntegerField('Enter Rate_of_interest:', validators=[DataRequired()])
    submit = SubmitField('Calculate Interest')

@app.route('/interest', methods=["GET", "POST"])
def interest_call():
    form = PnrForm()
    
    if request.method == "POST" and form.validate_on_submit():
        p = request.form.get("p")
        n = request.form.get("n")
        r = request.form.get("r")
        
        try:
            p= float(p)  # Convert PNR to float
            n= float(n)
            r= float(r)

            SI = p*n*r / 100  # Simple Interest Calculation
            if p < 5000:
                bg_color = "green"  # Low amount
                amount_category = "Low"
            elif 5000 <= p < 20000:
                bg_color = "orange"  # Medium amount
                amount_category = "Medium"
            else:
                bg_color = "red"  # High amount
                amount_category = "High"

            return render_template("pnr.html",form=form,SI=SI,p=p,bg_color=bg_color, amount_category=amount_category)
        except ValueError:
            return "Invalid input. Please enter a numeric PNR."

        

    return render_template("pnr.html", form=form,SI=0, p=0)


from flask import jsonify
@app.route('/calculate', methods=['GET'])
def calculate_parts():
    # Given values
    total_amount = 10000
    avg_interest = 9.2
    rate1 = 8  # 8% interest
    rate2 = 10  # 10% interest
    
    # Solve for x
    x = (total_amount * avg_interest - total_amount * rate2) / (rate1 - rate2)
    y = total_amount - x  # Remaining amount at 10%
    
    # Return the result as JSON
    return jsonify({
        "Amount at 8%": x,
        "Amount at 10%": y
    })


@app.route("/", methods=["GET", "POST"])
def calculate_installment():
    result = None
    if request.method == "POST":
        try:
            debt = float(request.form["debt"])
            years = int(request.form["years"])
            rate = float(request.form["rate"])
            
            # Calculate sum of factors like (1 + 3r/100), etc.
            total_factor = sum([(1 + (rate/100)*(years - i)) for i in range(years)])
            installment = round(debt / total_factor, 2)

            result = f"Annual Installment: ₹{installment}"
        except:
            result = "Invalid input. Please enter numeric values."
    
    return render_template("index.html", result=result)




if __name__ == '__main__':
    app.run(debug=True)

   










# from flask import Flask, render_template, request
# from flask_wtf import FlaskForm
# from wtforms import FloatField, SubmitField
# from wtforms.validators import DataRequired

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret_key'

# # Flask-WTF Form
# class InterestForm(FlaskForm):
#     principal = FloatField("Enter Principal Amount:", validators=[DataRequired()])
#     submit = SubmitField("Calculate Interest")

# # Route for Interest Calculation
# @app.route('/interest', methods=["GET", "POST"])
# def interest_call():
#     form = InterestForm()
#     SI = 0
#     interest_rate = 5  # Default 5% interest
#     bg_color = "white"  # Default color
#     amount_category = "Low"

#     if form.validate_on_submit():
#         p = form.principal.data
#         n = 1  # 1 year
#         r = interest_rate  
#         SI = (p * n * r) / 100  
        
#         # Change background color based on interest
#         if p < 5000:
#             bg_color = "green"  # Low amount
#             amount_category = "Low"
#         elif 5000 <= p < 20000:
#             bg_color = "orange"  # Medium amount
#             amount_category = "Medium"
#         else:
#             bg_color = "red"  # High amount
#             amount_category = "High"

#     return render_template("pnr.html", form=form, SI=SI, bg_color=bg_color, amount_category=amount_category)

# if __name__ == "__main__":
#     app.run(debug=True)
