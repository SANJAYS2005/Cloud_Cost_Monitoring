"""Simple cost calculations and simulated resource data for CloudWise."""

def make_sample_resources():
    """Return clearly simulated cloud-resource readings for the demo dashboard."""
    return [
        {"name": "web-server-01", "type": "Virtual machine", "cpu": 34, "memory": 58, "status": "Running"},
        {"name": "api-server-01", "type": "Virtual machine", "cpu": 62, "memory": 71, "status": "Running"},
        {"name": "test-server-01", "type": "Virtual machine", "cpu": 12, "memory": 29, "status": "Review"},
        {"name": "worker-01", "type": "Compute worker", "cpu": 26, "memory": 44, "status": "Running"},
    ]

def estimate_monthly_cost(hourly_rate: float, monthly_hours: float, resource_count: int) -> float:
    """Estimate cost from a user-provided hourly rate and number of resources."""
    if hourly_rate < 0 or monthly_hours < 0 or resource_count < 0:
        raise ValueError("Inputs must be non-negative.")
    return hourly_rate * monthly_hours * resource_count

def summarize_resources(resources: list) -> dict:
    if not resources:
        return {"avg_cpu": 0, "avg_memory": 0, "count": 0}
    return {
        "avg_cpu": round(sum(r["cpu"] for r in resources) / len(resources), 1),
        "avg_memory": round(sum(r["memory"] for r in resources) / len(resources), 1),
        "count": len(resources)
    }
