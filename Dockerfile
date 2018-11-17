FROM ubuntu:16.04
RUN apt-get update -qqq
RUN apt-get install python-dev -y
RUN apt-get install python-pip -y
RUN pip install numpy
RUN pip install pandas
RUN pip install scipy
RUN pip install statsmodels
ADD hie_analysis.py /simon/hie_analysis.py
ENTRYPOINT ["python", "/simon/hie_analysis.py"]
