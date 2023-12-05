# -*- coding: utf-8 -*-
"""
Created on Tue Dec 5 13:04:10 2023

@author: simja
"""

import webbrowser

html_content = """
<!-- Your HTML code here -->
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Am I HTML already?</title>
</head>
<body>
<h1>Aanschouw mijn verlanglijstje</h1>

<p>Op mijn lijstje staat:</p>
<ol>
    <ul>Bonsai boom <em>(echt of van LEGO, makkelijk te onderhouden)</em></ul>
    <ul>Google home mini</ul>
    <ul>Simpel minimalistisch toetsenbord</ul>
    <ul>Laptop houder<em> (een soort traytje voor mijn laptop waar ik spullen zoals toetsenbord kan opslaan)</em></ul>
    <ul>Zeven korte beschouwingen over natuurkunde - Carlo Rovelli </ul>
    <ul>Potjes voor spulletjes <em>(niet noodzakelijk)</em></ul>
    <ul>Sokken</ul>
    <ul>Goede draadloze koptelefoon<em>, zwart, bluetooth, overear</em></ul>
    <ul>Hoedjes/dopjes/pionetjes<em> (voor voetbal)</em></ul>
    <ul>Hue ledstrips+bridge <em>(bij elkaar best duur)</em></ul>
    <ul>Laptop hoes cover<em> (doorzichtig, 15-inch windows)</em></ul>
    <ul>Weekend tas</ul>
    <ul>Comfortabele pyjama broek</ul>
    <ul>Canon EF lens 24mm-200mm<em> (best duur)</em></ul>
</ol>

<h3> Als iets niet duidelijk is kan er altijd contact worden opgenomen, ik ben te vinden</h3>

</body>
</html>
"""

# GitHub Pages link of your repository
github_pages_link = "https://simja.github.io/your-repository-name/"

file_path = "index.html"

with open(file_path, "w", encoding="utf-8") as html_file:
    html_file.write(html_content)

webbrowser.open(github_pages_link)
