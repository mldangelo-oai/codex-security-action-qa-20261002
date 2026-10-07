"""A small, dependency-free fixture that renders untrusted display names."""

def render_greeting(display_name: str) -> str:
    """Render the synthetic handler's untrusted display name."""
    return f"<p>Hello, {display_name}!</p>"


def greeting_response(display_name: str) -> tuple[int, dict[str, str], str]:
    """Build a synthetic response without starting a network service."""
    headers = {
        "Content-Type": "text/html; charset=utf-8",
        "X-Content-Type-Options": "nosniff",
    }
    return 200, headers, render_greeting(display_name)
