詳細設計書
1. テーブル設計
テーブル名	カラム名	型	属性	説明
team	id	INT	PK, AUTO_INCREMENT	チームID
name	VARCHAR(255)	NOT NULL	チーム名
theme1	id	INT	PK, AUTO_INCREMENT	お題1ID
name	VARCHAR(255)	NOT NULL	お題1内容
theme2	id	INT	PK, AUTO_INCREMENT	お題2ID
name	VARCHAR(255)	NOT NULL	お題2内容
2. API設計
チーム関連
メソッド	パス	機能	リクエスト例	レスポンス例
GET	/teams	チーム一覧取得		[{"id":1,"name":"チームA"}]
POST	/teams	チーム追加	{"name":"チームA"}	{"id":1,"name":"チームA"}
DELETE	/teams/{id}	チーム削除		{"result":"ok"}
お題1関連
メソッド	パス	機能	リクエスト例	レスポンス例
GET	/theme1	お題1一覧取得		[{"id":1,"name":"お題1"}]
POST	/theme1	お題1追加	{"name":"お題1"}	{"id":1,"name":"お題1"}
DELETE	/theme1/{id}	お題1削除		{"result":"ok"}
お題2関連
メソッド	パス	機能	リクエスト例	レスポンス例
GET	/theme2	お題2一覧取得		[{"id":1,"name":"お題2"}]
POST	/theme2	お題2追加	{"name":"お題2"}	{"id":1,"name":"お題2"}
DELETE	/theme2/{id}	お題2削除		{"result":"ok"}
抽選関連
メソッド	パス	機能	リクエスト例	レスポンス例
POST	/draw	チーム×お題1×お題2のランダム組合せ抽選		[{"team":"チームA","theme1":"お題1","theme2":"お題2"}]
3. 画面設計（ざっくりイメージ）
お題01登録画面
お題1入力フォーム
お題1一覧表示
削除ボタン
お題02登録画面
お題2入力フォーム
お題2一覧表示
削除ボタン
チーム名登録画面
チーム名入力フォーム
チーム一覧表示
削除ボタン
抽選画面
「抽選する」ボタン
結果表示エリア
4. ディレクトリ構成
Apply to basic_design...
md
5. 使用技術
Python（FastAPI）
MySQL（MAMPでOK！）
Docker, docker-compose
6. 補足
APIは全部JSONでやりとりするスタイル！
DB接続情報は環境変数で管理して、セキュリティもアゲてこ！
最初はSwagger UIでAPIテストできるから、フロントなくても動作確認できるよ！