# Full Stack Reporting Tool

This is a full-stack application that allows users to define custom reporting layouts, which include custom text, images, tabular data, and graphs. The application consists of a React frontend and a Python (Flask) backend. Users can save, edit, delete, and visualize these layouts with sample data.

## Prerequisites

Before you start, make sure you have the following installed on your machine:

- [React.js](https://nodejs.org/) (for frontend)
- [Python 3](https://www.python.org/) (for backend)

---

## Setup and Running the Backend (Flask)

1. **Navigate to the backend directory**:
    ```bash
    cd backend
    ```

2. **Create a virtual environment** (recommended but optional):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install backend dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask server**:
    ```bash
    python app.py
    ```

5. The Flask server should now be running on `http://localhost:5000`.

---

## Setup and Running the Frontend (React)

1. **Navigate to the reporting-tool directory**:
    ```bash
    cd reporting-tool
    ```

2. **Install frontend dependencies**:
    ```bash
    npm install
    ```

3. **Start the React development server**:
    ```bash
    npm start
    ```

4. The React app should now be running on `http://localhost:3000`.

---

## Usage

- **Frontend**: Access the React frontend on `http://localhost:3000`. Here you can create and manage custom reporting layouts.
- **Backend**: The Flask API runs on `http://localhost:5000` and handles saving, retrieving, and deleting the reports.

### API Endpoints

- `POST /api/reports`: Save a new report layout.
- `GET /api/reports/random`: Generate a random report layout with sample data.
- `GET /api/reports/<id>`: Retrieve a specific report layout for editing.

---

## Important Notes

- Ensure that both the frontend and backend servers are running at the same time for the application to function correctly.
- If you encounter issues with cross-origin requests, ensure that CORS is properly configured in the Flask backend.
- To stop the backend server, use `CTRL + C` in the terminal running the Flask app.
- To stop the frontend server, use `CTRL + C` in the terminal running the React app.

---

## Troubleshooting

1. **Backend issues**: If you encounter errors while running the Flask backend, ensure that all required dependencies are installed by running:
    ```bash
    pip install -r requirements.txt
    ```

2. **Frontend issues**: If you encounter errors while running the React frontend, make sure all Node modules are installed by running:
    ```bash
    npm install
    ```

3. **Environment variables**: If you need to configure environment variables (e.g., API URLs), place them in a `.env` file in the frontend folder.

---

## Contributing

Feel free to fork this repository and submit pull requests with improvements!

---

## License

This project is licensed under the MIT License.
