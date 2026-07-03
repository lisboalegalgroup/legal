$files = Get-ChildItem -Filter *.html
foreach ($file in $files) {
    if ($file.Name -eq "privacidad.html") { continue }
    $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
    
    # Fix the literal backtick n
    $content = $content.Replace("`n    <meta charset=`"UTF-8`">", "`r`n    <meta charset=`"UTF-8`">")
    $content = $content.Replace("type=`"image/png`">``n    <meta", "type=`"image/png`">`r`n    <meta")

    [System.IO.File]::WriteAllText($file.FullName, $content, [System.Text.Encoding]::UTF8)
}
Write-Host "Fixed newlines."
