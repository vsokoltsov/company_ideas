FROM python:3.6.2

ARG DEFAULT_REQUIREMENTS
ENV REQUIREMENTS $DEFAULT_REQUIREMENTS

RUN mkdir /company_ideas
WORKDIR /company_ideas

ADD ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

ADD . /company_ideas
