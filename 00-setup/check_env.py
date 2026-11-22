"""Verify the toolchain and that keys load from .env."""
import os
import sys

from dotenv import load_dotenv

load_dotenv()
print(f"Python {sys.version.split()[0]}")
for key in ("LLM_API_KEY", "HF_TOKEN", "LANGSMITH_API_KEY"):
    print(f"{key}: {'set' if os.getenv(key) else 'MISSING'}")
