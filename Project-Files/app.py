from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Temporary storage for submitted data (replace with database in real applications)
client_feedback = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    if request.method == 'POST':
        name = request.form['fullName']
        email = request.form['email']
        message = request.form['message']

        # Store data temporarily (in real app, store in database)
        client_feedback.append({'name': name, 'email': email, 'message': message})

        # Redirect to a thank you page or back to contact page
        return redirect('/thankyou')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
