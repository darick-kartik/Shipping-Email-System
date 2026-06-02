def validate_tonnage(data):

    required_fields = [
        "vessel_name",
        "open_port"
    ]

    missing_fields = []

    for field in required_fields:

        if field not in data:
            missing_fields.append(field)

    data["missing_fields"] = missing_fields

    return data