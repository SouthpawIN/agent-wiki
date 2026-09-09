# Senter sandbox wrapper. Hermes-Agent supplies the runtime image; this layer
# adds versioned GOOP context without touching the live Hermes installation.
ARG HERMES_BASE=hermes-agent:latest
FROM ${HERMES_BASE}

ENV HERMES_HOME=/opt/data/.hermes
ENV SENTER_GOOP_ROOT=/opt/data/goop

COPY goop/ /opt/data/goop/

WORKDIR /opt/data/goop

# Runtime credentials belong in the environment/secret manager, never in this image.
ENTRYPOINT ["hermes"]
CMD ["--tui"]
