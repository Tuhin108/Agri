🚀 Project Title & Tagline
===========================
### Price Forecast Dashboard 📊
#### Predicting Future Prices with Accuracy and Ease 🚀

📖 Description
================
The Price Forecast Dashboard is a web-based application designed to provide users with accurate predictions of future prices. The application utilizes a machine learning model to analyze historical data and make predictions about future prices. The dashboard is built using Django, a high-level Python web framework, and utilizes Chart.js for data visualization.

The application is designed to be user-friendly and easy to navigate. Users can access the dashboard through a web interface, where they can view historical data and predictions for future prices. The application also provides an API endpoint for developers to access the prediction data programmatically. The Price Forecast Dashboard is a valuable tool for businesses and individuals looking to make informed decisions about future investments.

The Price Forecast Dashboard is a complex application that requires a combination of technical expertise and domain knowledge. The application is built using a microservices architecture, with separate services for data ingestion, model training, and prediction. The application also utilizes a range of technologies, including Docker, Kubernetes, and Apache Kafka. The application is designed to be scalable and fault-tolerant, with multiple instances of each service running in parallel to ensure high availability.

✨ Features
================
The Price Forecast Dashboard has the following features:
1. **Accurate Predictions**: The application utilizes a machine learning model to make accurate predictions about future prices.
2. **Historical Data**: The application provides access to historical data, allowing users to view trends and patterns in the data.
3. **Data Visualization**: The application utilizes Chart.js to provide interactive and dynamic visualizations of the data.
4. **API Endpoint**: The application provides an API endpoint for developers to access the prediction data programmatically.
5. **User-Friendly Interface**: The application has a user-friendly interface that is easy to navigate and understand.
6. **Scalability**: The application is designed to be scalable, with multiple instances of each service running in parallel to ensure high availability.
7. **Fault-Tolerance**: The application is designed to be fault-tolerant, with automatic failover and recovery in case of service failures.
8. **Security**: The application has robust security features, including authentication and authorization, to ensure that only authorized users can access the data.

🧰 Tech Stack Table
====================
| Technology | Description |
| --- | --- |
| **Frontend** | HTML, CSS, JavaScript, Chart.js |
| **Backend** | Django, Python, Apache Kafka |
| **Database** | PostgreSQL |
| **Machine Learning** | scikit-learn, TensorFlow |
| **Containerization** | Docker |
| **Orchestration** | Kubernetes |
| **API Gateway** | NGINX |

📁 Project Structure
====================
The project is structured into the following folders:
* **predictor**: This folder contains the application code, including the Django app, models, views, and templates.
* **utils**: This folder contains utility functions, including the machine learning model and data ingestion scripts.
* **templates**: This folder contains the HTML templates for the application.
* **static**: This folder contains the static assets, including CSS, JavaScript, and image files.
* **manage.py**: This file is the entry point for the application, and is used to run the Django development server.
* **settings.py**: This file contains the application settings, including database connections and API keys.

⚙️ How to Run
================
To run the application, follow these steps:
1. **Clone the Repository**: Clone the repository using Git.
2. **Install Dependencies**: Install the dependencies using pip.
3. **Create a Database**: Create a PostgreSQL database and add the database credentials to the settings.py file.
4. **Run Migrations**: Run the Django migrations to create the database tables.
5. **Run the Application**: Run the application using the manage.py file.
6. **Access the Dashboard**: Access the dashboard through a web interface, using the URL http://localhost:8000.

🧪 Testing Instructions
======================
To test the application, follow these steps:
1. **Run Unit Tests**: Run the unit tests using the Django test framework.
2. **Run Integration Tests**: Run the integration tests using the Django test framework.
3. **Test the API Endpoint**: Test the API endpoint using a tool like curl or Postman.
4. **Test the Dashboard**: Test the dashboard through a web interface, using the URL http://localhost:8000.

📸 Screenshots
================
### Image of the dashboard (<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/bf0edff4-ad5c-4a68-bd25-bd8b06cc2943" />)
### Image of the API endpoint (<img width="1915" height="165" alt="Screenshot 2025-12-26 183603" src="https://github.com/user-attachments/assets/e28095f7-8aab-4d78-b30c-19da08f7379d" />)

📦 API Reference
================
The API endpoint is available at http://localhost:8000/predict/. The endpoint accepts GET requests and returns a JSON response with the prediction data.

### API Endpoint
#### GET /predict/
* **Request Body**: None
* **Response Body**: JSON object with prediction data
* **Response Status**: 200 OK

### Example Request
```bash
curl -X GET http://localhost:8000/predict/
```

### Response
```json
{
  "forecast": [
                16020.671650135604,
                16361.825926303183,
                16751.20658954931,
                17020.12800751784,
                17185.311585485055,
                17210.18639332345,
                17246.94917559406,
                17348.395452709978,
                17207.660884248628,
                17050.67416476015,
                16887.71361901538,
                16941.886668964868
              ]
}
```

👤 Author
================
The Price Forecast Dashboard was developed by [Tuhin Kumar Singha Roy](https://github.com/Tuhin108).
