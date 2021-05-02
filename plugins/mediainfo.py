# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -

• `{i}mediainfo <reply to media>`
   To get info about it.
"""

import os, time

from . import *


@ultroid_cmd(pattern="mediainfo$")
async def mi(e):
    r = await e.get_reply_message()
    if not (r and r.media):
        return await eod(e, "`Reply to any media`")
    xx = mediainfo(r.media)
    murl = r.media.stringify()
    url = make_html_telegraph("Mediainfo", "Ultroid", f"<code>{murl}</code>")
    ee = await eor(e, f"**[{xx}]({url})**\n\n`Loading More...`", link_preview=False)
    taime = time.time()
    dl = await downloader(r.file.name, r.media.document, ee, taime, "Getting Media info...")
    out, er = await bash(f"mediainfo {dl.name} --Output=HTML")
    urll = make_html_telegraph("Mediainfo", "Ultroid", out)
    os.remove(dl)
    if er:
        return await ee.edit(f"**[{xx}]({url})**", link_preview=False)
    await ee.edit(
        f"**[{xx}]({url})**\n\n[More Explained Info]({urll})", link_preview=False
    )


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
