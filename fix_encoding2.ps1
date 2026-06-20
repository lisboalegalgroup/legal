$htmlFiles = Get-ChildItem -Path "." -Filter "*.html"

$corrupted1 = "Andr" + [char]0x00C3 + [char]0x00A9 + "s"
$fixed1 = "Andr" + [char]0x00E9 + "s"

$corrupted2 = "ANDR" + [char]0x00C3 + [char]0x2030 + "S" # Ã‰ is 0xC3 0x89 (0x2030 is per mille? 0x89 is not a printable ansi always, wait... Ã‰ is C3 89)
# Let's just be safer by matching regex: "San Andr.*?s" -> "San Andrés"
$fixed2 = "ANDR" + [char]0x00C9 + "S"

foreach ($file in $htmlFiles) {
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    
    $content = $content -replace "San AndrÃ©s", ("San Andr" + [char]0x00E9 + "s")
    $content = $content -replace "SAN ANDRÃ‰S", ("SAN ANDR" + [char]0x00C9 + "S")
    
    # Just in case, let's catch any weird "San Andr" + something + "s" that's broken
    # but the explicit string replacement above should work if the file was saved as UTF8
    
    [IO.File]::WriteAllText($file.FullName, $content, [System.Text.Encoding]::UTF8)
}

Write-Host "Encoding fixed."
