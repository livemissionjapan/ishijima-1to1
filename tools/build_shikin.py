# 資金繰り版の1to1シート（shikin.html）を組み立てる。
# 頭（CSS）と1to1シート・GAINS・フッター・スクリプトは index.html から取り、本文は tools/shikin_body.html。
import os, re
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(R, 'index.html'), encoding='utf-8').read()
body = open(os.path.join(R, 'tools', 'shikin_body.html'), encoding='utf-8').read()
css = open(os.path.join(R, 'tools', 'shikin_extra.css'), encoding='utf-8').read()
head = src[:src.index('</style>')] + css + src[src.index('</style>'):src.index('<header class="top">')]
head = head.replace('<title>石島 亮太｜飲食店専門の経理代行（BNI Trust）1to1シート</title>', '<title>石島 亮太｜資金繰り表（BNI Trust）1to1シート</title>')
sheets = src[src.index('<!-- SHEETS -->'):src.index('<!-- SECOND 1TO1 -->')]
story2 = src[src.index('<!-- STORY 2 -->'):src.index('<footer>')]
tail = src[src.index('<footer>'):]
out = head + body + '\n' + sheets + story2.replace('class="tint"', '') + tail
open(os.path.join(R, 'shikin.html'), 'w', encoding='utf-8').write(out)
print('shikin.html', len(out))
