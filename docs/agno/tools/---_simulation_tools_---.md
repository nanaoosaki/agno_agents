---
title: --- Simulation tools ---
category: tools
source_lines: 57768-57801
line_count: 33
---

# --- Simulation tools ---
def simulate_zoom_scheduling(
    agent: Agent, candidate_name: str, candidate_email: str
) -> str:
    """Simulate Zoom call scheduling"""
    # Generate a future time slot (1-7 days from now, between 10am-6pm IST)
    base_time = datetime.now() + timedelta(days=random.randint(1, 7))
    hour = random.randint(10, 17)  # 10am to 5pm
    scheduled_time = base_time.replace(hour=hour, minute=0, second=0, microsecond=0)

    # Generate fake Zoom URL
    meeting_id = random.randint(100000000, 999999999)
    zoom_url = f"https://zoom.us/j/{meeting_id}"

    result = f"✅ Zoom call scheduled successfully!\n"
    result += f"📅 Time: {scheduled_time.strftime('%Y-%m-%d %H:%M')} IST\n"
    result += f"🔗 Meeting URL: {zoom_url}\n"
    result += f"👤 Participant: {candidate_name} ({candidate_email})"

    return result


def simulate_email_sending(agent: Agent, to_email: str, subject: str, body: str) -> str:
    """Simulate email sending"""
    result = f"📧 Email sent successfully!\n"
    result += f"📮 To: {to_email}\n"
    result += f"📝 Subject: {subject}\n"
    result += f"✉️ Body length: {len(body)} characters\n"
    result += f"🕐 Sent at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    return result


