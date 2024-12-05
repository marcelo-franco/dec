ARG storeId

FROM python:alpine3.7
COPY . /usr/share/app
WORKDIR /usr/share/app
#RUN pip install -r requirements.txt
CMD python ./loggen.py $storeId