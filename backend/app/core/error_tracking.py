import sentry_sdk
from sentry_sdk.integrations.litestar import LitestarIntegration
from .settings import settings


def init_tracing():
    sentry_sdk.init(
        settings.sentry_dsn,
        send_default_pii=True,
        max_request_body_size="always",
        # Setting up the release is highly recommended. The SDK will try to
        # infer it, but explicitly setting it is more reliable:
        # release=...,
        traces_sample_rate=0,
        integrations=[
            LitestarIntegration(
                failed_request_status_codes={403, *range(500, 599)},
            ),
        ],
    )
