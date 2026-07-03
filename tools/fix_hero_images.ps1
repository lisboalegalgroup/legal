$files = @(
    "derecho-administrativo.html",
    "derecho-civil.html",
    "derecho-constitucional.html",
    "derecho-de-familia.html",
    "derecho-laboral.html",
    "derecho-penal.html",
    "derecho-procesal.html",
    "derecho-societario.html",
    "consultoria-tributaria.html",
    "compliance.html",
    "herencias-y-sucesiones.html"
)

$utf8NoBom = New-Object System.Text.UTF8Encoding $False

foreach ($f in $files) {
    try {
        $old_content = git show b3765b799871a5334d1ea748335dfac1e04bea1f:$f
        
        $img_url = $null
        $joined_content = $old_content -join "`n"
        if ($joined_content -match "(?s)\.area-hero\s*\{.*?url\(['""]?(.*?)['""]?\)") {
            $img_url = $matches[1]
            Write-Host "File $f had image $img_url"
            
            $absPath = Join-Path $PWD $f
            $current_content = [System.IO.File]::ReadAllText($absPath, $utf8NoBom)
            
            $inline_style = "<section class=""area-hero"" style=""background-image: linear-gradient(rgba(5, 20, 42, 0.85), rgba(5, 20, 42, 0.85)), url('$img_url');"">"
            
            $new_content = $current_content.Replace('<section class="area-hero">', $inline_style)
            [System.IO.File]::WriteAllText($absPath, $new_content, $utf8NoBom)
            Write-Host "Updated $f successfully with correct encoding."
        } else {
            Write-Host "Could not find original image for $f"
        }
    } catch {
        Write-Host "Error processing $($f): $_"
    }
}
