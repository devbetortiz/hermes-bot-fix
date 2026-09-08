FROM nousresearch/hermes-agent:v2026.9.7

USER root
COPY patch_bot_mode_dm.py /tmp/patch_bot_mode_dm.py
RUN /opt/hermes/.venv/bin/python /tmp/patch_bot_mode_dm.py && rm /tmp/patch_bot_mode_dm.py

# s6 runs cont-init scripts as root before it starts Hermes. This preserves the
# base image ENTRYPOINT and command while installing the CA from /opt/data.
COPY 10-install-obsidian-ca /etc/cont-init.d/10-install-obsidian-ca
RUN chmod 0755 /etc/cont-init.d/10-install-obsidian-ca

USER root
