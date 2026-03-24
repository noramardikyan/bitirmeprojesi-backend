from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def generate_report(output_path: str, form_data: dict, scores: dict):
    c = canvas.Canvas(output_path, pagesize=A4)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 800, "Scholarship DSS Report")

    c.setFont("Helvetica", 12)

    c.drawString(100, 760, f"Gender: {form_data.get('gender')}")
    c.drawString(100, 740, f"Parents Divorced: {form_data.get('parents_divorced')}")
    c.drawString(100, 720, f"Mother Working: {form_data.get('mother_working')}")
    c.drawString(100, 700, f"Everyone Healthy: {form_data.get('everyone_healthy')}")
    c.drawString(100, 680, f"Has Car: {form_data.get('has_car')}")
    c.drawString(100, 660, f"Has House: {form_data.get('has_house')}")
    c.drawString(100, 640, f"City: {form_data.get('city')}")
    c.drawString(100, 620, f"District: {form_data.get('district')}")
    c.drawString(100, 600, f"Square Meters: {form_data.get('square_meters')}")
    c.drawString(100, 580, f"Average m2 Price: {form_data.get('avg_m2_price')}")
    c.drawString(100, 560, f"Estimated Property Value: {form_data.get('property_estimated_value')}")

    c.drawString(100, 520, f"Total Score: {scores.get('total_score')}")
    c.drawString(100, 500, f"Priority: {scores.get('priority')}")
    c.drawString(100, 480, f"Decision: {scores.get('decision')}")

    reasons = scores.get("reasons", [])
    y = 440
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, y, "Scoring Reasons:")
    y -= 25

    c.setFont("Helvetica", 11)
    for reason in reasons:
        c.drawString(120, y, f"- {reason}")
        y -= 18

        if y < 80:
            c.showPage()
            y = 800
            c.setFont("Helvetica", 11)

    c.save()