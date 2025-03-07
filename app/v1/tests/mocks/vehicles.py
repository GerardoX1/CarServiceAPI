from datetime import datetime

BASE_TIMESTAMP = int(datetime.now().timestamp() * 1000)
BASE_VEHICLES = [
    {
        "id": "cc40aa76-8381-419c-b5cb-37e708556ab7",
        "plate_number": "PDU1210",
        "brand": "CHEVROLET",
        "model": "beat",
        "year": 2025,
        "mileage": 80000,
        "status": "ACTIVE",
        "created_at": BASE_TIMESTAMP,
        "updated_at": BASE_TIMESTAMP,
        "version": "1.0.0",
    },
    {
        "id": "0dc3692c-7f65-4352-8702-941e5e01cc7b",
        "plate_number": "XYZ1201",
        "brand": "NISSAN",
        "model": "Maxima",
        "year": 2022,
        "mileage": 20000,
        "status": "ACTIVE",
        "created_at": 1741297037700,
        "updated_at": 1741297037700,
        "version": "1.0.0",
    },
]


def generate_mock_vehicle(index=0, status=None, updated_at=None, custom_data=None):
    """
    Genera un mock de vehículo basado en la lista BASE_VEHICLES.
    - index: Índice en la lista BASE_VEHICLES.
    - status: Estado personalizado.
    - updated_at: Timestamp personalizado.
    - custom_data: Diccionario para sobrescribir valores específicos.
    """
    vehicle = BASE_VEHICLES[index].copy()
    vehicle["status"] = status if status else vehicle["status"]
    vehicle["updated_at"] = updated_at if updated_at else vehicle["updated_at"]

    if custom_data:
        vehicle.update(custom_data)

    return {"vehicles": vehicle}


mock_vehicle_data = {
    key: BASE_VEHICLES[0][key]
    for key in ["plate_number", "brand", "model", "year", "mileage", "status"]
}

mock_vehicle_response = generate_mock_vehicle()

mock_vehicle_patch_data = {
    "model": "beat",
    "year": 2026,
    "mileage": 1000,
}

mock_vehicle_updated_response = generate_mock_vehicle(
    custom_data=mock_vehicle_patch_data, updated_at=1741283920936
)

mock_vehicle_detail = generate_mock_vehicle()

mock_vehicles_list = {
    "vehicles": [
        generate_mock_vehicle(index=i)["vehicles"] for i in range(len(BASE_VEHICLES))
    ],
    "page_limit": 50,
    "total_pages": 1,
    "items_count": len(BASE_VEHICLES),
}
