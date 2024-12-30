#!/bin/bash

# Обновление списка пакетов
sudo apt update

# Установка wget, если не установлен
if ! command -v wget &> /dev/null
then
    echo "Installing wget..."
    sudo apt install -y wget
fi

# Загрузка grpcurl
if [ ! -f "grpcurl_1.8.8_linux_x86_64.tar.gz" ]; then
    echo "Downloading grpcurl..."
    wget https://github.com/fullstorydev/grpcurl/releases/download/v1.8.8/grpcurl_1.8.8_linux_x86_64.tar.gz
fi

# Распаковка grpcurl
if [ ! -f "grpcurl" ]; then
    echo "Extracting grpcurl..."
    tar -xvf grpcurl_1.8.8_linux_x86_64.tar.gz
fi

# Перемещение grpcurl в системный каталог
if ! command -v grpcurl &> /dev/null
then
    echo "Installing grpcurl..."
    sudo mv grpcurl /usr/local/bin/
fi

# Проверка установки
if command -v grpcurl &> /dev/null
then
    echo "grpcurl successfully installed! Version: $(grpcurl --version)"
else
    echo "Failed to install grpcurl."
    exit 1
fi
