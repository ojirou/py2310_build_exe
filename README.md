"#py2310_build_exe" 

手順
1. 実行ファイルの元となるpythonスクリプト作成
2. setup.py作成
3. 上記1,2を同フォルダに保存
4. AnacondaPromptを起動して上記フォルダに移動
　下記でも同じ事ができる
　①エクスプローラでパスをクリック選択して「cmd」Enterクリック
　② C:\Users\user\anaconda3\Scripts\activate　実行
5. python setup.py build　実行

「build」フォルダが生成される、
「exe.win-amd64-3.10」フォルダ下にexeファイルが生成される