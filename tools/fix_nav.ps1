$dir = "c:\Users\ja_Ca\Desktop\lisboa legal group"
$addCss = "        .nav-links {`n            display: flex;`n            gap: 25px;`n            list-style: none;`n            margin: 0;`n            padding: 0;`n            align-items: center;`n        }`n`n        .nav-links a {"

Get-ChildItem -Path $dir -Filter "*.html" -Exclude "index.html" | ForEach-Object {
    $content = Get-Content $_.FullName -Raw
    if ($content -notmatch "\.nav-links \{") {
        $content = $content -replace "        \.nav-links a \{", $addCss
        Set-Content -Path $_.FullName -Value $content -Encoding UTF8
        Write-Host "Fixed $_"
    }
    else {
        Write-Host "Skipped $_"
    }
}
