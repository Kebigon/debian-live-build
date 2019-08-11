This repository contains scripts I use to build a custom Debian image with settings and programs installed for my personal usages:
* Protect my privacy
* Learn Japanese
* File encryption and synchronization


# What's installed ?

## Hosts file

[StevenBlack's hosts file][1] is installed on the system (Unified hosts + fakenews + gambling + porn + social).

*At the moment it is updated everyday at 20:00 via a cron job (/etc/cron.d/hosts). It seems not possible to have it setup directly on the image, as during the installation/live startup process, the /etc/hosts file is overriden.*

## Firefox ESR

Firefox is configured via a user.js file based on [ghacks' user.js][2].

Firefox have the below add-ons installed using [firefox-extension-manager][3]:

| Add-on                                 | License          |
| -------------------------------------- | ---------------- |
| [uBlock Origin][4]                     | GPL-3.0-only     |
| [HTTPS Everywhere][5]                  | GPL-2.0-or-later |
| [Privacy Badger][6]                    | GPL-3.0-only     |
| [Decentraleyes][7]                     | MPL-2.0          |
| [Firefox Multi-Account Containers][8]  | MPL-2.0          |
| [Rikaichamp][9]                        | MPL-2.0          |
| [Plasma Integration][10]               | GPL-3.0-only     |

## Programs from Debian's APT repository

See config/package-lists/kebigon.list.chroot

## Other programs

| Program                        | License           | Installation method                                            |
| ------------------------------ | ----------------- | -------------------------------------------------------------- |
| [firefox-extension-manager][3] | N/A               | Script config/hooks/normal/9000-firefox-extensions.hook.chroot |
| [VeraCrypt][11]                | Apache-2.0        | Script config/hooks/normal/9001-veracrypt.hook.chroot          |
| [Anki][12]                     | AGPL-3.0-or-later | Script config/hooks/normal/9002-anki.hook.chroot               |
| [FreeFileSync][13]             | GPL-3.0-only      | Directly incorporated into this repository (version 10.8)      |


[1]: https://github.com/StevenBlack/hosts
[2]: https://github.com/ghacksuserjs/ghacks-user.js
[3]: https://github.com/NicolasBernaerts/ubuntu-scripts
[4]: https://addons.mozilla.org/ja/firefox/addon/ublock-origin
[5]: https://addons.mozilla.org/ja/firefox/addon/https-everywhere
[6]: https://addons.mozilla.org/ja/firefox/addon/privacy-badger17
[7]: https://addons.mozilla.org/ja/firefox/addon/decentraleyes
[8]: https://addons.mozilla.org/ja/firefox/addon/multi-account-containers
[9]: https://addons.mozilla.org/ja/firefox/addon/rikaichamp
[10]: https://addons.mozilla.org/ja/firefox/addon/plasma-integration
[11]: https://www.veracrypt.fr
[12]: https://apps.ankiweb.net/
[13]: https://freefilesync.org/

