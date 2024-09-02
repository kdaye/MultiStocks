FROM metacubex/mihomo

RUN apk add --no-cache python3 py3-pip && pip3 install requests pyyaml

COPY convert_config.py /app/convert_config.py

WORKDIR /app

# 运行时的入口点
ENTRYPOINT ["sh", "-c", "python3 /app/convert_config.py && /mihomo --config /root/.config/mihomo/config.yaml start"]
