# Django Zobo

This Django-based project provides a simple but efficient platform for managing products and handling the checkout process for customers. It includes key functionalities for adding and updating products, viewing product details, checking out products, and tracking order history. The system also includes user authentication, filtering, and pagination for improved usability.

### Getting Started

These instructions will guide you through setting up Django Zobo on your local machine for development and testing purposes. This guide assumes you are working on a Windows environment. Mac and Linux users can adapt the commands accordingly.

### Prerequisites

Below are the dependencies for the project. For quicker installation, please refer to the [requirements.txt](requirements.txt) file.
- [Python](https://www.python.org/downloads/) - The programming language used to build the backend of the application.
- [Django](https://www.djangoproject.com/download/) - The web framework that powers the server-side logic, database models, and URL routing.
- [Visual Studio Code](https://code.visualstudio.com/) -  A lightweight, flexible code editor recommended for writing and managing the project code.
- [Django Widget Tweaks](https://pypi.org/project/django-widget-tweaks/) - A Django template tag library used to customize form fields directly in templates.
- [Django Filter](https://pypi.org/project/django-filter/) - Adds filtering capabilities to Django views, making it easy to implement search and filter functionality.
- [Requests](https://pypi.org/project/requests/) - A simple and elegant HTTP library for Python, used to send HTTP/1.1 requests with methods like GET and POST. It simplifies interacting with external APIs.

### Installing

Create and initialize a virtual environment (optional)

    pip install virtualenv
    virtualenv zobo_env
    cd zobo_env
    Scripts\activate

Clone the Repository

    clone https://github.com/chidiohiri/django-zobo.git
    cd django-zobo

Move the project into the virtual environment, then install dependencies. The project dependencies can found in [requirements.txt](requirements.txt)

    pip install -r requirements.txt

Migrate all tables to the Sqlite3 DB

    python manage.py makemigrations
    python manage.py migrate

Create/Login to Paystack account, and get secret and public key, then add it to the settings.py file (see file ending)

    PAYSTACK_SECRET_KEY = ''
    PAYSTACK_PUBLIC_KEY = ''

Create a super user. This account will be used to access the admin dashboard, and add product.

    python manage.py createsuperuser

Run server on your terminal (cmd or powershell). Open your browser and navigate to http://127.0.0.1:8000/ to access the application.

    python manage.py runserver

### Core Features

- User Authentication and Authorization: Users must be logged in to perform actions like adding or updating products. The system ensures that each user is associated with their own products, and permissions are managed based on their login status.

- Product Management: A simple form allows users to add new products. Only authorized users can create and update their products, with each product linked to the user’s account for easy tracking.

- Checkout Process: A checkout form enables customers to purchase products. The total amount is calculated based on the product’s price and the selected quantity, with additional shipping costs applied. A unique checkout ID is stored in the session to handle the payment process.

- Order History: Users can view their past orders, which are displayed in a filtered and paginated list. The history can be sorted and narrowed based on the user's preferences, showing only the orders that meet the filtering criteria.

- Feedback and Messaging: The system uses Django’s messaging framework to notify users about the success or failure of their actions, ensuring clear communication and guiding users through the process.

- Filtering and Pagination for Order History: The order history page allows users to filter orders by various criteria and paginates the results to ensure easy navigation through large sets of data.

### Deployment

For production deployment, you will need to configure your application with a production-grade database (such as PostgreSQL), static file handling, and secure hosting. You may refer to the official [Django Documentation](https://docs.djangoproject.com/en/5.1/howto/deployment/) on deployment

### Authors

  - **Chidi Ohiri** - *For updates, networking, or feedback, feel free to connect:* -
    [Linkedin](https://www.linkedin.com/in/chidiebere-ohiri/)

### License

This project is licensed under the [MIT LICENSE](LICENSE.md), which permits reuse, modification, and distribution with proper attribution.

### Acknowledgments

  - Guido van Rossum, the creator of Python
  - The Django core team and community for building and maintaining such a robust framework
  - Developers and open-source contributors whose work inspired or supported the development of this project

