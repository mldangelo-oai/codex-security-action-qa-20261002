"""A small, dependency-free fixture that renders untrusted display names."""

from html import escape


def render_greeting(display_name: str) -> str:
    """Return an HTML fragment with the display name treated as plain text."""
    return f"<p>Hello, {escape(display_name, quote=True)}!</p>"


def greeting_response(display_name: str) -> tuple[int, dict[str, str], str]:
    """Build a synthetic response without starting a network service."""
    headers = {
        "Content-Type": "text/html; charset=utf-8",
        "Content-Security-Policy": "default-src 'none'; frame-ancestors 'none'",
        "X-Content-Type-Options": "nosniff",
    }
    return 200, headers, render_greeting(display_name)
