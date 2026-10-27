from flask import Flask, render_template, request, jsonify
from datetime import datetime
from cost_engine import estimate_monthly_cost, make_sample_resources, summarize_resources
from database import init_db, save_snapshot, get_history

app = Flask(__name__)
init_db()

@app.get("/")
def index():
    resources = make_sample_resources()
    summary = summarize_resources(resources)
    return render_template("index.html", resources=resources, summary=summary)

@app.post("/api/estimate")
def api_estimate():
    data = request.get_json(silent=True) or request.form
    try:
        hourly_rate = float(data.get("hourly_rate", 0.05))
        monthly_hours = float(data.get("monthly_hours", 730))
        budget = float(data.get("budget", 100))
        if hourly_rate < 0 or monthly_hours < 0 or budget < 0:
            raise ValueError
    except (TypeError, ValueError):
        return jsonify({"error": "Enter valid non-negative numbers."}), 400

    resources = make_sample_resources()
    total = estimate_monthly_cost(hourly_rate, monthly_hours, len(resources))
    summary = summarize_resources(resources)
    save_snapshot(total, budget, summary["avg_cpu"])
    return jsonify({
        "estimated_monthly_cost": round(total, 2),
        "budget": round(budget, 2),
        "over_budget": total > budget,
        "resource_count": len(resources),
        "avg_cpu": summary["avg_cpu"],
        "avg_memory": summary["avg_memory"],
        "status": "Budget exceeded" if total > budget else "Within budget",
        "calculation": f"{len(resources)} resources × ₹{hourly_rate:.2f}/hour × {monthly_hours:.0f} hours"
    })

@app.get("/api/history")
def api_history():
    return jsonify(get_history())

@app.get("/health")
def health():
    return jsonify({"status": "ok", "timestamp": datetime.now().isoformat(timespec="seconds")})

if __name__ == "__main__":
    app.run(debug=True)
