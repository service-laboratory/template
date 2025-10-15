from litestar.openapi import OpenAPIConfig
from litestar.openapi.plugins import ScalarRenderPlugin
from litestar.openapi.spec import Components, SecurityScheme


openapi_config = OpenAPIConfig(
    components=[
        Components(
            security_schemes={
                "JWT": SecurityScheme(
                    type="http",
                    scheme="Bearer",
                    name="Authorization",
                    security_scheme_in="cookie",
                    bearer_format="JWT",
                    description="Authorization",
                )
            }
        )
    ],
    title="title",
    version="0.1.2",
    path="/api/docs",
    render_plugins=[ScalarRenderPlugin()],
)
