import fastapi
from fastapi.middleware.cors import CORSMiddleware
from src.api.endpoints import router as api_endpoint_router
from src.config.manager import settings


def initialize_account_application() -> fastapi.FastAPI:
    app = fastapi.FastAPI(**settings.set_account_app_attributes)  # type: ignore

    # ✅ Add root route for browser testing
    @app.get("/")
    def root():
        return {"message": "Account Service is Running ✅"}

    # ✅ Optional: Add health check endpoint
    @app.get("/health")
    def health_check():
        return {"status": "healthy"}

    # Middleware setup
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=settings.IS_ALLOWED_CREDENTIALS,
        allow_methods=settings.ALLOWED_METHODS,
        allow_headers=settings.ALLOWED_HEADERS,
    )

    # Include all API endpoints with prefix
    app.include_router(router=api_endpoint_router, prefix=settings.API_PREFIX)

    return app


app: fastapi.FastAPI = initialize_account_application()
