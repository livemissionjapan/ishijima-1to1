# 石島亮太 1to1シート（Web版）

公開URL: https://livemissionjapan.github.io/ishijima-1to1/

- `index.html` … 本体（CSS/JS同梱・外部依存はGoogle Fontsのみ）
- `img/` … 写真（元はGoogleドキュメント版1to1シートから書き出し・JPEG最適化済み）
- `pdf/ishijima_1to1_sheet.pdf` … 略歴・GAINSシート（BNI公式書式）

## 更新手順
1. `index.html` を編集（お繋ぎ文は `<pre class="msg" id="m-…">` の中身）
2. `git commit` → `git push origin main` で数十秒後に公開反映
3. お繋ぎ文の正本は `aminde-consulting-dashboards/bni/data.php` と `.claude/skills/bni-matching/SKILL.md`。**そちらを先に直してからここへ**

## PDF版の作り方（2026-09-22 更新）

PDFの生成元は `bni/tools/build_1to1_doc.py`（HTMLを組み立てるスクリプト）。
**Web版の `index.html` とは別物**なので、内容を変えたら両方に反映すること。

```bash
cd "<repo>/bni/tools" && python3 build_1to1_doc.py            # → 1to1sheet_designed.html
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu \
  --no-pdf-header-footer --print-to-pdf="$PWD/sheet.pdf" --virtual-time-budget=20000 \
  "file://$PWD/1to1sheet_designed.html"
# sheet.pdf を pdf/ishijima_1to1_sheet.pdf に上書きして commit → push
```

- **LibreOffice（`soffice --convert-to pdf`）は使わない。** 日本語の一部が豆腐（□）になるフォント埋め込み不具合が出る（2026-09-22 実測）。Chromeのヘッドレス印刷なら再現しない
- 画像の元素材 `bni/tools/docexport/img_s/`（Googleドキュメントのzip展開・8MB超でgit対象外）は**現存しない**。スクリプトは `img/` の写真へ自動でフォールバックする（`FALLBACK` 辞書）。`image9.png`（表紙の画像）だけは元が特定できず `profile.jpg` を当てている ※要確認

## Googleドキュメント版

`build_1to1_doc.py` の末尾が Drive API で既存ドキュメントを上書きする。
**2026-09-22 時点で `~/.clasprc.json` のリフレッシュトークンが失効しており実行できない**（`python3 tools/gtoken.py` が 400 を返す）。
`clasp login` で再認証すれば復活する。トークンが無い間はスクリプトがHTML生成だけして正常終了するので、PDFは上記の手順で作れる。
