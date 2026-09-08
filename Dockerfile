FROM nousresearch/hermes-agent:v2026.9.7

USER root
COPY patch_bot_mode_dm.py /tmp/patch_bot_mode_dm.py
RUN /opt/hermes/.venv/bin/python /tmp/patch_bot_mode_dm.py && rm /tmp/patch_bot_mode_dm.py
USER hermes

