# 第3回
## 迷路ゲーム：迷えるこうかとん（ex03/maze.py）
### ゲーム概要
- ex03/maze.pyを実行すると，1500x900のcanvasに迷路が描画され，迷路に沿ってこうかとんを移動させるゲーム
- 実行するたびに迷路の構造は変化する

### 操作方法
- 矢印キーでこうかとんを上下左右に移動する

### 追加機能
- スタートとゴールの印追加
- ゴール後、移動しなくなる機能の実装
- 迷路の各角でゴールの方向のヒントが出る機能
- ゴールまでの移動回数をカウントしゴール後に開示する機能
- 平均２２回でゴール出来るゲームなので、
３０回移動してゴールしてない場合煽り文が出る

### ToDo（実装しようと思ったけど時間がなかった）
- 自動で動くお邪魔キャラの追加
- 落とし穴の追加
- wasdでその方向に壁に当たるまで突き進む

### メモ
- c_tで動いた回数をカウントしている
- c_tはこうかとんと移動するときにカウントが
行われる