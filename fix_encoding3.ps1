$bad1 = "San Andr" + [char]195 + [char]169 + "s"
$good1 = "San Andr" + [char]233 + "s"
$bad2 = "SAN ANDR" + [char]195 + [char]137 + "S"
$good2 = "SAN ANDR" + [char]201 + "S"

$htmlFiles = Get-ChildItem -Path "." -Filter "*.html" | Where-Object { $_.Name -ne "san-andres-legal-brand(1).html" }
foreach ($file in $htmlFiles) {
    $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
    $content = $content.Replace($bad1, $good1)
    $content = $content.Replace($bad2, $good2)
    [System.IO.File]::WriteAllText($file.FullName, $content, [System.Text.Encoding]::UTF8)
}
Write-Host "Done"
