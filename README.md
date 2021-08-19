# 抽出型文書要約
## 手続き
1. クリーニング(文区切り)
1. 文章の単語分割(形態素解析)
1. 単語の正規化(絵文字/記号などの削除，同じ意味を持つ単語の統一)
1. ストップワードの除去(名詞/形容詞/副詞/動詞のみの利用，辞書による除去)
1. 文書のベクトル表現(TF-IDF)*
1. 要約モデルの適用(LexRank)

## 使用技術/手法
coming soon

# 参考文献
## 要約に関する技術/手法
### 文章要約の全体なまとめ  
- [文書要約の歴史](https://qiita.com/siida36/items/4c0dbaa07c456a9fadd0)  

### テキストからセンテンス分割  
- [ja_sentence_segmenter](https://github.com/wwwcojp/ja_sentence_segmenter)  

### 前処理 (クリーニング処理)  
- [pythonによる日本語前処理備忘録](https://datumstudio.jp/blog/python%E3%81%AB%E3%82%88%E3%82%8B%E6%97%A5%E6%9C%AC%E8%AA%9E%E5%89%8D%E5%87%A6%E7%90%86%E5%82%99%E5%BF%98%E9%8C%B2/) ← かなり参考に
- [自然言語（前）処理](https://qiita.com/dcm_sawayama/items/406408e8bda0840a8106)  
- [自然言語処理における前処理の種類とその威力](https://qiita.com/Hironsan/items/2466fe0f344115aff177#%E3%82%B9%E3%83%88%E3%83%83%E3%83%97%E3%83%AF%E3%83%BC%E3%83%89%E3%81%AE%E9%99%A4%E5%8E%BB) ← 順を追って説明してくれる  
- [自然言語処理の前処理について](https://qiita.com/you_gin/items/03b6e5dc02892131cb9b) ← 絵文字の削除など  
- [データの前処理](https://zenn.dev/deepblackinc/books/5dd1d3acfcfd9e/viewer/07ad11) ← ベースはこれを参考にした  
- [Unicodeの正規化とテキストのクレンジング](https://tex2e.github.io/blog/python/unicodedata-normalize) ← 全角半角などの統一

### 形態素解析 (文章の単語分割)  
- [品詞推定(隠れマルコフ，ビタビアルゴリズム)](https://www.kabuku.co.jp/developers/hmm)  
- [【技術解説】形態素解析とは？MeCabインストール手順からPythonでの実行例まで](https://mieruca-ai.com/ai/morphological_analysis_mecab/) ← MeCabによる形態素解析  
- [Python: LexRankで日本語の記事を要約する](https://ohke.hateblo.jp/entry/2018/11/17/230000) ← janomeによる形態素解析  

### 単語の正規化  
- [自然言語処理における前処理の種類とその威力](https://qiita.com/Hironsan/items/2466fe0f344115aff177#%E8%BE%9E%E6%9B%B8%E3%82%92%E7%94%A8%E3%81%84%E3%81%9F%E5%8D%98%E8%AA%9E%E3%81%AE%E7%B5%B1%E4%B8%80)  
- [自然言語処理の前処理とMeCab(形態素解析エンジン)について](https://qiita.com/you_gin/items/03b6e5dc02892131cb9b#mecab%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6)  

### ストップワードの除去  
- [日本語ストップワードの考察【品詞別】](https://mieruca-ai.com/ai/nlp-stopwords/)  
- [MECABの形態素解析の結果から正規表現を使って品詞列を抜き出すMECABPR](https://yag-ays.github.io/project/mecab_pos_regex/)

### 単語/文の重要度 (単語/文の分散表現)  
- [TF-IDF(ある文における重要単語の抽出)](https://qiita.com/AwaJ/items/5937665d5a4152cc24cf)  
- [Word2Vecとは](https://ledge.ai/word2vec/)  

### 文章要約モデル (抽出型要約)  
- [LexRank](https://ramenjuniti.hatenablog.com/entry/2018/09/19/205330)  
- [LexRankによる代表文抽出](https://www.ai-shift.co.jp/techblog/938) ← 考え方がわかりやすい  
- [Pythonで長い文章をようやく可能！「sumy」](https://izanagiblog.com/archives/1164) ← LexRankの使い方がわかりやすい
- [sumyを使って青空文庫を要約してみる](https://qiita.com/hideki/items/5e9892094ae786d2ad6c)
- [Pythonによる自然言語処理技法をふんだんに使用した文書要約](https://software-data-mining.com/python%E3%81%AB%E3%82%88%E3%82%8B%E8%87%AA%E7%84%B6%E8%A8%80%E8%AA%9E%E5%87%A6%E7%90%86%E6%8A%80%E6%B3%95%E3%82%92%E3%81%B5%E3%82%93%E3%81%A0%E3%82%93%E3%81%AB%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%9F/) ← かなり参考に
- [A3RTとユーザーローカルの文章の自動要約を試してみた](https://crieit.net/posts/A3RT) ←[Doc2vecのAPI](https://a3rt.recruit-tech.co.jp/product/TextSummarizationAPI/)    

## 開発環境
- [Docker + MeCab + JupyterLabによる分析環境の構築](https://system.blog.uuum.jp/entry/2019/10/18/110000)