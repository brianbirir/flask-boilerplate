from src import create_app


if __name__ == "__main__":
    """
    This module should only bes used for development when running this application using the Flask webs server.
    Running this is in production is not recommend hence look at other production level WSGI like Gunicorn
    """
    create_app('config.DevelopmentConfig').run('0.0.0.0')
