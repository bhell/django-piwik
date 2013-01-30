django-piwik - Application to include Piwik analytics to a Django site

This app adds basic support for [Piwik web analytics](http://piwik.org/) to a Django web site:

- [Install Piwik](http://piwik.org/docs/installation/). Yes, you need PHP. But this is a Non-Evil PHP App™.
- Add a site in Piwik for the site to be tracked. Write down the number by which Piwik recognises the site.
- Add `piwik` to `INSTALLED_APPS`.
- Sync database.
- Set up a `site` for your Django web site (if you don't already have one)
- In the admin you should find a Piwik site analysis table.
- Add an entry for your site. The Piwik base URL is where `piwik.php` can be accessed.  The Piwik site number is the number you wrote down earlier. The preview does not work yet.
- `{% load piwik_tags %}` in your base html template and add `{% piwik_tracking_code %}` either before the `<body>` closing tag, or in the `<head>`.
- Done.

Have fun. BSD licensed.
