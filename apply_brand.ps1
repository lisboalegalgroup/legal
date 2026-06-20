# 1. Update CSS
$cssFile = "css\style.css"
$cssContent = Get-Content $cssFile -Raw -Encoding UTF8

$cssContent = $cssContent -replace '--primary-blue:\s*#[0-9a-fA-F]+;', '--primary-blue: #0D1B2A;'
$cssContent = $cssContent -replace '--dark-bg:\s*#[0-9a-fA-F]+;', '--dark-bg: #0D1B2A;'
$cssContent = $cssContent -replace '--accent-gold:\s*#[0-9a-fA-F]+;', '--accent-gold: #B8933F;'
$cssContent = $cssContent -replace '--accent-gold-hover:\s*#[0-9a-fA-F]+;', '--accent-gold-hover: #D4AE6A;'

$cssContent = $cssContent -replace "font-family:\s*'Golos Text',\s*sans-serif;", "font-family: 'Montserrat', sans-serif;"
$cssContent = $cssContent -replace "h1,\s*h2,\s*h3,\s*h4\s*\{\s*font-family:\s*'Golos Text',\s*sans-serif;", "h1, h2, h3, h4 { font-family: 'Cormorant Garamond', serif;"

$logoCss = @"

/* --- SAN ANDRES BRAND LOGO --- */
.slg-lockup { display: flex; flex-direction: column; align-items: center; gap: 4px; padding: 5px 0; }
.slg-letters { font-family: 'Cormorant Garamond', serif; font-size: 32px; font-weight: 300; line-height: 1; letter-spacing: 0.18em; color: var(--accent-gold); margin-right: -0.18em; }
.slg-rule-wrap { display: flex; align-items: center; gap: 6px; width: 100%; justify-content: center; }
.slg-rule { width: 40px; height: 1px; background: rgba(184,147,63,0.4); }
.slg-dot { width: 3px; height: 3px; border-radius: 50%; background: var(--accent-gold); }
.slg-firm { font-family: 'Tenor Sans', sans-serif; font-size: 8px; letter-spacing: 0.3em; text-transform: uppercase; color: var(--primary-blue); white-space: nowrap; }

header.scrolled .slg-firm { color: var(--primary-blue); }
.footer-brand .slg-firm { color: var(--white); }
.footer-brand .slg-rule { background: rgba(255,255,255,0.4); }
"@

if ($cssContent -notmatch "SAN ANDRES BRAND LOGO") {
    $cssContent += $logoCss
}

[IO.File]::WriteAllText((Get-Item $cssFile).FullName, $cssContent, [System.Text.Encoding]::UTF8)

# 2. Update HTML files
$htmlFiles = Get-ChildItem -Path "." -Filter "*.html" | Where-Object { $_.Name -ne "san-andres-legal-brand(1).html" }

$oldFontLink = '<link[^>]*href="https://fonts\.googleapis\.com/css2\?family=Golos\+Text[^>]*>'
$newFontLink = '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400&family=Tenor+Sans&family=Montserrat:wght@300;400;500&display=swap" rel="stylesheet">'

$logoHtml = @"
<div class="slg-lockup">
    <div class="slg-letters">SLG</div>
    <div class="slg-rule-wrap">
        <div class="slg-rule"></div><div class="slg-dot"></div><div class="slg-rule"></div>
    </div>
    <div class="slg-firm">San Andrés Legal Group</div>
</div>
"@

foreach ($file in $htmlFiles) {
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    
    $content = $content -replace $oldFontLink, $newFontLink
    
    # Simple replacements
    $content = $content.Replace("Lisboa Legal Group", "San Andrés Legal Group")
    $content = $content.Replace("Lisboa Legal", "San Andrés Legal")
    $content = $content.Replace("Lisboa", "San Andrés")
    $content = $content.Replace("LISBOA", "SAN ANDRÉS")
    $content = $content.Replace("lisboalegalgroup@gmail.com", "info@slggroup.ec")
    
    # Regex replacement for logo image
    $content = $content -replace '<img[^>]*src="logo-full\.png"[^>]*>', $logoHtml
    
    [IO.File]::WriteAllText($file.FullName, $content, [System.Text.Encoding]::UTF8)
}

Write-Host "Applied brand update to CSS and all HTML files."
