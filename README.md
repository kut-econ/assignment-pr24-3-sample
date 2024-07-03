# プログラミング2024 課題3

## 課題の内容

リストと制御構文を駆使して、次のことを実行するPythonスクリプト[prime.py](./prime.py)を完成させなさい。タスクごとにセルを分けて記述してください。

**Task 1.** 小さい方から数えて**ちょうど100個の素数**を格納したリスト`prime_numbers`を作成し、以下の出力例のように`prime_numbers`の要素を全て出力する。ただし10個ごとに改行すること。

```python
# 出力例
2 3 5 7 11 13 17 19 23 29
31 37 41 43 47 53 59 61 67 71
73 79 83 89 97 101 103 107 109 113
127 131 137 139 149 151 157 163 167 173
179 181 191 193 197 199 211 223 227 229
233 239 241 251 257 263 269 271 277 281
283 293 307 311 313 317 331 337 347 349
353 359 367 373 379 383 389 397 401 409
419 421 431 433 439 443 449 457 461 463
467 479 487 491 499 503 509 521 523 541
```

**ヒント:** リストの長さは関数`len`で調べることができます。ただし`len`を使わなくても書けます。

**Task 2.** 以下のように、Task 1で作った`prime_numbers`の要素を逆順に出力する。やはり10個ごとに改行すること。

```python
# 出力例
541 523 521 509 503 499 491 487 479 467
463 461 457 449 443 439 433 431 421 419
409 401 397 389 383 379 373 367 359 353
349 347 337 331 317 313 311 307 293 283
281 277 271 269 263 257 251 241 239 233
229 227 223 211 199 197 193 191 181 179
173 167 163 157 151 149 139 137 131 127
113 109 107 103 101 97 89 83 79 73
71 67 61 59 53 47 43 41 37 31
29 23 19 17 13 11 7 5 3 2
```

**ヒント:** いろんなやり方がありますが、いったん逆順に並んだリストを作ってから印字するのも一つの方法です(教科書セクション6.1.2参照)。

**Task 3.** 以下のように、Task 1で作った`prime_numbers`のうち、偶数番目に現れる素数のみを出力する。やはり10個ごとに改行すること。

```python
# 出力例
3 7 13 19 29 37 43 53 61 71
79 89 101 107 113 131 139 151 163 173
181 193 199 223 229 239 251 263 271 281
293 311 317 337 349 359 373 383 397 409
421 433 443 457 463 479 491 503 521 541
```

**Task 4.** 以下のように、Task 1で作った`prime_numbers`の要素のうち、素数番目に現れる素数(これを[スーパー素数](https://ja.wikipedia.org/wiki/スーパー素数)と呼ぶ)のみを出力する。すなわち、2番目、3番目、5番目、7番目、11番目・・・に現れる素数のみを出力する。5個ごとに改行すること。

```python
# 出力例
3 5 11 17 31
41 59 67 83 109
127 157 179 191 211
241 277 283 331 353
367 401 431 461 509
```

**ヒント:** ちょうど5個で改行するのが意外と難しく感じるかもしれません。一つ素数を出力するごとに+1増加するようなカウンタ変数を作成し、この変数を用いて改行のタイミングを制御するのが一つの方法です。あるいはいったんスーパー素数のリストを作成するのでも良いでしょう。
