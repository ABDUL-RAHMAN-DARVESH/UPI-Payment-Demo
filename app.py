from flask import Flask, render_template, request, redirect, url_for, session
import random
import string
from datetime import datetime

app = Flask(__name__)
import os
app.secret_key = os.environ.get('SECRET_KEY', 'fallback-key')

# In-memory storage for demo (use database in production)
payments = {}

def generate_order_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

@app.route('/')
def index():
    order_id = generate_order_id()
    amount = 1.00
    product = "AI Course Access"

    # Store payment details
    payments[order_id] = {
        'amount': amount,
        'product': product,
        'status': 'pending',
        'created_at': datetime.now()
    }
    
    session['current_order'] = order_id

    # Create UPI deep link
    upi_id = "exampleUPI@sbi"
    payee_name = "UserStore"
    note = f"Payment for {order_id}"

    upi_link = f"upi://pay?pa={upi_id}&pn={payee_name}&am={amount}&cu=INR&tn={note}"

    return render_template(
        'index.html',
        product=product,
        order_id=order_id,
        amount=amount,
        upi_link=upi_link
    )

@app.route('/confirm-payment')
def confirm_payment():
    return render_template('confirm.html')

@app.route('/payment-status', methods=['POST'])
def payment_status():
    order_id = request.form.get('order_id')
    user_confirmation = request.form.get('payment_done')
    
    if order_id in payments and user_confirmation == 'yes':
        payments[order_id]['status'] = 'completed'
        return render_template('success.html', order_id=order_id)
    else:
        return render_template('failed.html', order_id=order_id)

@app.route('/check-status/<order_id>')
def check_status(order_id):
    if order_id in payments:
        return {'status': payments[order_id]['status']}
    return {'status': 'not_found'}

if __name__ == '__main__':
    app.run(debug=True)
