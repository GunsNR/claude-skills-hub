# Start the Smart OS CEO Layer (standalone mode).
# Run from the Smart OS repo root: .\scripts\start_ceo_layer.ps1
param(
    [string]$VaultPath = "",
    [int]$Port = 8100
)

$ErrorActionPreference = "Stop"

if ($VaultPath -ne "") { $env:SMARTOS_VAULT = $VaultPath }
if (-not $env:OPENROUTER_API_KEY) {
    Write-Host "OPENROUTER_API_KEY not set - running with the offline mock gateway." -ForegroundColor Yellow
    Write-Host "Tasks/tax/clients work fully; research & distill return mock text." -ForegroundColor Yellow
}

$env:SMARTOS_CEO_PORT = "$Port"
$python = ".\.venv\Scripts\python.exe"
if (-not (Test-Path $python)) { $python = "python" }

Push-Location apps\api
try {
    Write-Host "Smart OS CEO Layer -> http://localhost:$Port" -ForegroundColor Green
    & $python -m smartos_ceo.run
}
finally {
    Pop-Location
}
