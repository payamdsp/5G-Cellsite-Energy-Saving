import uuid, time, random, json

def generate_cell_data(cell_id, gn_id):
    # Dummy MCC/MNC, random load/traffic
    return {
        "cell_id": cell_id,
        "gNodeB_id": gn_id,
        "MCC": "123", "MNC": "45",
        "timestamp": int(time.time()),
        "traffic_load": random.uniform(0, 1),
        "user_count": random.randint(10, 500),
        "biometric_pattern": random.random(),
        "context": {"device_fingerprint": str(uuid.uuid4()), "location_zone": random.randint(1, 100)}
    }

if __name__ == "__main__":
    n_cells = 15000
    n_gnb = 5000
    for cell in range(n_cells):
        gn = f"gNB_{cell % n_gnb}"
        data = generate_cell_data(f"cell_{cell}", gn)
        print(json.dumps(data))