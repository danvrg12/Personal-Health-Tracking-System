# Personal Health Tracker

A Flask-based web application for tracking personal health metrics with user authentication and an interactive dashboard.

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Features](#features)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Description

This project combines a Flask backend with a modern HTML/CSS/JavaScript frontend to create a comprehensive personal health tracking system. Users can securely log in, track various health metrics (weight, exercise, water intake, mood), view interactive charts, and access personalized insights about their health journey.

**Problem it solves**: Managing personal health data across multiple platforms can be fragmented and insecure. This application provides a centralized, privacy-focused solution for individuals to track and analyze their health metrics over time.

## Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd personal-health-tracker
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install flask
```

4. **Create project structure**
```bash
mkdir templates static
```

5. **Set up the template file**
   - Save the HTML content as `templates/lab7.html`
   - Ensure the HTML file includes all the CSS and JavaScript inline

## Usage

1. **Start the Flask application**
```bash
python app.py
```

2. **Access the application**
   - Open your browser to `http://localhost:5000`
   - Log in with demo credentials (see Examples section)
   - Start tracking your health metrics

3. **Navigate the application**
   - **Dashboard**: View your health statistics and charts
   - **Add Record**: Input daily health metrics
   - **Records**: View and manage your health history
   - **Goals**: Set and track health goals
   - **Insights**: Get personalized health insights

## Examples

### Demo Login Credentials
```
Username: user1
Password: pass1

Username: user2
Password: pass2
```

### Adding a Health Record
1. Navigate to "Add Record" section
2. Fill in the form:
   - Date: 2024-01-15
   - Weight: 70.5 kg
   - Exercise: 30 minutes
   - Water: 2.5 liters
   - Mood: 8/10
   - Notes: "Great workout today!"
3. Click "Save Record"

### Viewing Dashboard
Access your dashboard to see:
- Total records count
- Average weight trend
- Total exercise minutes
- Interactive charts showing progress over time

## Features

- **🔐 User Authentication** - Secure login system with session management
- **📊 Interactive Dashboard** - Real-time charts and statistics
- **📝 Health Tracking** - Weight, exercise, water intake, and mood logging
- **📈 Progress Visualization** - Multi-axis charts showing trends over time
- **🎯 Goal Setting** - Set and track personal health goals
- **💡 Personalized Insights** - AI-driven health recommendations
- **📱 Responsive Design** - Works seamlessly on desktop and mobile
- **🏃‍♂️ Gym Finder** - Discover nearby fitness facilities
- **🔒 Privacy Focused** - Data stored locally in browser
- **✨ Modern UI** - Glassmorphism design with smooth animations

## API Reference

### Authentication Endpoints

#### `GET /`
Returns the login page or redirects to dashboard if already authenticated.

#### `POST /login`
Authenticates user credentials.

**Parameters:**
- `username` (string): User's username
- `password` (string): User's password

**Response:**
- Success: Redirect to `/dashboard`
- Error: Login page with error message

#### `GET /logout`
Logs out the user and clears session.

### Application Routes

#### `GET /dashboard`
Main dashboard with health statistics and charts.
**Requires authentication**

#### `GET /add_record`
Form for adding new health records.
**Requires authentication**

#### `GET /history`
View historical health records.
**Requires authentication**

#### `GET /register`
User registration page (placeholder).

### Frontend JavaScript API

The frontend includes a `HealthTracker` class with methods:
- `saveRecord()` - Save health data to localStorage
- `updateDashboard()` - Refresh dashboard statistics
- `renderChart()` - Generate Chart.js visualizations
- `editRecord(id)` - Edit existing health records
- `deleteRecord(id)` - Remove health records

## Configuration

### Flask Configuration
```python
app.secret_key = 'your_super_secret_key_here'  # Change this in production
```

### User Management
Currently uses in-memory user storage:
```python
users = {
    'user1': 'pass1',
    'user2': 'pass2'
}
```

### Health Goals (Frontend)
Default goals can be modified in the JavaScript:
```javascript
this.goals = {
    targetWeight: 70,
    weeklyExercise: 150,
}
```

## Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/database-integration
   ```
3. **Make your changes**
4. **Test thoroughly**
5. **Submit a pull request**

### Development Guidelines
- Follow PEP 8 for Python code
- Use meaningful commit messages
- Test all authentication flows
- Ensure responsive design works on mobile
- Add comments for complex frontend logic

### Potential Improvements
- Replace in-memory user storage with a database
- Add password hashing and validation
- Implement user registration functionality
- Add data export/import features
- Create REST API endpoints for mobile apps

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- **Flask** - Python web framework
- **Chart.js** - Interactive charting library
- **Font Awesome** - Icon library
- **Google Fonts (Inter)** - Typography
- **HTML5/CSS3** - Modern web standards
- **JavaScript ES6+** - Frontend interactivity

---

**⚠️ Security Note**: This is a demonstration application. For production use, implement proper password hashing, HTTPS, CSRF protection, and use a proper database instead of in-memory storage.

**📱 Health Disclaimer**: This application is for personal health tracking only and should not replace professional medical advice. Always consult healthcare professionals for medical concerns.
