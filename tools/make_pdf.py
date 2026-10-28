"""1to1シート（Web版）の「1to1シート・GAINS」部分を、そのままA4のPDFに書き出す。
使い方: python3 -m http.server 8765 を起動した状態で
  python3 tools/make_pdf.py http://localhost:8765/index.html pdf/ishijima_1to1_sheet.pdf
Web版を直したら、これでPDFも同じ中身になる（旧 build_1to1_doc.py 方式は廃止）。
"""
import asyncio, sys
from playwright.async_api import async_playwright

src, out = sys.argv[1], sys.argv[2]
CSS = '''
header,.top,.side,.hero,.making-banner,.toast,footer,.pdf,section:not(#sheets),.stats{display:none!important}
html,body{background:#fff!important}
#sheets{padding:0!important;background:#fff!important;color:#14274a!important}
#sheets .sec-head{margin:0 0 10px!important}
#sheets .sec-head p,#sheets .sec-head .en{color:#5b6b82!important}
#sheets h2{color:#14274a!important}
.sheet{box-shadow:none!important;border:1px solid #d8e0ea!important}
#s-gains{break-before:page}
tr,.gains-row,figure{break-inside:avoid}
.rv{opacity:1!important;transform:none!important}
'''

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(channel='chrome')
        pg = await b.new_page(viewport={'width': 1100, 'height': 1400})
        await pg.goto(src, wait_until='networkidle')
        await pg.add_style_tag(content=CSS)
        await pg.evaluate("document.querySelectorAll('img[loading=lazy]').forEach(i=>i.loading='eager')")
        await pg.wait_for_timeout(1500)
        await pg.emulate_media(media='screen')
        await pg.pdf(path=out, format='A4', print_background=True, scale=0.62,
                     margin={'top': '10mm', 'bottom': '10mm', 'left': '8mm', 'right': '8mm'})
        await b.close()

asyncio.run(main())
