from typing import Any

import boto3
from botocore.client import BaseClient
from botocore.config import Config

from inference_lab.config import Settings

class BedrockClient:
    """Small wrapper around the Amazon Bedrock Runtime client."""

    def __init__(
            self, 
            settings: Settings,
            client: BaseClient | None = None,
    ) -> None:
        self._settings = settings
        self._client = client or self._create_client()
    
    def _create_client(self) -> BaseClient:
        """Create an authenticated Bedrock runtime client."""

        session = boto3.Session(
            profile_name=self._settings.aws_profile,
            region_name=self._settings.aws_region,
        )

        client_config = Config(
            connect_timeout=self._settings.request_timeout_seconds,
            read_timeout=self._settings.request_timeout_seconds,
            retries={"max_attempts": 0},
        )

        return session.client(
            service_name="bedrock-runtime",
            config=client_config,
        )
    
    def generate(self, prompt: str) -> str:
        """Send a text prompt to the configured Bedrock model."""

        response: dict[str, Any] = self._client.converse(
            modelId=self._settings.bedrock_model_id,
            messages=[
                {
                    "role": "user",
                    "content" : [
                        {
                        "text": prompt,
                        }
                    ],
                }
            ],
            inferenceConfig={
                "maxTokens": 300,
                "temperature": 0.2,
                "topP": 0.9,
            },
        )

        return response["output"]["message"]["content"][0]["text"]
