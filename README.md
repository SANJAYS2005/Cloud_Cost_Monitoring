# CloudWise — Cloud Cost & Resource Monitor ☁️

CloudWise is a beginner-friendly portfolio project for learning Python, Flask, SQLite, REST APIs, dashboard design, and basic cloud cost concepts.

## Features
- Responsive dashboard with simulated cloud-resource readings
- CPU and memory usage overview
- Monthly cost estimator using a configurable hourly rate
- Budget status warning
- SQLite history of estimates
- JSON API endpoints: `POST /api/estimate`, `GET /api/history`, `GET /health`
- Unit tests using Python's built-in `unittest`

## Important note
This prototype uses **simulated resource data**. It is not connected to AWS, Azure, or Google Cloud, and the sample hourly rate is user-configurable rather than a provider quote. Real prices depend on service, region, instance size, usage, discounts, storage, networking, and taxes. Do not use this demo as a billing source.

## Run locally
Python 3.10+ recommended.

```bash
python -m venv .venv
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

## Run tests
```bash
python -m unittest discover -s tests -v
```

## Sample calculation
For 4 resources, ₹0.05 per resource-hour and 730 hours:
`4 × ₹0.05 × 730 = ₹146.00`

## Project structure
```text
CloudWise-Cloud-Cost-Monitor/
├── app.py
├── cost_engine.py
├── database.py
├── templates/index.html
├── static/css/style.css
├── static/js/app.js
├── tests/test_cost_engine.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Future improvements
- Connect read-only cloud billing and monitoring APIs
- Add configurable currency and provider-specific price data
- Add CSV export and date-range charts
- Add authentication and role-based access if deployed for multiple users
- Deploy with environment-based configuration and production server settings

## License
MIT. See `LICENSE`.
