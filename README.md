This script translates hugo menu to different lanuages 

## How to use

1. Create **txt** file with original menu. Here is an example:

````
# header menu

[[menu.header]]
name = "News"
url = "/news/"
weight = 1
[[menu.header]]
name = "Categories"
url = "/categories/"
weight = 2
[[menu.header]]
name = "Games"
url = "/games/"
weight = 3

# bunuses

[[menu.footer_bonus_menu]]
name = "Bunuses"
url = "/bunuses/"
weight = 1
[[menu.footer_bonus_menu]]
name = "New Promocodes"
url = "/bonus-codes-and-promocodes/"
weight = 2

# usefull

[[menu.footer_useful_menu]]
name = "Mobile application"
url = "/mobilnaya-versiya/"
weight = 2

# help

[[menu.footer_help_menu]]
name = "Regustration"
url = "/regustration/"
weight = 1
[[menu.footer_help_menu]]
name = "Support"
url = "/tecincal-support/"
weight = 2

# footer menu

[[menu.footer_menu]]
name = "Main page"
url = "/"
weight = 1
[[menu.footer_menu]]
name = "Sitemap"
url = "/karta-saita/"
weight = 2
[[menu.footer_menu]]
name = "Contact us"
url = "/kontakty/"
weight = 3
[[menu.footer_menu]]
name = "Rules"
````

2. Pass an array of languages to translate to **langs** variable


