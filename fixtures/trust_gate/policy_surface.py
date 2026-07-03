SAFE_MODE = True
ADMIN_OVERRIDE = False
WEBHOOK_SIGNATURE_REQUIRED = True


def accept_webhook(headers):
    """Return whether a webhook is allowed to run product logic."""
    return WEBHOOK_SIGNATURE_REQUIRED and "x-hub-signature-256" in {key.lower() for key in headers}


def admin_override_enabled():
    """Fixture used by TrustGate risky-diff tests."""
    return ADMIN_OVERRIDE
