# xrwvm-fullstack-developer-capstone

## Project Overview
An enhanced car dealership portal application built with Django backend and React frontend. This application provides comprehensive features for managing car dealerships, including dealer information, car inventory, customer reviews, and sentiment analysis.

## Repository
**GitHub Repository:** [https://github.com/Premlad1289/xrwvm-fullstack-developer-capstone](https://github.com/Premlad1289/xrwvm-fullstack-developer-capstone)

## Project Name
**fullstack_developer_capstone**

## Features
- User authentication (login, logout, registration)
- Dealer management (view all dealers, filter by state, view dealer details)
- Car inventory management (car makes and models)
- Customer reviews and ratings
- Sentiment analysis of reviews
- Admin panel for data management
- Responsive frontend interface
- RESTful API backend

## Technology Stack

### Backend
- Django 4.x
- Django REST Framework
- django-cors-headers
- Python 3.8+
- SQLite database (development)

### Frontend
- React 18.x
- React Router
- Axios for API calls
- Bootstrap for styling

### Deployment
- GitHub Actions for CI/CD
- Cloud deployment (configured)

## Project Structure
```
Full Stack Capstone Project/
├── server/
│   ├── djangoapp/          # Main Django application
│   │   ├── models.py       # Database models
│   │   ├── views.py        # API views
│   │   ├── urls.py         # URL routing
│   │   └── admin.py        # Admin configuration
│   ├── frontend/           # React frontend
│   │   ├── src/
│   │   │   ├── components/ # React components
│   │   │   └── App.js      # Main app component
│   │   └── static/         # Static HTML pages
│   │       ├── About.html
│   │       └── Contact.html
│   ├── manage.py
│   └── requirements.txt
├── README.md
└── .github/
    └── workflows/
        └── ci-cd.yml
```

## Installation

### Prerequisites
- Python 3.8 or higher
- Node.js 14.x or higher
- npm or yarn
- Git

### Backend Setup
```bash
cd server
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Frontend Setup
```bash
cd server/frontend
npm install
npm start
```

## API Endpoints

### Authentication
- POST `/api/login/` - User login
- POST `/api/logout/` - User logout
- POST `/api/register/` - User registration

### Dealers
- GET `/fetchDealers` or `/api/dealers/` - Get all dealers
- GET `/fetchDealer/<int:id>` or `/api/dealers/<int:id>/` - Get dealer by ID
- GET `/fetchDealers/<str:state>` or `/api/dealers/state/<str:state>/` - Get dealers by state

### Reviews
- GET `/fetchReviews/dealer/<int:dealer_id>` or `/api/reviews/dealer/<int:dealer_id>/` - Get reviews for a dealer
- POST `/api/reviews/` - Post a new review

### Cars
- GET `/djangoapp/get_cars` - Get car makes and models wrapped in CarModels
- GET `/api/cars/makes/` - Get all car makes
- GET `/api/cars/models/` - Get all car models

### Sentiment Analysis
- GET `/analyze/<str:text>` or POST `/api/analyze/` - Analyze review sentiment

## Admin Access
- URL: `http://localhost:8000/admin/`
- Create superuser using: `python manage.py createsuperuser`

## Testing
Run tests using:
```bash
python manage.py test
```

## Deployment
The application is deployed using GitHub Actions CI/CD pipeline. The deployment URL is saved in the `deploymentURL.txt` file.

## Grading Outputs
The following files contain verified outputs for Coursera grading criteria:
- `django_server.txt` - Django server terminal output
- `getdealerreviews.txt` - Get dealer reviews cURL output (`GET /fetchReviews/dealer/1`)
- `getalldealers.txt` - Get all dealers cURL output (`GET /fetchDealers`)
- `getdealerbyid.txt` - Get dealer by ID cURL output (`GET /fetchDealer/1`)
- `getdealersbyState.txt` - Get dealers by state cURL output (`GET /fetchDealers/Kansas`)
- `getallcarmakes.txt` - Get all car makes cURL output (`GET /djangoapp/get_cars`)
- `analyzereview.txt` - Sentiment analysis cURL output (`GET /analyze/Fantastic%20services`)
- `CI-CD.txt` - GitHub Actions workflow output
- `deploymentURL.txt` - Application deployment URL

## Contributors
- **Premlad** - Full Stack Developer ([Premlad1289](https://github.com/Premlad1289))
- **John Smith** - Backend Developer
- **Sarah Johnson** - Frontend Developer

## License
MIT License

## Contact
For questions or support, please visit the Contact Us page or email: support@cardealership.com
