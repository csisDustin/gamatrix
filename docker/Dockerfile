from python:3.8

ADD dist /

ARG API_KEY=DEADBEEFF00DD00DBEEF000F5ADF00D5

ENV USER_STEAM_API_DEV_KEY=$API_KEY

RUN pip install /gamatrix*.whl

CMD [ "python", "-m", "gamatrix" ]
