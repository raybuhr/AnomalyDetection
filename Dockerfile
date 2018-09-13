FROM continuumio/anaconda3

WORKDIR play
COPY anomaly_detection/ anomaly_detection/

CMD ["ipython"]