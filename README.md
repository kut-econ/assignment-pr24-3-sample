# プログラミング2024 課題3

## 課題の内容

### Q1. 3が入っている数を探すプログラム

3桁の自然数のうち、100の位、10の位、1の位の少なくともどれか一つが3であるようなものを全て印字するPythonスクリプト[three.py](./three.py)を作成しなさい。その際、数字と数字の間には空白を入れ、8個印字するごとに改行しなさい。このプログラムの出力は以下のようになります。

```python
# 出力例
3 13 23 30 31 32 33 34
35 36 37 38 39 43 53 63
73 83 93 103 113 123 130 131
132 133 134 135 136 137 138 139
143 153 163 173 183 193 203 213
223 230 231 232 233 234 235 236
237 238 239 243 253 263 273 283
293 300 301 302 303 304 305 306
307 308 309 310 311 312 313 314
315 316 317 318 319 320 321 322
323 324 325 326 327 328 329 330
331 332 333 334 335 336 337 338
339 340 341 342 343 344 345 346
347 348 349 350 351 352 353 354
355 356 357 358 359 360 361 362
363 364 365 366 367 368 369 370
371 372 373 374 375 376 377 378
379 380 381 382 383 384 385 386
387 388 389 390 391 392 393 394
395 396 397 398 399 403 413 423
430 431 432 433 434 435 436 437
438 439 443 453 463 473 483 493
503 513 523 530 531 532 533 534
535 536 537 538 539 543 553 563
573 583 593 603 613 623 630 631
632 633 634 635 636 637 638 639
643 653 663 673 683 693 703 713
723 730 731 732 733 734 735 736
737 738 739 743 753 763 773 783
793 803 813 823 830 831 832 833
834 835 836 837 838 839 843 853
863 873 883 893 903 913 923 930
931 932 933 934 935 936 937 938
939 943 953 963 973 983 993 
```

#### Q1. ヒント

- ３つの条件A, B, Cの少なくともどれか一つが成り立っているときにTrueになる条件式は、`A or B or C`と書くことができます。
- 3桁の自然数が与えられたとき、100の位、10の位、1の位の数は`//`と`%`を使ってどのように表現できるか考えましょう。
- 次のように、単純なプログラムから初めて、段階的に少しずつ複雑にしてくようにしましょう。
  - まずは、与えられた3桁の数から、100の位、10の位、1の位を取り出すプログラムを書きましょう。
  - 与えられた3桁の数に3が含まれているかどうか判定するプログラムを書きましょう。
  - 1000未満の自然数のうち、3が含まれている自然数を全て印字するプログラムを書きましょう。
  - 最後に、8個印字するごとに改行するようにプログラムを修正しましょう。
- 8個ずつ改行するには、1個印字するごとに1だけ増加するようなカウンタ変数を用意してやれば良いです。

### Q2. 完全数を探すプログラム

自然数の約数のうち、自分自身以外の約数を真の約数と呼びます。たとえば6の約数は1,2,3,6ですので、真の約数は1,2,3です。真の約数の和が自分自身に等しい自然数を[完全数](https://ja.wikipedia.org/wiki/完全数)と呼びます。たとえば6の真の約数の和は1+2+3=6なので6は完全数です。一方、真の約数の和が1であれば、その数は素数です。1000未満の全ての数について、自分自身と真の約数の和をセットで印字するプログラム[perfect_number.py](./perfect_number.py)を作成しなさい。また、完全数であれば"完全数"、素数であれば"素数"と印字しなさい。出力例は次の通りです。1000未満の完全数は6,28,496の3つしかないので、それを確認しなさい。

#### Q2. ヒント

```python
# 出力例
1 0
2 1 素数
3 1 素数
4 3
5 1 素数
6 6 完全数
7 1 素数
8 7
9 4
10 8
11 1 素数
12 16
13 1 素数
14 10
15 9
16 15
17 1 素数
18 21
19 1 素数
20 22
21 11
22 14
23 1 素数
24 36
25 6
26 16
27 13
28 28 完全数
29 1 素数
30 42
31 1 素数
32 31
33 15
34 20
35 13
36 55
37 1 素数
38 22
39 17
40 50
41 1 素数
42 54
43 1 素数
44 40
45 33
46 26
47 1 素数
48 76
49 8
50 43
51 21
52 46
53 1 素数
54 66
55 17
56 64
57 23
58 32
59 1 素数
60 108
61 1 素数
62 34
63 41
64 63
65 19
66 78
67 1 素数
68 58
69 27
70 74
71 1 素数
72 123
73 1 素数
74 40
75 49
76 64
77 19
78 90
79 1 素数
80 106
81 40
82 44
83 1 素数
84 140
85 23
86 46
87 33
88 92
89 1 素数
90 144
91 21
92 76
93 35
94 50
95 25
96 156
97 1 素数
98 73
99 57
100 117
101 1 素数
102 114
103 1 素数
104 106
105 87
106 56
107 1 素数
108 172
109 1 素数
110 106
111 41
112 136
113 1 素数
114 126
115 29
116 94
117 65
118 62
119 25
120 240
121 12
122 64
123 45
124 100
125 31
126 186
127 1 素数
128 127
129 47
130 122
131 1 素数
132 204
133 27
134 70
135 105
136 134
137 1 素数
138 150
139 1 素数
140 196
141 51
142 74
143 25
144 259
145 35
146 76
147 81
148 118
149 1 素数
150 222
151 1 素数
152 148
153 81
154 134
155 37
156 236
157 1 素数
158 82
159 57
160 218
161 31
162 201
163 1 素数
164 130
165 123
166 86
167 1 素数
168 312
169 14
170 154
171 89
172 136
173 1 素数
174 186
175 73
176 196
177 63
178 92
179 1 素数
180 366
181 1 素数
182 154
183 65
184 176
185 43
186 198
187 29
188 148
189 131
190 170
191 1 素数
192 316
193 1 素数
194 100
195 141
196 203
197 1 素数
198 270
199 1 素数
200 265
201 71
202 104
203 37
204 300
205 47
206 106
207 105
208 226
209 31
210 366
211 1 素数
212 166
213 75
214 110
215 49
216 384
217 39
218 112
219 77
220 284
221 31
222 234
223 1 素数
224 280
225 178
226 116
227 1 素数
228 332
229 1 素数
230 202
231 153
232 218
233 1 素数
234 312
235 53
236 184
237 83
238 194
239 1 素数
240 504
241 1 素数
242 157
243 121
244 190
245 97
246 258
247 33
248 232
249 87
250 218
251 1 素数
252 476
253 35
254 130
255 177
256 255
257 1 素数
258 270
259 45
260 328
261 129
262 134
263 1 素数
264 456
265 59
266 214
267 93
268 208
269 1 素数
270 450
271 1 素数
272 286
273 175
274 140
275 97
276 396
277 1 素数
278 142
279 137
280 440
281 1 素数
282 294
283 1 素数
284 220
285 195
286 218
287 49
288 531
289 18
290 250
291 101
292 226
293 1 素数
294 390
295 65
296 274
297 183
298 152
299 37
300 568
301 51
302 154
303 105
304 316
305 67
306 396
307 1 素数
308 364
309 107
310 266
311 1 素数
312 528
313 1 素数
314 160
315 309
316 244
317 1 素数
318 330
319 41
320 442
321 111
322 254
323 37
324 523
325 109
326 166
327 113
328 302
329 55
330 534
331 1 素数
332 256
333 161
334 170
335 73
336 656
337 1 素数
338 211
339 117
340 416
341 43
342 438
343 57
344 316
345 231
346 176
347 1 素数
348 492
349 1 素数
350 394
351 209
352 404
353 1 素数
354 366
355 77
356 274
357 219
358 182
359 1 素数
360 810
361 20
362 184
363 169
364 420
365 79
366 378
367 1 素数
368 376
369 177
370 314
371 61
372 524
373 1 素数
374 274
375 249
376 344
377 43
378 582
379 1 素数
380 460
381 131
382 194
383 1 素数
384 636
385 191
386 196
387 185
388 298
389 1 素数
390 618
391 41
392 463
393 135
394 200
395 85
396 696
397 1 素数
398 202
399 241
400 561
401 1 素数
402 414
403 45
404 310
405 321
406 314
407 49
408 672
409 1 素数
410 346
411 141
412 316
413 67
414 522
415 89
416 466
417 143
418 302
419 1 素数
420 924
421 1 素数
422 214
423 201
424 386
425 133
426 438
427 69
428 328
429 243
430 362
431 1 素数
432 808
433 1 素数
434 334
435 285
436 334
437 43
438 450
439 1 素数
440 640
441 300
442 314
443 1 素数
444 620
445 95
446 226
447 153
448 568
449 1 素数
450 759
451 53
452 346
453 155
454 230
455 217
456 744
457 1 素数
458 232
459 261
460 548
461 1 素数
462 690
463 1 素数
464 466
465 303
466 236
467 1 素数
468 806
469 75
470 394
471 161
472 428
473 55
474 486
475 145
476 532
477 225
478 242
479 1 素数
480 1032
481 51
482 244
483 285
484 447
485 103
486 606
487 1 素数
488 442
489 167
490 536
491 1 素数
492 684
493 47
494 346
495 441
496 496 完全数
497 79
498 510
499 1 素数
500 592
501 171
502 254
503 1 素数
504 1056
505 107
506 358
507 225
508 388
509 1 素数
510 786
511 81
512 511
513 287
514 260
515 109
516 716
517 59
518 394
519 177
520 740
521 1 素数
522 648
523 1 素数
524 400
525 467
526 266
527 49
528 960
529 24
530 442
531 249
532 588
533 55
534 546
535 113
536 484
537 183
538 272
539 145
540 1140
541 1 素数
542 274
543 185
544 590
545 115
546 798
547 1 素数
548 418
549 257
550 566
551 49
552 888
553 87
554 280
555 357
556 424
557 1 素数
558 690
559 57
560 928
561 303
562 284
563 1 素数
564 780
565 119
566 286
567 401
568 512
569 1 素数
570 870
571 1 素数
572 604
573 195
574 434
575 169
576 1075
577 1 素数
578 343
579 197
580 680
581 91
582 594
583 65
584 526
585 507
586 296
587 1 素数
588 1008
589 51
590 490
591 201
592 586
593 1 素数
594 846
595 269
596 454
597 203
598 410
599 1 素数
600 1260
601 1 素数
602 454
603 281
604 460
605 193
606 618
607 1 素数
608 652
609 351
610 506
611 61
612 1026
613 1 素数
614 310
615 393
616 824
617 1 素数
618 630
619 1 素数
620 724
621 339
622 314
623 97
624 1112
625 156
626 316
627 333
628 478
629 55
630 1242
631 1 素数
632 568
633 215
634 320
635 133
636 876
637 161
638 442
639 297
640 890
641 1 素数
642 654
643 1 素数
644 700
645 411
646 434
647 1 素数
648 1167
649 71
650 652
651 373
652 496
653 1 素数
654 666
655 137
656 646
657 305
658 494
659 1 素数
660 1356
661 1 素数
662 334
663 345
664 596
665 295
666 816
667 53
668 508
669 227
670 554
671 73
672 1344
673 1 素数
674 340
675 565
676 605
677 1 素数
678 690
679 105
680 940
681 231
682 470
683 1 素数
684 1136
685 143
686 514
687 233
688 676
689 67
690 1038
691 1 素数
692 526
693 555
694 350
695 145
696 1104
697 59
698 352
699 237
700 1036
701 1 素数
702 978
703 57
704 820
705 447
706 356
707 109
708 972
709 1 素数
710 586
711 329
712 638
713 55
714 1014
715 293
716 544
717 243
718 362
719 1 素数
720 1698
721 111
722 421
723 245
724 550
725 205
726 870
727 1 素数
728 952
729 364
730 602
731 61
732 1004
733 1 素数
734 370
735 633
736 776
737 79
738 900
739 1 素数
740 856
741 379
742 554
743 1 素数
744 1176
745 155
746 376
747 345
748 764
749 115
750 1122
751 1 素数
752 736
753 255
754 506
755 157
756 1484
757 1 素数
758 382
759 393
760 1040
761 1 素数
762 774
763 117
764 580
765 639
766 386
767 73
768 1276
769 1 素数
770 958
771 261
772 586
773 1 素数
774 942
775 217
776 694
777 439
778 392
779 61
780 1572
781 83
782 514
783 417
784 983
785 163
786 798
787 1 素数
788 598
789 267
790 650
791 121
792 1548
793 75
794 400
795 501
796 604
797 1 素数
798 1122
799 65
800 1153
801 369
802 404
803 85
804 1100
805 347
806 538
807 273
808 722
809 1 素数
810 1368
811 1 素数
812 868
813 275
814 554
815 169
816 1416
817 63
818 412
819 637
820 944
821 1 素数
822 834
823 1 素数
824 736
825 663
826 614
827 1 素数
828 1356
829 1 素数
830 682
831 281
832 946
833 193
834 846
835 173
836 844
837 443
838 422
839 1 素数
840 2040
841 30
842 424
843 285
844 640
845 253
846 1026
847 217
848 826
849 287
850 824
851 61
852 1164
853 1 素数
854 634
855 705
856 764
857 1 素数
858 1158
859 1 素数
860 988
861 483
862 434
863 1 素数
864 1656
865 179
866 436
867 361
868 924
869 91
870 1290
871 81
872 778
873 401
874 566
875 373
876 1196
877 1 素数
878 442
879 297
880 1352
881 1 素数
882 1341
883 1 素数
884 880
885 555
886 446
887 1 素数
888 1392
889 135
890 730
891 561
892 676
893 67
894 906
895 185
896 1144
897 447
898 452
899 61
900 1921
901 71
902 610
903 505
904 806
905 187
906 918
907 1 素数
908 688
909 417
910 1106
911 1 素数
912 1568
913 95
914 460
915 573
916 694
917 139
918 1242
919 1 素数
920 1240
921 311
922 464
923 85
924 1764
925 253
926 466
927 425
928 962
929 1 素数
930 1374
931 209
932 706
933 315
934 470
935 361
936 1794
937 1 素数
938 694
939 317
940 1076
941 1 素数
942 954
943 65
944 916
945 975
946 638
947 1 素数
948 1292
949 87
950 910
951 321
952 1208
953 1 素数
954 1152
955 197
956 724
957 483
958 482
959 145
960 2088
961 32
962 634
963 441
964 730
965 199
966 1338
967 1 素数
968 1027
969 471
970 794
971 1 素数
972 1576
973 147
974 490
975 761
976 946
977 1 素数
978 990
979 101
980 1414
981 449
982 494
983 1 素数
984 1536
985 203
986 634
987 549
988 972
989 67
990 1818
991 1 素数
992 1024
993 335
994 734
995 205
996 1356
997 1 素数
998 502
999 521
```
