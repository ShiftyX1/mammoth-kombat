# Определение путей к подкаталогам
$envPaths = @("api", "bot", "front")

# Создание виртуальных окружений и установка модулей
foreach ($envPath in $envPaths) {
    # Проверка наличия подкаталога, создание если отсутствует
    if (-Not (Test-Path $envPath)) {
        # New-Item -ItemType Directory -Path $envPath
        continue
    }

    # Создание виртуального окружения
    python -m venv "$envPath\venv_$envPath"

    # Активация виртуального окружения
    & "$envPath\venv\Scripts\Activate.ps1"

    # Установка модулей из requirements.txt, если файл существует
    $requirementsPath = "$envPath\requirements.txt"
    if (Test-Path $requirementsPath) {
        pip install -r $requirementsPath
    } else {
        Write-Host "requirements.txt не найден в $envPath"
    }

    # Деактивация виртуального окружения
    deactivate
}