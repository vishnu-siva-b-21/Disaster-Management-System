# 🆘 Disaster Management System - Empowering NGOs to Respond Faster ![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Flask](https://img.shields.io/badge/Flask-2.0%2B-yellow) ![License: MIT](https://img.shields.io/badge/License-MIT-green.svg) ![Status](https://img.shields.io/badge/status-active-brightgreen)

**Disaster Management System** is a web application developed to assist **NGOs and emergency response teams** in efficiently managing help requests during crises. It connects people in need with nearby volunteers, coordinated through a structured admin–sub-admin system, ensuring timely support and scalable disaster response.

---

## 📚 Table of Contents

- 🌟 [Features](#features)
- 🌐 [Live Demo](#live-demo)
- 🧰 [Tech Stack](#tech-stack)
- 🛠️ [How to Run Locally](#how-to-run-locally)
- 💡 [Future Enhancements](#future-enhancements)
- 🤝 [Contributing](#contributing)
- 📬 [Contact](#contact)
- ⭐ [Support](#support)
- 📝 [License](#license)

---

<a id="features"></a>

## ✅ Features

- 🚨 **Emergency Request System**  
  Victims can send location-based help requests during disasters.

- 🙋‍♂️ **Volunteer Notifications**  
  Volunteers receive real-time notifications when someone nearby needs assistance.

- 🧑‍💼 **Role-Based Management**  
  Admins and Sub-Admins oversee requests, assign volunteers, and track progress.

- 📍 **Geolocation Integration**  
  Automatically fetches victim's or volunteer's location for efficient task allocation.

- 🔒 **Secure Access Controls**  
  Authentication and access control based on roles.

- 📊 **Dashboard for Monitoring**  
  Admin panel displays real-time stats on requests, volunteers, and completion rates.

- 📡 **Offline Support (PWA)**
  Allow users to submit requests even with poor network.

- 🗺️ **Map View for Volunteers (leaflet.js)**
  Enable volunteers to view requests and affected areas on a live map.

---

<a id="live-demo"></a>

## 🌐 Live Demo

🔗 **Try it here**: [Disaster Management System](https://disaster-management-system-kh12.onrender.com/)  
_(Runs best on modern browsers and desktop view.)_

---

<a id="tech-stack"></a>

## 🧰 Tech Stack

| Category      | Technologies Used                              |
| ------------- | ---------------------------------------------- |
| 💻 Frontend   | HTML, CSS, JavaScript (Vanilla)                |
| 🔙 Backend    | Python, Flask                                  |
| 🧠 API        | leaflet.js, Twillio                            |
| 🛢️ Database   | MongoDB                                        |
| 🚀 Deployment | Render / Vercel / Heroku (based on preference) |

---

<a id="how-to-run-locally"></a>

## 🛠️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/vishnu-siva-b-21/Disaster-Management-System/
cd Disaster-Management-System
```

### 2. Create a Virtual Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate   # For Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Start MongoDB Locally

To use MongoDB, install the **MongoDB Community Server** from the [official MongoDB website](https://www.mongodb.com/try/download/community).  
After installation, start the MongoDB server locally on default port 27017.

### 4. Run the Flask Application

```bash
python app.py
```

### 5. Access the Website

Open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)  
✅ Default Admin Credentials (for demo/testing)

- Email: admin@gmail.com
- Password: admin

---

<a id="future-enhancements"></a>

## 🌱 Future Enhancements

- 📱 Mobile App Integration
  Build a React Native app for easier access by victims and volunteers.

- 🧠 AI-based Prioritization
  Use AI/ML to auto-prioritize requests based on severity or region.

- 🌍 Multilingual Support
  Make the platform more accessible to non-English speakers.

---

<a id="contributing"></a>

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork the repo and open a Pull Request.

- Fork the repo
- Create a new branch (`git checkout -b feature-xyz `)
- Commit your changes (`git commit -m 'Added new feature'`)
- Push and open a Pull Request

---

<a id="contact"></a>

## 📬 Contact

If you'd like to connect or know more:  
 ✉️ Email: vishnu.siva.b.21@gmail.com  
 🔗 [LinkedIn](https://www.linkedin.com/in/b-vishnu-siva/) | [Portfolio](https://vishnusiva.site/)

---

<a id="support"></a>

### ⭐Support

If you found this project helpful, please consider giving it a star on GitHub!  
Share it with others who might benefit — educators, developers, or students!

---

<a id="license"></a>

## 📄 License

This project is licensed under the [MIT License](LICENSE.md).  
Feel free to use, modify, and distribute for both personal and commercial purposes.

---
