FROM public.ecr.aws/lambda/python:3.9-slim

RUN mkdir -p /app
COPY ./wikibot.py /app/
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
WORKDIR /app
EXPOSE 8000
CMD ["uvicorn", "wikibot:app", "--host", "0.0.0.0", "--port", "8000"]
ENTRYPOINT ["python", "wikibot.py"]