$files = Get-ChildItem -Filter "*.html"
foreach ($file in $files) {
    if ($file.Name -ne "index.html" -and $file.Name -ne "areas-de-practica.html" -and $file.Name -ne "procesal.html") {
        $content = Get-Content $file.FullName -Raw
        $newContent = $content -replace '(?m)^\s*<li><a href="procesal\.html".*?>Derecho Procesal \(COGEP\)</a></li>\s*$', ''
        Set-Content -Path $file.FullName -Value $newContent -Encoding UTF8
    }
}
