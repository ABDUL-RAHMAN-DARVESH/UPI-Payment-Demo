# UPI Payment Flow Demo

A simple Flask web application demonstrating UPI payment integration with manual confirmation system.

## 🚀 Features
I Have ability to do that automatic confirmation and send conformation via sms but these are requires some cost of api's. So i simply created this but I'll create what you want.

- **Order Summary Display** - Shows product details and ₹1 payment amount
- **UPI Deep-Link Generation** - Creates direct UPI payment links for GPay, PhonePe, Paytm
- **Manual Payment Confirmation** - User confirms payment completion after UPI transaction
- **Session Management** - Tracks orders using Flask sessions
- **Success/Failure Pages** - Displays appropriate status after payment confirmation

## 📁 Project Structure

```
UPI/
├── templates/
│   ├── index.html      # Main payment page
│   ├── success.html    # Payment success page
│   └── failed.html     # Payment failure page
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🛠️ Setup & Installation

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure UPI ID
Edit `app.py` line 32:
```python
upi_id = "your-upi-id@bank"  # Replace with your UPI ID
```

### 3. Run Application
```bash
python app.py
```

### 4. Access Application
Open browser: `http://localhost:5000`

## 💳 How It Works

1. **Generate Order** - System creates unique order ID and ₹1 payment request
2. **UPI Deep-Link** - Click "Pay via UPI" opens UPI app with pre-filled details
3. **Payment Process** - User completes payment in UPI app (GPay/PhonePe/etc.)
4. **Manual Confirmation** - User returns and confirms payment status
5. **Result Display** - Shows success or failure page based on confirmation

## 🔗 UPI Deep-Link Format

```
upi://pay?pa=merchant@bank&pn=MerchantName&am=1.00&cu=INR&tn=ORDER12345
```

**Parameters:**
- `pa` - Payee Address (UPI ID)
- `pn` - Payee Name
- `am` - Amount (₹1.00)
- `cu` - Currency (INR)
- `tn` - Transaction Note

## ⚠️ Important Notes

### Payment Confirmation
- **Manual System** - Users self-report payment status
- **No Automatic Verification** - Real UPI payments cannot be auto-detected without payment gateway
- **Security Risk** - Users can falsely claim payment completion

### Production Considerations
- Replace in-memory storage with database
- Implement proper payment gateway (Razorpay/PayU) for automatic verification
- Add proper error handling and logging
- Use environment variables for sensitive data

## 🚀 Deployment Options

### Vercel
```bash
pip install vercel
vercel --prod
```

### Netlify
- Build command: `pip install -r requirements.txt`
- Publish directory: `/`

### Railway/Render
- Direct Flask deployment supported
- Set environment variables in platform settings

## 🔧 Environment Variables

```bash
SECRET_KEY=your-secret-key-here
UPI_ID=your-upi-id@bank
```

## 📱 Compatible UPI Apps

- Google Pay (GPay)
- PhonePe
- Paytm
- BHIM
- Bank UPI apps

## 🛡️ Security Features

- Flask session encryption with secret key
- Order ID generation using random strings
- Basic input validation for payment confirmation

## 🔄 Future Enhancements

- [ ] Integrate Razorpay/PayU for automatic payment verification
- [ ] Add SMS-based payment confirmation
- [ ] Implement database storage
- [ ] Add payment timeout handling
- [ ] Create admin dashboard for payment tracking

## 📄 License

This project is for educational purposes. Use responsibly and ensure compliance with payment regulations.

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

---

**⚠️ Disclaimer:** This is a demo application. For production use, implement proper payment gateway integration for secure and automatic payment verification.
