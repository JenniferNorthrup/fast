FROM ghcr.io/astral-sh/uv:python3.12-trixie-slim

WORKDIR /app


# ---- environment ----
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8000 \
    UV_PROJECT_ENVIRONMENT=/app/.venv \
    PATH="app/.venv/bin:$PATH"

# ---- system user (optional but good practice) ----
RUN groupadd --system nonroot && useradd --system --gid nonroot nonroot

# ---- install deps first (better caching) ----
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    uv sync --locked --no-install-project

# ---- copy app ----
COPY . .

# ---- install project ----
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]