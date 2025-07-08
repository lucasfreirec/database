# 1. Usar uma imagem base oficial e leve do Python
FROM python:3.11-slim

# 2. Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# 3. Copiar o arquivo de dependências e instalá-las
# Isso é feito em um passo separado para aproveitar o cache do Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar o resto do código do projeto para o contêiner
COPY . .

# 5. Comando que será executado quando o contêiner iniciar
CMD ["python", "main.py"]