import pandas as pd


def normalize_turkish(text: str) -> str:
    if not text:
        return ""

    replacements = {
        "ı": "i",
        "İ": "I",
        "ğ": "g",
        "Ğ": "G",
        "ü": "u",
        "Ü": "U",
        "ş": "s",
        "Ş": "S",
        "ö": "o",
        "Ö": "O",
        "ç": "c",
        "Ç": "C",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text.strip().lower()


def estimate_property_value(district: str, square_meters: float):
    try:
        df = pd.read_csv("backend/istanbul_property_reference.csv")
    except Exception:
        return {
            "estimated_value": None,
            "avg_m2_price": None,
            "district_found": False
        }

    district_normalized = normalize_turkish(district)

    df["district_normalized"] = df["district"].apply(normalize_turkish)

    match = df[df["district_normalized"] == district_normalized]

    if match.empty:
        return {
            "estimated_value": None,
            "avg_m2_price": None,
            "district_found": False
        }

    avg_m2_price = float(match.iloc[0]["avg_m2_price"])
    estimated_value = avg_m2_price * float(square_meters)

    return {
        "estimated_value": estimated_value,
        "avg_m2_price": avg_m2_price,
        "district_found": True
    }