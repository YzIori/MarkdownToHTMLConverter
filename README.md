# Markdown to HTML Converter

マークダウンを HTML に変換するプログラムです。

## 実行

.md ファイルのパスである inputfile を受取り、出力パスに .html ファイルを出力します。<br>
以下のコマンドで実行します。

```bash
python3 file-converter.py markdown inputfile outputfile
```

## 実行例

以下のようなディレクトリ構成においてコマンドを実行します。

```bash
.
├── input.md
└── file-converter.py
```

以下のコマンドを実行します。入力は .md ファイル、出力は .html ファイルを指定してください。

```bash
python3 file-converter.py markdown input.md output.html
```

## NOTE

ディレクトリ内に outputpath で指定したファイル名と同名のファイルが存在する場合、エラーとなります。
