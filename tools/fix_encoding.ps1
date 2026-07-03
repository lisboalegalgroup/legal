$files = Get-ChildItem -Filter *.html
foreach ($file in $files) {
    if ($file.Name -eq "privacidad.html") { continue }
    $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
    
    $content = $content.Replace("PolÃ­ticas", "Políticas")
    $content = $content.Replace("JurÃ­dico", "Jurídico")
    $content = $content.Replace("Estudio JurÃ­dico Lisboa Legal Group en Guayaquil, Ecuador. Especialistas en derecho corporativo, civil y penal.", "Estudio Jurídico Lisboa Legal Group en Guayaquil, Ecuador. Especialistas en derecho corporativo, civil y penal.")

    [System.IO.File]::WriteAllText($file.FullName, $content, [System.Text.Encoding]::UTF8)
}
Write-Host "Fixed encoding."
