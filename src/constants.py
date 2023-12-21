ARNALDOR = "Arnaldor"
TONYN = "Tonyn"

MOVEMENTS = {"W", "S", "A", "D", "SD", "DSD", "SA", "ASA"}

HITS = {"P", "K"}
HIT_WORDS = {
    "P": "un puño",
    "K": "una patada",
}

CHARACTER_ATTACKS = {
    TONYN: {
        ("DSD", "P"): ("Taladoken", 3),
        ("SD", "K"): ("Remuyuken", 2),
        ("P", None): ("puño", 1),
        ("K", None): ("patada", 1),
    },
    ARNALDOR: {
        ("SA", "K"): ("Remuyuken", 3),
        ("ASA", "P"): ("Taladoken", 2),
        ("P", None): ("puño", 1),
        ("K", None): ("patada", 1),
    },
}
