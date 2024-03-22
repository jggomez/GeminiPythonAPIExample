FROM python:3.10-slim as requirements-stage
WORKDIR /tmp
RUN pip install poetry
COPY poetry.lock pyproject.toml /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
FROM python:3.10-slim
WORKDIR /app
COPY --from=requirements-stage /tmp/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY src/ /app/
COPY resources/ /app/resources/
ENV PROJECT_ID="devhack-3f0c2"
ENV MODEL_NAME="gemini-1.0-pro-001"
ENV MAX_OUTPUT_TOKENS=8182
ENV TEMPERATURE=0.0
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
