# 🌾 CropMate: Smart Farming Assistant  

CropMate is an AI-powered farming assistant that helps farmers make data-driven decisions for improved crop yield, resource optimization, and sustainable farming. This project integrates cutting-edge machine learning, cloud services, and modern DevOps practices for efficient and scalable operation.  


## 🚀 Features  
- **Crop Recommendation:** Suggests optimal crops based on soil nutrients, temperature, and pH level.  
- **Weather Updates:** Provides real-time weather insights for better planning.  
- **Fertilizer Optimization:** AI-powered guidance for efficient nutrient and water usage.  
- **Scalability & Accessibility:** Built with cloud technologies for scalability and easy access.  
- **Future Expansion:** Integrating IoT devices for real-time data collection and monitoring.  

---

## 🔧 Technologies Used  

### Programming & Frameworks  
- **Python**: Backend logic and machine learning model serving.  
- **Flask**: Web-based API to serve predictions and interact with users.  

### Machine Learning  
- **Random Forest Model**: Trained on soil and environmental data for crop prediction.  

### Cloud Services (AWS)  
- **AWS S3**: For storage and deployment of application assets.  
- **AWS Lambda**: Serverless computing for executing lightweight functions.  
- **AWS EC2**: For hosting and scaling the backend application.  
- **AWS IoT Core** (Future Work): Real-time integration of data from IoT devices.  

### DevOps  
- **Docker**: Containerization for consistent deployment across environments.  
- **Jenkins**: Continuous integration and deployment pipeline for streamlined development.  

---

## 📁 Project Structure  
```plaintext
CropMate/  
├── templates/  
│   ├── index.html        # User interface  
│   └── styles.css        # Styling for the web app  
├── static/  
│   └── images/           # Images used in the application  
├── app.py                # Flask application  
├── model.pkl             # Pre-trained machine learning model  
├── Dockerfile            # Docker setup file  
├── Jenkinsfile           # Jenkins CI/CD pipeline definition  
├── requirements.txt      # Python dependencies  
└── README.md             # Project documentation  

```


## 🧑‍💻 Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/onkardamal/CropMate.git
   ```
2. Navigate to the project directory:
   ```bash
   cd CropMate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask app:
   ```bash
   python app.py
   ```
5. Access the application in your browser at `http://127.0.0.1:5000`.

---

## 📊 How It Works
1. **Input Parameters:** Users enter soil data like nitrogen, phosphorus, potassium, temperature, and pH levels.
2. **Machine Learning Model:** The backend uses a trained Random Forest model to predict the best crop.
3. **Recommendations:** The system provides crop suggestions and displays helpful farming tips.

---

## 🌱 Benefits
- Maximizes crop yield through data-driven decisions.
- Promotes sustainable farming practices.
- Saves time and resources for farmers.

---

## 📩 Contact
Developed with ❤️ by [Sai Lokesh Manchineella](mailto:sailokesh1705@gmail.com).  
Feel free to contribute or provide feedback!  

---

## 📝 License
This project is licensed under the [MIT License](LICENSE).
