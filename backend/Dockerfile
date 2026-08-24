FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --extra-index-url https://download.pytorch.org/whl/cpu -r requirements.txt

COPY . .

# Bake the pretrained model weights into the image so containers don't
# depend on Hugging Face Hub being reachable at runtime/cold start.
RUN python -c "from transformers import pipeline; pipeline('sentiment-analysis')"

RUN DJANGO_DEBUG=true python manage.py collectstatic --noinput

RUN chmod +x entrypoint.sh

EXPOSE 8000
ENTRYPOINT ["./entrypoint.sh"]
