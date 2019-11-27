# Ubuntu Linux as the base imag
FROM ubuntu:16.04

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Add the files
ADD . /Wiki-QA-Magic

# Specify the work dir
WORKDIR /Wiki-QA-Magic

ENV SPACY_WARNING_IGNORE=W008

# Install packages 
RUN apt-get -y update && \
    apt-get -y upgrade && \
	apt-get -y install python3-pip python3-dev &&\
	pip3 install -r requirements.txt  &&\
	python3 -m spacy download en_core_web_sm &&\
 	python3 -m spacy download en_core_web_lg

# Create Excutables
CMD ["chmod 777 ask"]
CMD ["chmod 777 answer"]

ENTRYPOINT ["/bin/bash", "-c"]