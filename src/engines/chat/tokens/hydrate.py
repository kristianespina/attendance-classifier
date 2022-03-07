def get_hydrated_response(response: str, intent_data: dict) -> str:
    hydrated_response = response

    for i, (key, value) in enumerate(intent_data.items()):
        hydrated_response = hydrated_response.replace(f"<{key}>", value)
    
    return hydrated_response