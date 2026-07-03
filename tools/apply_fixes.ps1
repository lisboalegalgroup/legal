$files = Get-ChildItem -Filter *.html
$utf8NoBom = New-Object System.Text.UTF8Encoding($False)

foreach ($file in $files) {
    if ($file.Name -eq "privacidad.html") { continue }
    
    # Read text 
    $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
    
    # 1. Fix encodings
    $content = $content.Replace("PolÃ­ticas", "Políticas")
    $content = $content.Replace("JurÃ­dico", "Jurídico")
    
    # 2. Add Favicon if missing
    if ($content -notmatch '<link rel="icon"') {
        # Using Singleline so .* matches across newlines
        $content = [System.Text.RegularExpressions.Regex]::Replace($content, '(?is)(<head>.*?)<meta charset', "`$1<link rel=`"icon`" href=`"ChatGPT Image 26 ago 2025, 14_11_32.png`" type=`"image/png`">`n    <meta charset")
    }

    # 3. Add Meta description if missing
    if ($content -notmatch '<meta name="description"') {
        $content = [System.Text.RegularExpressions.Regex]::Replace($content, '(?i)(</title>)', "`$1`n    <meta name=`"description`" content=`"Estudio Jurídico Lisboa Legal Group en Guayaquil, Ecuador. Especialistas en derecho corporativo, civil y penal.`">")
    }

    # 4. Add Privacy Policy to footer if missing
    if ($content -notmatch 'privacidad\.html') {
        $content = [System.Text.RegularExpressions.Regex]::Replace($content, '(?i)(<p>&copy; 2026 Lisboa Legal Group\.)\s*(</p>)', '$1 | <a href="privacidad.html" style="color: #ccc; text-decoration: underline; margin-left:10px; font-size: 0.9rem;">Políticas de Privacidad</a>$2')
    }

    # 5. Add Alt to images
    $evaluator = [System.Text.RegularExpressions.MatchEvaluator] {
        param($m)
        $tag = $m.Value
        if ($tag -match '(?i)alt=') { return $tag }
        if ($tag.EndsWith('/>')) {
            return $tag.Substring(0, $tag.Length - 2) + ' alt="Lisboa Legal Group"/>'
        }
        else {
            return $tag.Substring(0, $tag.Length - 1) + ' alt="Lisboa Legal Group">'
        }
    }
    $content = [System.Text.RegularExpressions.Regex]::Replace($content, '(?i)<img[^>]+>', $evaluator)

    [System.IO.File]::WriteAllText($file.FullName, $content, $utf8NoBom)
}

Write-Host "SEO Fixes Completed Successfully."
