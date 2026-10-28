# 石島亮太 1to1シート（Web版）

公開URL: https://livemissionjapan.github.io/ishijima-1to1/

- `index.html` … 本体（CSS/JS同梱・外部依存はGoogle Fontsのみ）
- `img/` … 写真（元はGoogleドキュメント版1to1シートから書き出し・JPEG最適化済み）
- `pdf/ishijima_1to1_sheet.pdf` … 略歴・GAINSシート（BNI公式書式）

## 更新手順
1. `index.html` を編集（お繋ぎ文は `<pre class="msg" id="m-…">` の中身）
2. `git commit` → `git push origin main` で数十秒後に公開反映
3. お繋ぎ文の正本は `aminde-consulting-dashboards/bni/data.php` と `.claude/skills/bni-matching/SKILL.md`。**そちらを先に直してからここへ**

## PDF版の作り方（2026-10-28 更新）

PDFは **Web版の「1to1シート・GAINS」部分をそのまま書き出す**（旧 `bni/tools/build_1to1_doc.py` 方式は廃止。Web版と中身がずれ続けたため）。

```bash
python3 -m http.server 8765   # このフォルダで起動
python3 tools/make_pdf.py http://localhost:8765/index.html pdf/ishijima_1to1_sheet.pdf
```

- Chrome（Playwright の channel='chrome'）で A4・4ページ前後に書き出す
- index.html を直したら、必ずPDFも作り直してから commit・push する

## 指示文集（howto.html）

「BNIで毎週使える、AIの指示文集」。ウィークリープレゼン・1to1の準備・お礼文・お繋ぎ文・金の卵・推薦の言葉・1to1シートづくりの7本。各指示文にコピーボタン。1to1シート上部のバナーから開く。

## Googleドキュメント版

`build_1to1_doc.py` の末尾が Drive API で既存ドキュメントを上書きする。
**2026-09-22 時点で `~/.clasprc.json` のリフレッシュトークンが失効しており実行できない**（`python3 tools/gtoken.py` が 400 を返す）。
`clasp login` で再認証すれば復活する。トークンが無い間はスクリプトがHTML生成だけして正常終了するので、PDFは上記の手順で作れる。
