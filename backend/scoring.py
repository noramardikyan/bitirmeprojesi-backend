def compute_scores(form_data: dict):
    score = 0
    reasons = []

    gender = form_data.get("gender")
    parents_divorced = form_data.get("parents_divorced")
    mother_working = form_data.get("mother_working")
    everyone_healthy = form_data.get("everyone_healthy")
    has_car = form_data.get("has_car")
    has_house = form_data.get("has_house")
    property_value = form_data.get("property_estimated_value")

    # 1) Gender
    if gender == "female":
        score += 60
        reasons.append("Female applicant priority applied")
    elif gender == "male":
        score += 40
        reasons.append("Male applicant baseline applied")

    # 2) Parents divorced
    if parents_divorced == "yes":
        score += 10
        reasons.append("Parents are divorced")

    # 3) Mother working
    if mother_working == "no":
        score += 10
        reasons.append("Mother is not working")

    # 4) Family health condition
    if everyone_healthy == "no":
        score += 10
        reasons.append("Health-related disadvantage in family")

    # 5) Car ownership
    if has_car == "no":
        score += 5
        reasons.append("No car ownership")

    # 6) House ownership
    if has_house == "no":
        score += 5
        reasons.append("No house ownership")

    # 7) Property valuation effect
    if property_value:
        try:
            property_value = float(property_value)

            if property_value < 3_000_000:
                score += 20
                reasons.append("Low property value → financial need")
            elif property_value < 7_000_000:
                score += 10
                reasons.append("Medium property value")
            else:
                score -= 10
                reasons.append("High property value → lower priority")

        except Exception:
            reasons.append("Property valuation could not be processed")

    # Clamp score
    score = max(0, min(score, 100))

    # Final classification
    if score >= 80:
        priority = "High Priority"
        decision = "Accepted"
    elif score >= 60:
        priority = "Medium Priority"
        decision = "Under Review"
    else:
        priority = "Low Priority"
        decision = "Rejected"

    return {
        "total_score": score,
        "priority": priority,
        "decision": decision,
        "reasons": reasons
    }