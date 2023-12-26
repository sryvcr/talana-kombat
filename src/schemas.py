KOMBAT_DATA_SCHEMA = {
    "type": "object",
    "properties": {
        "player1": {
            "type": "object",
            "properties": {
                "movimientos": {"type": "array", "items": {"type": "string"}},
                "golpes": {"type": "array", "items": {"type": "string"}},
            },
            "required": ["movimientos", "golpes"],
        },
        "player2": {
            "type": "object",
            "properties": {
                "movimientos": {"type": "array", "items": {"type": "string"}},
                "golpes": {"type": "array", "items": {"type": "string"}},
            },
            "required": ["movimientos", "golpes"],
        },
    },
    "required": ["player1", "player2"],
}
