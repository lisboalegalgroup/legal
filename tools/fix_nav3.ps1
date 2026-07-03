$dir = "c:\Users\ja_Ca\Desktop\lisboa legal group"
Get-ChildItem -Path $dir -Filter "*.html" -Exclude "index.html" | ForEach-Object {
    $content = Get-Content $_.FullName -Raw
    
    if ($content -notmatch "\.nav-links\s*\{") {
        $pattern = "(?m)^\s*\.nav-links\s+a\s*\{"
        $addCss = "        .nav-links {`r`n            display: flex;`r`n            gap: 25px;`r`n            list-style: none;`r`n            margin: 0;`r`n            padding: 0;`r`n            align-items: center;`r`n        }`r`n`r`n        .nav-links a {"
        
        $newContent = [System.Text.RegularExpressions.Regex]::Replace($content, $pattern, $addCss)
        if ($newContent -ne $content) {
            Set-Content -Path $_.FullName -Value $newContent -Encoding UTF8
            Write-Host "Fixed $($_.Name)"
        }
    }
    else {
        Write-Host "Skipped $($_.Name) - already fixed"
    }
}
