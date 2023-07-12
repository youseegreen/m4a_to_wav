# m4aをwavに変換する
Windowsのサウンドレコーダーで録音するとm4a形式で保存される。  
そのままだとプログラムで扱いにくかったので、ボタン1クリックでwavに変換してくれるスクリプトを作った。

## 環境構築
- python (3以上なら動くはず)
- ffmpeg (https://github.com/BtbN/FFmpeg-Builds/releases からダウンロードしてbinにパスを通しておく、ffmpeg -versionが通ればOK)
- pydub (mp3 -> wav変換に使用)
- このリポジトリをクローン

## 使い方
- m4a_to_wav/m4as/ に変換したいm4aファイルを入れる
- python m4a_to_wav.pyを実行、もしくは.batを自分の環境用に書き換え、それをクリック
- wavs, mp3sにファイルが作成される
