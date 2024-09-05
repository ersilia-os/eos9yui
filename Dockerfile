FROM bentoml/model-server:0.11.0-py310
MAINTAINER ersilia

RUN pip install rdkit==2024.3.5
RUN pip install pandas==2.2.2
RUN pip install tqdm==4.66.5
RUN pip install pyyml==0.0.2
RUN pip install torch==2.4.1 --index-url https://download.pytorch.org/whl/cpu
RUN pip install scipy==1.14.1
RUN pip install scikit-learn==1.5.1

WORKDIR /repo
COPY ./repo
