# CORSハンズオン

## 読者へ

このハンズオンでは、ブラウザにおけるCORSの挙動をサーバとなるPythonコードをいじりながら理解していくことを目的としています。このハンズオンでは、CORSについてざっくりとした解説しかしないため、より詳細を知りたい方はMDNの[オリジン間リソース共有 (CORS)](https://developer.mozilla.org/ja/docs/Web/HTTP/CORS)を参照することをお奨めします。

## CORS

Cross-Origin Resource Sharing (CORS) は、ブラウザ上で動作するスクリプトが異なるオリジンのリソースとやり取りできるようにするためのプロトコルです。

オリジンとは: [Origin (オリジン)](https://developer.mozilla.org/ja/docs/Glossary/Origin)

CORSは、リクエストの特性によって次のどちらかの動作をします。

- 単純リクエスト(Simple Requests)
- プリフライトリクエスト(Preflight requests)

以下の条件を満たすものは単純リクエストとなります。

|条件|項目|
|---|---|
|メソッドが以下の中に含まれる|<ul><li>`GET`</li><li>`HEAD`</li><li>`POST`</li></ul>|
|独自で設定するヘッダーが以下の中に含まれる|<ul><li>`Accept`</li><li>`Accept-Language`</li><li>`Content-Length`</li><li>`Content-Type`(以下の値のみ)<ul><li>`application/x-www-form-urlencoded`</li><li>`multipart/form-data`</li><li>` text/plain`</li></ul></ul>|
