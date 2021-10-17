# preparation

tesseractをインストール

```
brew install tesseract
```

普通に使うなら以下
```
tesseract <IMAGE_FILE> <OUTPUT_FILE_NAME> -l <LANGUAGE>
```
<LANGUAGE>: eng, jpn, jpn_vert くらい


https://github.com/tesseract-ocr/tessdata から日本語をダウンロードしてパスに置く。多分下のとこ。

```
$ /usr/local/Cellar/tesseract/4.1.1/share/tessdata
```