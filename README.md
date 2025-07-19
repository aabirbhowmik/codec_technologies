# codec_technologies
# Real-Time Stock Market Dashboard & Secure Authentication System

This repository contains two integrated projects:

1. **Real-Time Stock Market Dashboard** – A Streamlit-based dashboard for live stock data visualization with technical indicators.
2. **Secure Authentication System** – A Flask-based REST API for user registration, login, and protected route access using JWT authentication.

---

## 📊 Real-Time Stock Market Dashboard

### Features

- Fetches real-time stock data using `yfinance`
- Interactive charts using Plotly (candlestick or line)
- Technical indicators: SMA (20), EMA (20)
- Display of key metrics (price, high, low, volume)
- Sidebar to switch ticker, time period, chart type
- Real-time metrics for popular stocks like AAPL, MSFT, AMZN, GOOGL

# 🔐 Secure Authentication System

A secure and extensible REST API built with Flask for user registration, login, and access control using JWT (JSON Web Tokens). This microservice is suitable as a base for authenticating users in web or mobile applications.

---

## ✨ Features

- ✅ User registration with email and password
- 🔐 Passwords are hashed using Bcrypt
- 🔑 JWT-based authentication for stateless security
- 🔒 Protected routes with token validation
- 🧪 Scalable architecture using Flask, SQLAlchemy

