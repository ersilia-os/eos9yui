FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install rdkit-pypi
RUN pip install tqdm
RUN pip install pyyml
RUN pip install torch==1.8.0
RUN pip install seaborn==0.11.0
RUN pip install scipy==1.5.2
RUN pip install scikit-learn==0.23.2

WORKDIR /repo
COPY ./repo
