"""Service app configuration."""
from typing import Any

from pydantic import BaseSettings, Field, validator
from pydantic.networks import AnyHttpUrl, MongoDsn


class ServiceSettings(BaseSettings):
    """Service app configuration."""

    base_url: AnyHttpUrl = Field(  # type: ignore[assignment]
        "http://onto-ns.com/meta",
        description="Base URL, where the service is running.",
    )
    mongo_uri: MongoDsn = Field(  # type: ignore[assignment]
        "mongodb://localhost:27017",
        description="URI for the MongoDB cluster/server.",
    )

    @validator("base_url", pre=True)
    def _strip_ending_slashes(cls, value: Any) -> str:
        """Strip any end forward slashes."""
        if not isinstance(value, str):
            raise TypeError("Expected a string for `base_url`.")
        return value.rstrip("/")

    class Config:
        """Pydantic configuraiton for the settings."""

        env_prefix = "entity_service_"


CONFIG = ServiceSettings()
