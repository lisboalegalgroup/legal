$dir = "c:\Users\ja_Ca\Desktop\lisboa legal group"
Set-Location -Path $dir

if (-not (Test-Path -Path "css")) {
    New-Item -ItemType Directory -Path "css" | Out-Null
}

$indexContent = Get-Content -Raw -Path "index.html" -Encoding UTF8
if ($indexContent -match '(?s)<style>(.*?)</style>') {
    $cssContent = $matches[1].Trim()
    Set-Content -Path "css\style.css" -Value $cssContent -Encoding UTF8
    Write-Host "CSS extracted to css\style.css"
} else {
    Write-Host "Could not find <style> block in index.html"
    exit
}

$linkTag = '<link rel="stylesheet" href="css/style.css">'
$htmlFiles = Get-ChildItem -Filter "*.html" | Where-Object { $_.Name -notmatch '^google' }

foreach ($file in $htmlFiles) {
    $content = Get-Content -Raw -Path $file.FullName -Encoding UTF8
    $newContent = $content -replace '(?s)<style>.*?</style>', $linkTag
    if ($newContent -ne $content) {
        # Para evitar problemas con BOM, usaremos utf8 sin BOM en PS 5.1
        $Utf8NoBomEncoding = New-Object System.Text.UTF8Encoding $False
        [System.IO.File]::WriteAllText($file.FullName, $newContent, $Utf8NoBomEncoding)
        Write-Host "Updated $($file.Name)"
    } else {
        Write-Host "No inline <style> found in $($file.Name) (or already updated)"
    }
}
Write-Host "Done extracting CSS."
