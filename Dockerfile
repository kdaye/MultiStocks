FROM metacubex/mihomo

# 安装Python和创建虚拟环境
RUN apk add --no-cache python3 py3-pip && \
    python3 -m venv /app/venv

# 安装依赖
COPY requirements.txt /app/
RUN . /app/venv/bin/activate && pip install -r /app/requirements.txt

COPY convert_config.py /app/convert_config.py

WORKDIR /app

# 设置环境变量
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# 运行时的入口点
ENTRYPOINT ["sh", "-c", "python3 /app/convert_config.py && /mihomo --config /root/.config/mihomo/config.yaml start"]
