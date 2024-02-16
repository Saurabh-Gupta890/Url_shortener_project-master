# URL Shortener

This is a simple URL shortener application built with Django.

## Models

The application has one model, `ShortenedURL`, with the following fields:

- `long_url`: A `URLField` that stores the original URL.
- `short_code`: A `CharField` that stores the unique short code corresponding to the long URL.
- `created_at`: A `DateTimeField` that stores the date and time when the `ShortenedURL` instance was created.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/urlshortener.git
    ```

2. Navigate to the project directory:
    ```bash
    cd urlshortener
    ```

3. Install the requirements:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Start the server:
    ```bash
    python manage.py runserver
    ```

Now you can navigate to `http://localhost:8000` in your browser to use the application.

## Usage

To shorten a URL, navigate to the home page and enter your URL in the form. The application will generate a short code and display it on the page.

To visit a shortened URL, navigate to `http://localhost:8000/<short_code>`, replacing `<short_code>` with your unique short code.
