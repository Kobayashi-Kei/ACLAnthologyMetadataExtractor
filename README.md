# ACLAnthologyMetadataExtractor
ACLAnthologyScraperはACL Anthologyから論文のメタデータをスクレイピングするPythonスクリプトです。BeautifulSoup, re (正規表現), requestsを用いてウェブページを解析し、bibtexparserとjsonを用いて取得した情報を整形・保存します。

## 必要なライブラリ
BeautifulSoup
re
requests
bibtexparser
json
time
これらのパッケージは pip install または conda install コマンドを使用してPython環境にインストールできます。

## 使用方法
スクリプトをPython環境で実行します。
スクリプトがACL Anthologyからメタデータを自動的にダウンロードして、ローカルに保存します。
注意：このスクリプトはACL Anthologyのウェブサイトの変更に対応するため、定期的に更新が必要です。また、スクレイピングを行う際には適切な間隔を開けてサーバーに負荷をかけないようにしましょう。
