FROM python:2.7
MAINTAINER Veeresh Kamble 'veereshkamble7@gmail.com'
COPY . /Assignment1
WORKDIR /Assignment1
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
