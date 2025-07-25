## Nowy koncept
Nowy koncept skryptu opiera się na pobieraniu samych krawędzi crossa, aby nie obliczać dla wszystkich krawędzi, ponieważ na ten moment nie jest to istotne. Interesują nas tylko ramiona crossa, które powinny znaleźć się po kolei we właściwym miejscu, czyli kiedy określona reprezentacja binarna jest spełniana dla danego pola na kostce.

Kostka wygląda w taki sposób:

Górna wartstwa
| | | |
|-|-|-|
| |36| |
|6| |5|
| |20| |
| |  | |


Środkowa wartstwa
| | | | |
|-|-|-|-|
|34|18|17|33|
|  |  |  |  |


Dolna warstwa
| | | |
|-|-|-|
| |24| |
|10| |9|
| |40| |
| |  | |


Na reprezentację binarną:
| Ruch | B | F | D | U | L | R | Wynik dziesiętny |
| ---- | - | - | - | - | - | - | ---------------- |
| UB   | 1 | 0 | 0 | 1 | 0 | 0 | 36     | 100     |
| UR   | 0 | 0 | 0 | 1 | 0 | 1 | 5      | 69      |
| UF   | 0 | 1 | 0 | 1 | 0 | 0 | 20     | 84      |
| UL   | 0 | 0 | 0 | 1 | 1 | 0 | 6      | 70      |
| DB   | 1 | 0 | 1 | 0 | 0 | 0 | 24     | 88      |
| DR   | 0 | 0 | 1 | 0 | 0 | 1 | 9      | 73      |
| DF   | 0 | 1 | 1 | 0 | 0 | 0 | 40     | 104     |
| DL   | 0 | 0 | 1 | 0 | 1 | 0 | 10     | 74      |
| LB   | 1 | 0 | 0 | 0 | 1 | 0 | 34     | 98      |
| RB   | 1 | 0 | 0 | 0 | 0 | 1 | 33     | 97      |
| RF   | 0 | 1 | 0 | 0 | 0 | 1 | 17     | 81      |
| LF   | 0 | 1 | 0 | 0 | 1 | 0 | 18     | 82      |


## Zakazane ruchy

Koncepcja powstała aby nie wykonywać zbędnych ruchów, które nie przemieszczą ramion crossa na kostce.
Używając funkcję or dla ramion crossa, które zostały zamienione na reprezentację binarną sposowduje że wykorzystując funkcję "or" tam gdzie jest "0", jesteśmy pewni że nie warto wykorzystywać tego ruchu.

### Dla przykładu:
Dla scrambla
`L2 B2 L2 U' B2 L2 U' R2 D' L2 U B2 R B' D F L F2 D F2` mamy nasze ramiona crossa znajdują się w miejscu
```
RB -> 100001
RF -> 010001
UL -> 000110
LF -> 010010
------------
OR    110111
```

Teraz jak przełożymy to na tabelę wyżej otrzymamy
| B | F | D | U | L | R |
| - | - | - | - | - | - |
| 1 | 1 | 0 | 1 | 1 | 1 |

czyli ruch D nic nam nie zmien

ps. Oczywiście wiem że używając ruchów, które nie wskazywałyby na ewaluację krzyża na dole są potrzebne do przygotowania kolejnych par, x-crossów itd., jednak skupiam się na samym optymalizowaniu wyodrębnienia dobrych prypadków crossa.

## Ruchy

Ruchy są zrobione tak, aby każdy ruch zamianiał postać binarną na następną postać binarną. One będą jeszcze dokładnie dopracowywane. Teraz zajmę się robieniem pętli


## Prędkość

Próby:

1,2,3 -> średnia ze 100
4 -> średnia z 10
5 -> średnia z 5
6 -> średnia z 1


| Zasady      | 1 | 2 | 3 | 4 | 5 | 6 |
| ----------- | - | - | - | - | - | - |
| Brak        | 8.05807113647461e-05 | 0.0012435793876647949 | 0.010737712383270264 | 0.170829176902771 | 2.8648971557617187 | 48.239978075027466 |
| [-1] != [-2]| 2.889871597290039e-05 | 0.00046373844146728514 | 0.007187414169311524 | 0.09732249736785889 | 1.450125551223755 | 22.14314079284668 |
| [-3] != [-1]| 2.291679382324219e-05 | 0.0005358791351318359 | 0.006567776203155518 | 0.10549061059951782 | 1.3592053413391114 | 19.99150848388672 |
| rozdzielenie na dwie pętle for | 2.3453235626220704e-05 | 0.000522007942199707 | 0.008277478218078614 | 0.08396749973297118 | 1.2110511302947997 | 16.85955786705017 |
| dodanie funkcji które pomija nieistotne ruchy | 4.1701793670654296e-05 | 0.0005760955810546875 | 0.00662555456161499 | 0.105507230758667 | 1.212249183654785 | 17.35208026568095 |
| dodanie sum do poprzedniej funkcji | 3.855705261230469e-05 | 0.0008545756340026855 | 0.00939859390258789 | 0.10680460453033447 | 1.4455292224884033 | 17.450045585632324 |
| DF          | 0 | 1 | 1 | 0 | 0 | 0 |
| DL          | 0 | 0 | 1 | 0 | 1 | 0 |
| LB          | 1 | 0 | 0 | 0 | 1 | 0 |
| RB          | 1 | 0 | 0 | 0 | 0 | 1 |
| RF          | 0 | 1 | 0 | 0 | 0 | 1 |
| LF          | 0 | 1 | 0 | 0 | 1 | 0 |


Na bicie 64 dodałem znak "-", przez co 