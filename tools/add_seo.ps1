$files = Get-ChildItem -Filter *.html
foreach ($file in $files) {
    if ($file.Name -eq "privacidad.html") { continue }
    $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)

    # Add Favicon if missing
    if ($content -notmatch '<link rel="icon"') {
        $content = $content -replace '(?i)(<head>(?:.|\n|\r)*?)(<meta)', '$1<link rel="icon" href="ChatGPT Image 26 ago 2025, 14_11_32.png" type="image/png">`n    $2'
    }

    # Add Meta description if missing
    if ($content -notmatch '<meta name="description"') {
        $content = $content -replace '(?i)(</title>)', "$1`n    <meta name=`"description`" content=`"Estudio Jurídico Lisboa Legal Group en Guayaquil, Ecuador. Especialistas en derecho corporativo, civil y penal.`">"
    }

    # Add Privacy Policy to footer if missing
    if ($content -notmatch 'privacidad\.html') {
        $content = $content -replace '(?i)(<p>&copy; 2026 Lisboa Legal Group\.)(</p>)', '$1 | <a href="privacidad.html" style="color: #ccc; text-decoration: underline; margin-left:10px; font-size: 0.9rem;">Políticas de Privacidad</a>$2'
    }

    [System.IO.File]::WriteAllText($file.FullName, $content, [System.Text.Encoding]::UTF8)
}
Write-Host "SEO Update Completed."
