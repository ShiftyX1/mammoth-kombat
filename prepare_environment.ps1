$envPaths = @("api", "bot", "front")

foreach ($envPath in $envPaths) {
    if (-Not (Test-Path $envPath)) {
        continue
    }

    python -m venv "$envPath\venv_$envPath"

    & "$envPath\venv_$envPath\Scripts\Activate.ps1"

    $requirementsPath = "$envPath\requirements.txt"
    if (Test-Path $requirementsPath) {
        pip install -r $requirementsPath
    } else {
        Write-Host "requirements.txt не найден в $envPath"
    }

    deactivate
}
