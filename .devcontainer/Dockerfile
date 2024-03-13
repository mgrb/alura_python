FROM python:3.12-alpine

RUN apk update && apk add --no-cache \
git \
curl \
zsh \
starship \
openssh \
pipx \
&& pipx install poetry

ENV PATH="/root/.local/bin:${PATH}"

COPY .zshrc /root/

ENV ZSH_THEME starship

SHELL ["/bin/zsh", "-c"]

WORKDIR /workspace
COPY ../ .

CMD ["tail", "-f", "/dev/null"]