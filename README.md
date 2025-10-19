# Sentiment-Analysis
A small Flask web app that demonstrates a sentiment-analysis dashboard for product reviews.

The app provides:

- A clean, responsive UI (Bootstrap + custom CSS) showing positive and negative review counts.
- A product image panel and summary card for quick overview.
- A comment box so users can post short comments; comments are stored in-memory (for demo purposes) and displayed on the page.


## Quick start (Windows PowerShell)

1. Activate the project's virtual environment:

```powershell
Sentiment-Analysis\env\Scripts\Activate.ps1
```

2. Start the Flask development server (the venv's python is configured in this repo):

```powershell
# from repository root
python .\app.py
```

3. Open your browser at:

```
http://127.0.0.1:5000/
```


## Files of interest

- `app.py` - Flask application. The `/` route renders the dashboard. The `/comment` POST route accepts comment submissions (stored in-memory).
- `templates/index.html` - Jinja2 template for the main dashboard (Bootstrap layout).
- `static/css/styles.css` - Custom CSS for gradients, cards, and comment styling.
- `static/products/image.png` - Product image used on the page (ensure this file exists).
- `notebooks/` - Jupyter notebooks used for dataset download and model building.
- `artifacts/sentiment_analysis.csv` - (Optional) dataset artifacts.

# Sentiment-Analysis