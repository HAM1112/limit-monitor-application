# Limit Monitor Application

This Django project includes Redis and Celery for background task processing.

## Cloning the Repository

To clone this repository, use the following steps:

1. Open a terminal.
2. Change the current working directory to the location where you want the cloned directory.
3. Run the following command:

```bash
git clone https://github.com/your-username/limit-monitor-application.git

```

## Installing Required Packages

To install the required packages, use the following steps:

    1. Navigate to the project directory:

        ```bash
            cd limit-monitor-application

        ```

    2. Install the packages using pip:

        ```bash
            pip install -r requirements.txt

        ```


## Setting Up the Environment File

To set up the environment file, follow these steps:

    Create a new file named .env in the project directory.

    Add the required environment variables to the file. For example:

        ```bash
            DEBUG=True
            SECRET_KEY=your_secret_key_here
            DATABASE_URL=your_database_url_here
            REDIS_URL=your_redis_url_here

        ```


##Running the Project

To run the project, use the following steps:

    1. Make migrations:

            ```bash
                python manage.py makemigrations
                python manage.py migrate

            ```

    2. Start the Celery worker:

            ```bash
                celery -A limit_monitor worker --loglevel=info

            ```



    3. Start the Celery beat:


             ```bash
                celery -A limit_monitor beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

             ```

    4. Run the Django development server:


            ```bash
                python manage.py runserver

            ```

    5. Access the application at http://localhost:8000/login




    
