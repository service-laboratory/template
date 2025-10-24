import sentry_sdk
from sentry_sdk.integrations.litestar import LitestarIntegration

from .settings import settings


def init_error_tracking():
    sentry_sdk.init(
        settings.sentry_dsn,
        send_default_pii=True,
        max_request_body_size="always",
        traces_sample_rate=0,
        integrations=[
            LitestarIntegration(
                failed_request_status_codes={403, *range(500, 599)},
            ),
        ],
    )
