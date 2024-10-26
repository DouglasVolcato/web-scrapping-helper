# web-scrapping-helper

This is a helper for complex and authenticated web scrapings that listens to all requests made by the browser while getting the content of a website. It makes it easier to view and navigate through the requests and responses made by the browser as well as the authentication process.

# How to use
- Change the callback function in the `main.py` file in order to navigate to the website page you want to scrape.
- View the requests and responses made by the browser inside the txt files in `tmp/logs` folder, they follow the same order as they were made.

## Installing
```bash
pip install selenium-wire
```

## Running
```bash
python main.py
```