# Simple URL Shortener

A simple URL shortener backend built with Flask and SQLite.

## Features

- Accepts a long URL and generates a unique short code
- Stores URL mappings in an SQLite database
- Redirects short URLs to their original destination
- Supports a JSON API
- Includes a basic frontend

## Technologies Used

- Python
- Flask
- SQLite
- HTML and CSS

## API Endpoint

### Shorten a URL

`POST /shorten`

JSON request example:

```json
{
  "url": "https://www.example.com/very-long-url"
}
```

Example response:

```json
{
  "original_url": "https://www.example.com/very-long-url",
  "short_code": "aB12Cd",
  "short_url": "http://127.0.0.1:5000/aB12Cd"
}
```

## Redirect Route

`GET /<short_code>`

Opening a generated short URL redirects the user to the original URL.

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Start the Flask server:

```bash
python app.py
```

3. Open this address in your browser:

`http://127.0.0.1:5000/`

## Project Structure

```text
simple-url-shortener/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── templates/
    └── index.html
```

## Author

Yash Kamboj
