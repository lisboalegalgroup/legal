$dir = "c:\Users\ja_Ca\Desktop\lisboa legal group"
Set-Location -Path $dir

$htmlFiles = Get-ChildItem -Filter "*.html" | Where-Object { $_.Name -notmatch '^google' }

$replaces = @{
    '<a href="https://www.linkedin.com/company/lisboa-legal-group/?viewAsMember=true" target="_blank">' = '<a href="https://www.linkedin.com/company/lisboa-legal-group/?viewAsMember=true" target="_blank" aria-label="LinkedIn Lisboa Legal Group">'
    '<a href="https://www.instagram.com/lisboalegalgroup/" target="_blank">' = '<a href="https://www.instagram.com/lisboalegalgroup/" target="_blank" aria-label="Instagram Lisboa Legal Group">'
    '<a href="https://www.facebook.com/profile.php?id=61581507116446" target="_blank">' = '<a href="https://www.facebook.com/profile.php?id=61581507116446" target="_blank" aria-label="Facebook Lisboa Legal Group">'
    '<a href="https://wa.me/593990967952" target="_blank" class="whatsapp-float">' = '<a href="https://wa.me/593990967952" target="_blank" class="whatsapp-float" aria-label="Chat en WhatsApp">'
}

foreach ($file in $htmlFiles) {
    $content = Get-Content -Raw -Path $file.FullName -Encoding UTF8
    $newContent = $content
    foreach ($key in $replaces.Keys) {
        $newContent = $newContent.Replace($key, $replaces[$key])
    }
    
    if ($newContent -ne $content) {
        $Utf8NoBomEncoding = New-Object System.Text.UTF8Encoding $False
        [System.IO.File]::WriteAllText($file.FullName, $newContent, $Utf8NoBomEncoding)
        Write-Host "Updated $($file.Name)"
    }
}
Write-Host "Done adding aria-labels."
